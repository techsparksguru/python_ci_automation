pipeline {
   agent any
   parameters {
      string(name: 'BRANCH_NAME', defaultValue: '', description: 'Enter the branchname')
   }
   stages {
      stage('Example') {
         steps {
            script {
               if (params.BRANCH_NAME == 'master') {
                  echo 'I only execute on the master branch'
               } else {
                  echo 'I execute elsewhere'
               }
            }
         }
      }
   }
}