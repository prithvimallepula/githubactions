pipeline {
  agent any

  stages {
    stage('Make Request') {
      steps {
        script {
          def response = httpRequest "https://www.pinknoiseplaylisting.com"
          def statusCode = response.status

          echo "Status Code: ${statusCode}"
        }
      }
    }
  }
}
