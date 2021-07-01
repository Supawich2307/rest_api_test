// node {
//     stage("Hello") {
//         sh "echo 'Hello'"   
//     }
//     stage("docker") {
//         sh "docker --version"    
//     }
// }
pipeline {
  agent { dockerfile true }
  stages {
    stage('Hello') {
      steps {
        sh "echo 'HELLO'"
      }
    }
    stage('Do job stage') {
      steps {
        sh "python --version"
      }
    }
  }
}
