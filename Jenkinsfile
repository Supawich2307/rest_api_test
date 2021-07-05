node{
   //  stage("SCM") {
   //      git branch: "master", url: "https://github.com/codebangkok/jenkins"
   //  }
    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
        sh "echo ${env.PATH}"
    }
    stage("Build") {
      sh "pwd"
      sh "docker build ."
    }
   //  stage("Push") {
   //      sh """
   //      docker login -u "supakew" -p "Su11pa11kew11"
   //      docker image push suapkew/test_rest
   //      """
   //  }
}
