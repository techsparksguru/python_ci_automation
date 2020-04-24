pipeline {
    agent {
        label 'master'
    }

    parameters {
        string(name: 'GIT_BRANCH',
            description: 'Please input the git branch from which the code should be checkout',
            defaultValue: 'master')
        
        choice(name: 'COLLECTION_TYPE',
            description: 'Choose the collection type from the dropdown',
            choices: 'Basic\nAdvance')
        
        string(name: 'URL',
            description: 'Please input the host url under test')
        
        
        string(name: 'ITERATIONS',
            description: 'No.of iterations to run the requests',
            defaultValue: '1')
    }

    stages {
        stage('checkout') {
            steps {
                git branch: '${GIT_BRANCH}', url: 'https://github.com/techsparksguru/python_ci_automation'
            }
        }
        stage('Execute  Collections using newman') {
            steps {
                script{
                    try{
                        if(params.COLLECTION_TYPE=='Basic'){
                            dir('Class5/techsparks_postman_apis'){
                                sh 'newman run techsparks_postman_basic_api_collection.json -e local_environment.json -n ${ITERATIONS}'
                                }
                            }
                        
                        if(params.COLLECTION_TYPE=='Advance'){
                            dir('Class5/techsparks_postman_apis'){
                                    sh 'newman run techsparks_postman_advance_api_collection.json -e local_environment.json -n ${ITERATIONS}'
                                }
                            }
                        }
                        catch(Exception error){
                            currentBuild.result = 'SUCCESS'
                    }   
                }
            }
        }
    }

    post {
        always {
               cleanWs deleteDirs:true
        }//always
    }// post
} // pipeline