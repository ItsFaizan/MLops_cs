pipeline {
    agent any
    
    stages {

        stage('Cloning from git') {
            steps {
                git branch: 'main', url: 'https://github.com/ItsFaizan/MLops_cs'
            }
        }

        stage('Installation of dependencies') {
            steps {
                bat 'pip3 install -r requirements.txt'
                echo 'Dependencies successfully installed!'
            }
        }

        stage('Test') {
            steps {
                bat 'python test.py'
                echo 'Tests passed!'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo 'Deploying to production...'
                        
                    } else {
                        echo 'Deploying to development server...'
                        
                    }
                }
            }
        }
    }
}
