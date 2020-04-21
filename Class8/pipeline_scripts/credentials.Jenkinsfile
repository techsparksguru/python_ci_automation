pipeline {
    agent any
    environment {
        secret = credentials('SECRET_TEXT')
    }
    stages {
        stage('Echo credentials') {
            steps {
                sh 'echo $secret'
            }
        }
    }
}