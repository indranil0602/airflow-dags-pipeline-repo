node {
    stage('git clone') {
        git branch: 'main', credentialsId: 'github-credential', url: 'https://github.com/indranil0602/airflow-dags-pipeline-repo.git'
    }
    stage('Upload to GCS') { 
        googleStorageUpload bucket: 'gs://jenkins-upload-demo-bucket', credentialsId: 'web-resume-project-DAG-upload', pattern: 'DAG/*'
    }
}