pipeline {
    agent {
        label 'master'
    }
    stages {
        stage('Copy jobs and its configurations') {
            steps {
                    git branch: 'jenkins_backup', credentialsId: 'ssh_jenkins_master', url: 'git@github.com:techsparksguru/python_ci_automation.git'                    
                    script {
                        dir('python_ci_automation') {
                        sh 'rm -rf Backups/*'
                        sh './backup-script.sh'
                    }
                }
            }
        }
        stage('Backup files by pushing into the git repo') {
            steps {
                    script {
                        def date = new Date()
                        def commit_date = date.format("yyyyMMddHHmm")
                        println ${commit_date}
                        dir('python_ci_automation') {
                            sh 'git add --all'
                            sh 'git commit -m "Automated Jenkins commit - ${commit_date}"'
                            git push origin jenkins_backup
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