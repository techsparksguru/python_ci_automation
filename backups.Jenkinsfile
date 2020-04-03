pipeline {
    agent {
        label 'master'
    }
    triggers {
        cron('30 23 * * 6')
    }
    stages {
        stage('Copy jobs and its configurations') {
            steps {
                git branch: 'jenkins_backup', credentialsId: 'ssh_jenkins_credential', url: 'git@github.com:techsparksguru/python_ci_automation.git'                    
                sh './backup-script.sh'
            }
        }
        stage('Backup files by pushing into the git repo') {
            steps {
                script {
                    def date = new Date()
                    def commit_date = date.format("yyyy-MM-dd'T'HH:mm:ss")
                    println "${commit_date}"
                    dir('python_ci_automation') {
                        sh 'git add --all'
                        sh "git commit -m 'This is an auto commit - ${commit_date}'"
                        sh 'git push origin jenkins_backup'
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