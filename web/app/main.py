from flask import Flask
import os
import time 
app = Flask(__name__)

def mongodb_cmd(host, port, username, password, out):
   command = "mongodump --host {host} --port {port} --username {username} --password {password} --out {out}".format(
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

@app.route("/start")
def runbackup():
    host, port, username, password = mongodb_conf()
    cmd = mongodb_cmd(host, port, username, password, render_output_locations())
    os.system(cmd)
    return cmd

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
