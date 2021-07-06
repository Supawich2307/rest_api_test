node{
    stage("SCM") {
        git branch: "main", url: "https://github.com/Supawich2307/rest_api_test.git"
    }
    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
        sh "echo ${env.PATH}"
    }
    stage("Kill Docker") {
      def older_num = "${env.BUILD_NUMBER-1}"
      sh "echo 'older_num'"
      sh "docker kill supakew/test_api:${older_num}"
    }
    stage("Build") {
      sh "docker build -t supakew/test_api:${env.BUILD_NUMBER} ."
    }
    stage("Run") {
        sh "docker run -d -p 5200:5200 --name test_rest supakew/test_api:${env.BUILD_NUMBER}"
    }
}
