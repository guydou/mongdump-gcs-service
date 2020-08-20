# mongdump-gcs-service

I created this project to run a service in google cloud run. 
The service does a `mongodump` to archive file and upload it to a GCS

## Warning
I haven't yet a chance to run this code on production environment, use this code with care. 
## Docker
The image is published in dockerhub [here](https://hub.docker.com/repository/docker/guydou/mongdump-gcs-service)

```shell script
docker pull guydou/mongdump-gcs-service
``` 

### Configuration
The configuration is done through environment variables.

| Field   |      Description | 
|----------|:-------------:|
| MONGODB_HOST |  hostname where the mongo is found |
| MONGODB_PORT| the port of mongodb (no default) |
| MONGODB_USERNAME |     |  
| MONGODB_PASSWORD |  |   
| GOOGLE_APPLICATION_CREDENTIALS| the location of the google conf file|
| GCS_BUCKET | The bucket to which the dump will be written|

Execution example
```shell script
docker run guydou/mongdump-gcs-service -e MONGODB_HOST=host/
 -e MONGODB_PORT=27017 -e MONGODB_USERNAME=username -e MONGODB_PASSWORD=password -e GCS_BUCKET=bucket/
-e GOOGLE_APPLICATION_CREDENTIALS=/conf/keyfile.json -v /loction/of/key/file:/conf/keyfile.json
```

## Running on local machine
When developing you could run the service using the docker-composue in the repo. 
This compose file runs also a mongodb. 
The container still needs GOOGLE_APPLICATION_CREDENTIALS as I didn't mock the the GCS service.

After setting up the docker-compose, execute:
```
docker-compose up
```

And then go to http://localhost/start

