#!/usr/bin/bash -xe
sudo yum install python -y
sudo yum install python-pip -y
sudo pip install ansible
ansible-playbook DevOps-Crypto/requirements.yml
ansible-playbook DevOps-Crypto/deploy.yml