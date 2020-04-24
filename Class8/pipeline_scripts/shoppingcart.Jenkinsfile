pipeline {
    agent {
        label 'master'
    }   
    parameters {
        string(name: 'GIT_BRANCH',
           description: 'Please input the git branch from which the code should be checkout',
           defaultValue: 'pom_fixes')
    }
    stages {
        stage('checkout') {
            steps {
	             git branch: '${GIT_BRANCH}', url: 'https://github.com/suhimanju/Python_Page_Object'
	             sh 'ls -al'
               }
        } // stage
        stage('Execute') {
            steps {
                    sh 'pip3 install -r requirements.txt'
                    sh 'behave features/CompleteShoppingCart.feature:71 -D BROWSER=chrome -D HEADLESS=True --no-capture --junit'
		            sh 'python3 -m behave2cucumber -i results.json -o cucumber_reports.json'
            }
        }
    }
    post {
    always {
        junit 'reports/*.xml'
	    cucumber failedFeaturesNumber: -1, failedScenariosNumber: -1, failedStepsNumber: -1, fileIncludePattern: 'cucumber_reports.json', pendingStepsNumber: -1, skippedStepsNumber: -1, sortingMethod: 'ALPHABETICAL', undefinedStepsNumber: -1
      } // always
   } // post
}