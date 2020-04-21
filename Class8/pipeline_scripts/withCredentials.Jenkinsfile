pipeline {
    agent any
    stages {
        stage('Echo credentials') {
            steps {
                withCredentials([string(credentialsId: 'SECRET_TEXT', variable: 'mysecrettext')]) {
                    sh 'echo $mysecrettext'
                }
            }
        }
    }
}