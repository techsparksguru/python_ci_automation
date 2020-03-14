// This script waits until a user inputs value at the stage
pipeline {
    agent {
        label 'windows'
    }

    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }

    stages {
        stage('Build') {
            input{
                message "Press Ok to continue"
                submitter "DB_ENGINE"
                parameters {
                    string(name:'DB_ENGINE', defaultValue: 'sqlite', description: 'Enter the db engine')
                }
            }
            steps {
                echo "Database engine is ${DB_ENGINE}"
                echo "DISABLE_AUTH is ${DISABLE_AUTH}"
            }
        }
    }
}