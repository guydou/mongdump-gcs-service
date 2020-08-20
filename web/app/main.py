from flask import Flask
from google.cloud import storage


import os
import time 
app = Flask(__name__)

def mongodb_cmd(host, port, username, password, out):
   command = "mongodump --host {host} --port {port} --username {username} --password {password} --archive={out}".format(
              host=host, port=port, username=username, password=password, out=out)
   return command

def mongodb_conf():
    host = os.environ.get("MONGODB_HOST")
    port = os.environ.get("MONGODB_PORT")
    username = os.environ.get("MONGODB_USERNAME")
    password = os.environ.get("MONGODB_PASSWORD")
    return host, port, username, password

def render_output_locations():
  return "/tmp/" + time.strftime("%Y-%m-%d-%H:%M:%S")

def get_bucket_name():
   return "coqualabs-mongodb-backup"

@app.route("/start")
def runbackup():
    host, port, username, password = mongodb_conf()
    archive_file = render_output_locations()
    cmd = mongodb_cmd(host, port, username, password, archive_file)
    os.system(cmd)
    client = storage.Client()
    bucket = client.get_bucket(get_bucket_name())
    blob = bucket.blob(archive_file[4:])
    with open(archive_file, "rb") as archive_file_bin:
         blob.upload_from_file(archive_file_bin)
    return "Done"

@app.route("/test")
def test():
   client = storage.Client()
   bucket = client.get_bucket(get_bucket_name())
   return "list buckets: {blobs}".format(blobs=bucket.list_blobs())

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
