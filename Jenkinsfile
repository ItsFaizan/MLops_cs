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
                    // Assuming Python and pip are already installed on Windows
                    // You can add additional checks or installation steps here if needed
                }
            }
        }
        
        stage('Install dependencies') {
            steps {
                script {
                    // Install Python dependencies using pip
                    bat 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run tests') {
            steps {
                script {
                    // Run tests using the appropriate Windows command
                    // This example assumes you have a script named 'test_script.py'
                    // Modify this according to your actual testing setup
                    bat 'python test_script.py'
                }
            }
        }
    }
}
