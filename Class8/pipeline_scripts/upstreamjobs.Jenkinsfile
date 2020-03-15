pipeline {
   agent {
      label 'windows'
   }
   triggers {
      //Execute when either job1 or job2 are successful
      upstream(upstreamProjects: 'buildTrigger, parallel-pipeline', threshold: hudson.model.Result.SUCCESS)
   }
   stages {
      stage('console') {
         steps {
            echo "Printing on the console"
         }
      }
      stage('write') {
         steps {
            bat "echo writing this to the file > file.txt"
         }
      }
      stage('delete') {
         steps {
            bat "del file.txt"
         }
      }
      stage('create') {
         steps {
            bat "mkdir test_directory"
         }
      }
      stage('list') {
         steps {
            bat "dir"
            }
        }
    }
} 