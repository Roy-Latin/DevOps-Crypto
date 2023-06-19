#!/usr/bin/bash -xe
tar -xvf /home/ec2-user/crypto.tar.gz
rm -r crypto.tar.gz
sudo yum install python -y
sudo yum install python-pip -y
sudo pip install ansible
ansible-playbook DevOps-Crypto/requirements.yml
ansible-playbook DevOps-Crypto/deploy.yml
./tests.sh