node {
    stage('Upload to GCS') { 
        checkout([$class: 'GitSCM', branches: [[name: '*/main/DAG']], extensions: [], userRemoteConfigs: [[url: 'ssh://git@bitbucket.org:company/repo.git']]])
        googleStorageUpload bucket: 'gs://jenkins-upload-demo-bucket', credentialsId: 'web-resume-project-DAG-upload', pattern: 'DAG/*'
    }
}