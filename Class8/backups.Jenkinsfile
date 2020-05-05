pipeline {
    agent {
        label 'master'
    }

    // Triggers function runs the job automatically based on cron date-time specified
    triggers {
        cron('H 23 * * 6')
    }
    stages {
        stage('Copy jobs and its configurations') {
            steps {
                git branch: 'jenkins_backup', credentialsId: 'ssh_jenkins_master', url: 'git@github.com:techsparksguru/python_ci_automation.git'                    
                sh './backup-script.sh'
            }
        }
        stage('Backup files by pushing into the git repo') {
            steps {
                    script {
                    def date = new Date()
                    def commit_date = date.format("yyyy-MM-dd'T'HH:mm:ss")
                    def commit_msg = "Automated Jenkins commit - ${commit_date}"
                    println "${commit_date}"
                    dir('python_ci_automation') {
                        sh 'git add --all'
                        sh "git commit -m '${commit_msg}'"
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