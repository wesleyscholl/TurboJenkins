pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Compile the code
                    sh 'groovyc -d out src/main.groovy'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'groovy -cp out src/main.groovy'
                }
            }
        }
    }

    post {
        success {
            echo 'Build and tests completed successfully.'
        }
        failure {
            echo 'Build or tests failed.'
        }
    }
}