# 01 - Run any docker container

## Description

There are 2 configuration directories in this repository:

1. 01-run-docker-container
* run-docker-python.yaml: this will run a Docker container from hub.docker.com (specifically the Python container) as a knative-workflow instance. The premise of this worklflow is to show how we run ANY container using the `direktiv-cmd` configuration.
* run-docker-python-service.yaml: this will run a Docker container from hub.docker.com (specifically the Python container) as a knative-namespace service. The premise of this is to show how Direktiv services work. Use the following inputs:
```json
{
    "cmd": "--version"
}
```
```json
{
    "cmd": "-c \"print('hello world')\""
}
```
* run-docker-python-service-snippet.yaml: this will run a Docker container from hub.docker.com (specifically the Python container) as a knative-namespace service with a copde snippet:
```json
{
    "username": "s3-administartor",
    "password": "Direktiv"
}
```

NOT Finalised
