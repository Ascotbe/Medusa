#!/bin/bash
if [[ `uname` == 'Linux' ]]; then
    sudo apt update
    sudo apt install docker.io -y
    sudo systemctl start docker
    sudo docker build -t medusa_web .
    sudo docker run -d -i -t --name  medusa -p 80:80 -p 443:443 -p 53:53 medusa_web
fi
