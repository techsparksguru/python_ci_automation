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
                echo "Database engine is ${DB_ENGINE}"
                echo "DISABLE_AUTH is ${DISABLE_AUTH}"
            }
        }
    }
    post { 
        always { 
            echo 'I will always run this!'
            cleanWs deleteDirs: true, notFailBuild: true
        }
    }
}