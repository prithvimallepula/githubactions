pipeline {
  agent any

  stages {
    stage('Check URL Accessibility') {
      steps {
        script {
          urls = [
            "https://www.pinknoiseplaylisting.com",
            "https://pinknoiseplaylisting.com/how-it-works",
            "https://pinknoiseplaylisting.com/for-curators",
            "https://pinknoiseplaylisting.com/contact",
            "https://pinknoiseplaylisting.com/album-art-generator",
            "https://pinknoiseplaylisting.com/track-compatibility/1lRtH4FszTrwwlK5gTSbXO",
            "https://pinknoiseplaylisting.com/next-steps",
            "https://docs.google.com/forms/d/1atqmfm-lxYGnIuMaUpsmdlcczEFV0_1WmQucKxj5KxM/edit?ts=63d81540",
            "https://docs.google.com/forms/u/1/d/1rV8M82qiEv6ZpCkcFW27_ELYE-o5XkG8CZ0d_uAqdx0/edit?usp=forms_home&ths=true",
            "https://pinknoiseplaylisting.com/track-compatibility/1lRtH4FszTrwwlK5gTSbXO"
            // Add more URLs to test
          ]

          for (url in urls) {
            checkURLAccessibility(url)
          }
        }
      }
    }
  }
}

def checkURLAccessibility(url) {
  try {
    def response = httpRequest(url: url, httpMode: 'HEAD')
    def statusCode = response.status

    echo "07/09 - This code is being read from Git. Also, ${url} is accessible (Status Code: ${statusCode})"
  } catch (Exception e) {
    echo "${url} FAILED"
  }
}
