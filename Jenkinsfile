pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: '*/mrinal-test']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/indranil0602/airflow-dags-pipeline-repo.git']]])
                    googleStorageUpload bucket: 'gs://jenkins-upload-demo-bucket', credentialsId: 'indranil-json', pattern: 'pythons/*'
                    sh'''
                        rm -rfv pythons/*
                        git config --global user.email "githubbot@gmail.com"
                        git config --global user.name "GithubBot"
                        git add .
                        git commit -m "removing files"
                    '''
                    withCredentials([usernamePassword(credentialsId: 'GITHUB', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                        sh('git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/indranil0602/airflow-dags-pipeline-repo.git HEAD:mrinal-test')
                    }
                }
            }
        }
    }
}


