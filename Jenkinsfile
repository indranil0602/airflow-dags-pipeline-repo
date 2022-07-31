node {
    stage('Upload to GCS') { 
        sh """
            env > test.txt
        """
        googleStorageUpload bucket: 'gs://jenkins-upload-demo-bucket', credentialsId: 'indranil-json', pattern: '*.txt'
    }
}