pipeline {
    agent any
        environment {
        EC2_IP_TEST = "18.212.98.180"
    }

    stages {
        stage('Cleanup And Clone') {
            steps {
                sh 'echo "Performing cleanup..."'
                sh 'rm -rf *'
                sh 'echo "Cloning..."'
                sh 'git clone https://github.com/Roy-Latin/DevOps-Crypto.git'
                sh 'ls'
            }
        }
        stage('Packaging And Pushing To S3') {
            steps {
                sh 'echo "packaging"'
                sh 'tar -czvf crypto.tar.gz DevOps-Crypto'
                sh 'ls'
                sh 'echo "pushing to s3"'
                sh 'echo "packaging"'
                sh 'aws s3 cp crypto.tar.gz s3://roylatin-flask-artifacts'
            }
        }
        
        stage('check for the connection'){
            steps {
                sh 'ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/key.pem ec2-user@${EC2_IP_TEST}'
            }
        }
        
        stage('Fetch from S3 To EC2 - TEST-SERVER') {
            steps {
                withAWS(credentials: 'Jenkins-AWS') {
                sh 'aws s3 cp s3://roylatin-flask-artifacts/crypto.tar.gz /var/lib/jenkins/workspace/crypto.tar.gz'
                sshagent(['aws-key-ssh']) {
                         sh 'scp -i /var/lib/jenkins/key.pem /var/lib/jenkins/workspace/crypto.tar.gz ec2-user@${EC2_IP_TEST}:/home/ec2-user'
            }
        }
    }
}

        stage('Setting Up The Test Server') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'aws-key-ssh', keyFileVariable: 'KEY_FILE')]) {
                    sshagent(['aws-key-ssh']) {
                    sh """ 
                    ssh -o StrictHostKeyChecking=no -i $KEY_FILE ec2-user@${EC2_IP_TEST} '
                    tar -xvf /home/ec2-user/crypto.tar.gz
                    rm -r crypto.tar.gz
                    sudo yum install python -y
                    sudo yum install python-pip -y
                    sudo pip install ansible
                    chmod +x DevOps-Crypto/tests.sh
                    ansible-playbook DevOps-Crypto/requirements.yml
                    ansible-playbook DevOps-Crypto/deploy.yml
                    ./DevOps-Crypto/tests.sh "${EC2_IP_TEST}"
                    '
                    """
                }
            }
        }
    }
}

        
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'aws-key-ssh', keyFileVariable: 'KEY_FILE')]) {
                    sshagent(['aws-key-ssh']) {
                    sh """ 
                    ssh -i $KEY_FILE ec2-user@${EC2_IP} '
                    ansible-playbook DevOps-Crypto/deploy.yml
                    '
                    """
                }
            }
        }
    }
}
}
}
