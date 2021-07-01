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
  stage('Hello') {
      steps {
        sh "echo 'HELLO'"
      }
  stages {
    stage('Do job stage') {
      steps {
        sh "python --version"
      }
    }
  }
}
