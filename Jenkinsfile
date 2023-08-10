pipeline {
    agent any
        environment {
        EC2_IP_TEST = "52.207.237.140"
        EC2_IP_PROD = "54.164.184.153"
    }
    stages {
        stage('Cleanup And Clone') {
            steps {
                sh 'echo "Performing cleanup And Cloning Git Repo..."'
                sh 'rm -rf *'
                sh 'git clone https://github.com/Roy-Latin/DevOps-Crypto.git'
            }
        }
        stage('Packaging And Pushing To S3') {
            steps {
                sh 'echo "packaging And Pushing To S3..."'
                sh 'tar -czvf crypto.tar.gz DevOps-Crypto'
                sh 'aws s3 cp crypto.tar.gz s3://roylatin-flask-artifacts'
            }
        }
        stage('check for the connection'){
            steps {
                sh 'ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/key.pem ec2-user@$EC2_IP_TEST'
                sh 'ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/key.pem ec2-user@$EC2_IP_PROD'

            }
        }
        stage('Setting Up The Test Server And Running Checks') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'aws-key-ssh', keyFileVariable: 'KEY_FILE')]) {
                    sh 'scp -i $KEY_FILE -r DevOps-Crypto ec2-user@$EC2_IP_TEST:/home/ec2-user'
                    sshagent(['aws-key-ssh']) {
                    sh """ 
                    ssh -o StrictHostKeyChecking=no -i $KEY_FILE ec2-user@$EC2_IP_TEST '
                    chmod +x DevOps-Crypto/scripts/setup.sh
                    ./DevOps-Crypto/scripts/setup.sh
                    '
                    """
                    sh 'chmod +x DevOps-Crypto/scripts/tests.sh'
                    sh './DevOps-Crypto/scripts/tests.sh'

                }
            }
        }
    }
} 
        stage('Deploying On Prod. Server') {
            steps {
                sh 'echo "Deploying..."'
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'aws-key-ssh', keyFileVariable: 'KEY_FILE')]) {
                    sh 'scp -i $KEY_FILE -r DevOps-Crypto ec2-user@$EC2_IP_PROD:/home/ec2-user'
                    sshagent(['aws-key-ssh']) {
                    sh """ 
                    ssh -o StrictHostKeyChecking=no -i $KEY_FILE ec2-user@$EC2_IP_PROD '
                    chmod +x DevOps-Crypto/scripts/setup.sh
                    ./DevOps-Crypto/scripts/setup.sh
                    '
                    """
                }
            }
        }
    }
}
}
}