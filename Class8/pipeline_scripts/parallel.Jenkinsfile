pipeline {
  agent none
  stages {
    stage('Run Tests') {
      parallel {
        stage('Test On Windows') {
          agent {
            label "windows"
          }
          steps {
            bat "mkdir testdir"
            bat "dir"
            echo "Running on windows slave"

          }
        }
        stage('Test On Linux') {
          agent {
            label "linux"
          }
          steps {
            sh "mkdir test"
            sh "ls -la"
            echo "Running on linux slave"
          }
        }
      }
    }
  }
}