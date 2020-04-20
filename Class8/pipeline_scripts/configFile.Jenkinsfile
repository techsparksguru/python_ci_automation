pipeline {
    agent any
    stages {
        stage('Echo credentials') {
            steps {
                    configFileProvider([configFile(fileId: '1a583362-97dd-4521-84b4-9040bbc850d6', variable: 'pemfile')]) {
                    sh 'echo $pemfile'
                    sh 'cp $pemfile /home/ubuntu/jenkins/privatekey.pem'
                    sh 'ls /home/ubuntu/jenkins/'
                }
            }
        }
    }
}