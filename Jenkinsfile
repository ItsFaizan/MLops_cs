pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/ItsFaizan/MLops_cs.git'
                }
            }
        }
        
        stage('Set up Python') {
            steps {
                script {
                    // Install Python
                    sh 'apt-get update && apt-get install -y python3 python3-pip'
                }
            }
        }
        
        stage('Install dependencies') {
            steps {
                script {
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        
        stage('Run tests') {
            steps {
                script {
                    sh 'make test'
                }
            }
        }
    }
}