pipeline {
    agent {
        label 'master'
    }
    stages {
        stage('Echo credentials') {
            steps {
                    git branch: 'jenkins_backup', credentialsId: 'ssh_jenkins_master', url: 'git@github.com:techsparksguru/python_ci_automation.git'                    
                    script {
                        dir('python_ci_automation') {
                        sh 'echo $ssh_jenkins_master'
                        sh './backup-script.sh'
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs deleteDirs: true
        }
    }
}