pipeline {
    agent any

    environment {
        IMAGE_NAME = "prasad1703/flask-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Prasad-1703/Jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKER_HUB_TOKEN')]) {
                    sh '''
                    echo $DOCKER_HUB_TOKEN | docker login -u prasad1703 --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
                sh 'docker run -d --name flask-container -p 5000:5000 $IMAGE_NAME'
            }
        }
    }
}
