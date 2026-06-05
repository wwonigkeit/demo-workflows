FROM alpine:latest

RUN apk add --no-cache python3 py3-pip \
    && pip3 install --no-cache-dir boto3 --break-system-packages \
    && pip3 install --no-cache-dir ansible --break-system-packages \
    && ansible-galaxy collection install amazon.aws ansible.posix

CMD ["/bin/sh"]
