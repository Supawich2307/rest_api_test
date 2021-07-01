// node {
//     stage("Hello") {
//         sh "echo 'Hello'"   
//     }
//     stage("docker") {
//         sh "docker --version"    
//     }
// }
pipeline {
  agent { Dockerfile true }
  stages {
    stage('Do job stage') {
      steps {
        sh "python --version"
      }
    }
  }
}
