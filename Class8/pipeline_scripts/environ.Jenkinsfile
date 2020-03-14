// https://jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables

def DISABLE_AUTH = 'false'
def DB_ENGINE = 'postgres'

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
            steps {
                echo "Database engine value from declared variable = ${DB_ENGINE}"
                echo "Database engine value from an environmental variable = ${env.DB_ENGINE}"
                echo "DISABLE_AUTH declared variable ${DISABLE_AUTH}"
                echo "DISABLE_AUTH environmental variable ${env.DISABLE_AUTH}"
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            }
        }
    }
}