pipeline {
    agent {
        label 'master'
    }
    parameters {
        string(name: 'GIT_BRANCH',
            description: 'Please input the git branch from which the code should be checkout',
            defaultValue: 'master')
        string(name: 'BROWSER',
            description: 'Enter the desired browser for testing the shopping cart UI Layer',
            defaultValue: 'chrome')
        string(name: 'EMAIL_ID',
            description: 'Enter your email address for shopping cart website')
        password(name: 'PASSWORD',
            description: 'Enter your password for shopping cart website')
    }
    
    stages {
        stage('Git Checkout'){
            steps{
                git branch: '${GIT_BRANCH}', url: 'https://github.com/techsparksguru/python_ci_automation'
            }
        }
        stage('Execute Shopping testcases') {
            steps {
                dir("Class4/shoppingcart_pom"){
                    sh 'pip3 install -r requirements.txt'
                    sh 'behave features -D BROWSER=${BROWSER} -D HEADLESS=True --no-capture --junit'
		            sh 'python3 -m behave2cucumber -i results.json -o cucumber_reports.json'
                }
            }
        }
    }
    post {
    always {
        dir("Class4/shoppingcart_pom"){		
            junit 'reports/*.xml'
	        cucumber failedFeaturesNumber: -1, failedScenariosNumber: -1, failedStepsNumber: -1, fileIncludePattern: 'cucumber_reports.json', pendingStepsNumber: -1, skippedStepsNumber: -1, sortingMethod: 'ALPHABETICAL', undefinedStepsNumber: -1
         }
      } // always
   } // post
}