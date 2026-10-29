pipeline{
  agent any

  environment{
    IMAGE_NAME = 'pygame'
    TAG = 'v1'
  }
  stages{
    stage('Pull from git hub'){
      steps{
        git branch: 'main', url: 'https://github.com/satejc2425/pygame.git'
      }
    }

    stage('Build docker image'){
      steps{
        script{
          try{
            sh "sudo docker rmi -f ${IMAGE_NAME}:${TAG}"
          }catch (Exception e){
            echo "Image not found with the '${IMAGE_NAME}:${TAG}'"
          }
          sh "sudo docker build -t ${IMAGE_NAME}:${TAG} ."
        }
      }
    }
  }
post{
  success{
     echo 'Python application Docker image built successfully.'
  }
  failure{
    echo 'Docker build failed'
    
  }
}
}
