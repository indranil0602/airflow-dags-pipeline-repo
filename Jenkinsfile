pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                git diff --name-only HEAD HEAD~1 > change.txt
                cat change.txt
                googleStorageUpload bucket: 'gs://jenkins-upload-demo-bucket', credentialsId: 'indranil-json', pattern: '*.txt'
            }
        }
    }
}
