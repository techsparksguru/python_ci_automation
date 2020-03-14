// https://jenkins.io/doc/book/pipeline/syntax/#cron-syntax
pipeline {
    agent any
    triggers {
        cron('30 22 15 * *')
    }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
}