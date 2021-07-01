// node {
//     stage("Hello") {
//         sh "echo 'Hello'"   
//     }
//     stage("docker") {
//         sh "docker --version"    
//     }
// }
pipeline {
  agent {
    docker {
      image 'python:3.7.3'
    }
  }
  stages {
    stage('Do job stage') {
      steps {
        sh "python --version"
      }
    }
  }
}
