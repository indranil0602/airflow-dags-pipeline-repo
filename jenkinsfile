node {
    stage('Upload to GCS') { 
        googleStorageUpload bucket: 'gs://jenkins-upload-demo-bucket', credentialsId: 'web-resume-project', pattern: '*.py'
    }
}