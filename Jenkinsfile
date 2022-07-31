pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: '*/mrinal-test']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/indranil0602/airflow-dags-pipeline-repo.git']]])
                    sh """
                    git diff --name-only HEAD HEAD~1 > change.txt
                    cat change.txt
                    if [[ \$(cat change.txt | grep \".py\") ]]; then
                        cat change.txt | grep \".py\" > change.txt
                    else
                        echo "No python file changed"
                        exit 1
                    fi
                    cat change.txt
                    """
                    changedFile = readFile('change.txt')
                    print "changedFile: ${changedFile}"
                    // googleStorageUpload bucket: 'gs://jenkins-upload-demo-bucket', credentialsId: 'indranil-json', pattern: '*.txt'
                }
            }
        }
    }
}


