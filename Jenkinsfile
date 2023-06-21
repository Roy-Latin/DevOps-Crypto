pipeline {
    agent any
        environment {
        EC2_IP_TEST = "54.234.179.11"
        EC2_IP_MAIN = "54.160.178.222"
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
                sh 'ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/key.pem ec2-user@$EC2_IP_TEST'
                sh 'ssh -o StrictHostKeyChecking=no -i /var/lib/jenkins/key.pem ec2-user@$EC2_IP_MAIN'

            }
        }
        
       // stage('Fetch from S3 To EC2 - TEST-SERVER') {
         //   steps {
           //     withAWS(credentials: 'Jenkins-AWS') {
             //   sh 'aws s3 cp s3://roylatin-flask-artifacts/crypto.tar.gz /var/lib/jenkins/workspace/crypto.tar.gz'
                //sshagent(['aws-key-ssh']) {
                  //       sh 'scp -i /var/lib/jenkins/key.pem /var/lib/jenkins/workspace/crypto.tar.gz ec2-user@$EC2_IP_TEST:/home/ec2-user'
            //}
       // }
    //}
//}

        stage('Setting Up The Test Server And Running Checks') {
            steps {
                script {
                    withCredentials([sshUserPrivateKey(credentialsId: 'aws-key-ssh', keyFileVariable: 'KEY_FILE')]) {
                    sh 'scp -i /var/lib/jenkins/key.pem DevOps-Crypto ec2-user@$EC2_IP_TEST:/home/ec2-user'
                    sshagent(['aws-key-ssh']) {
                    sh """ 
                    ssh -o StrictHostKeyChecking=no -i $KEY_FILE ec2-user@$EC2_IP_TEST '
                    chmod +x DevOps-Crypto/setup.sh
                    ./DevOps-Crypto/setup.sh
                    '
                    """
                    sh 'chmod +x DevOps-Crypto/tests.sh'
                    sh './DevOps-Crypto/tests.sh'

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
                    sh 'scp -i /var/lib/jenkins/key.pem /var/lib/jenkins/workspace/crypto.tar.gz ec2-user@$EC2_IP_MAIN:/home/ec2-user'
                    sshagent(['aws-key-ssh']) {
                    sh """ 
                    ssh -o StrictHostKeyChecking=no -i $KEY_FILE ec2-user@$EC2_IP_MAIN '
                    tar -xvf /home/ec2-user/crypto.tar.gz
                    chmod +x DevOps-Crypto/setup.sh
                    ./DevOps-Crypto/setup.sh
                    '
                    """
                }
            }
        }
    }
}
}
}