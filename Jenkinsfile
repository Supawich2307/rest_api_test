node{
   stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
        sh "echo ${env.PATH}"
    }
    stage("SCM") {
        git branch: "main", url: "https://github.com/Supawich2307/rest_api_test.git"
    }
    stage("Build") {
      sh "pwd"
      sh "docker image build -t test_1 https://github.com/Supawich2307/rest_api_test/blob/main/Dockerfile"
    }
   //  stage("Push") {
   //      sh """
   //      docker login -u "supakew" -p "Su11pa11kew11"
   //      docker image push suapkew/test_rest
   //      """
   //  }
}
