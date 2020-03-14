pipeline {
   agent any

   stages {
      stage('Example') {
         steps {
            script {
               try {
                  sh 'exit 1'
               } catch (exc) {
                  echo 'Something failed, I should sound the klaxons!'
                  echo exc.getMessage()
               }
            }
         }
      }
   }
}