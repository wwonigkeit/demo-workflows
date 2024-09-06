# 01 - Run any docker container

## Description

There are a couple of examples in this repository

### run-docker-container
This is the most simplest examples of how to run ANY container. In this case we use the Python container from hub.docker.com and run a Python code snippet. The progression of workflow complexity in the directory should be followed:
1. **run-docker-python-command.yaml**: run a simple Python command in the container with an on-demand container
2. **run-docker-python-code.yaml**: run a simple Python code snippet (`code/pythonExample.py`) in a Python on-demand container
3. **run-docker-python-code-service.yaml**: run a simple Python code snippet (`code/pythonExample.py`) in Direktiv scale 1 service (this is a stateful container / service configured with the `services/python.yaml` file)
4. **run-docker-python-code-service-gateway.yaml**: run a simple Python code snippet (code/pythonExample.py) in Direktiv scale 1 service (this is a stateful container / service), but executed using a POST. The gateway configuration is in the `gateway/v1/run-python.yaml` file. The sample curl command is shown below:
```sh
curl -i -X POST 'https://internal.direktiv.io/ns/demo-workflows/v1/run-python-code' --header 'Content-Type: text/xml' --data-binary '@/demo-workflows/run-docker-container/code/pythonExample.py'
```



1. run-docker-container
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
    "username": "s3-administrator",
    "password": "Direktiv"
}
```

