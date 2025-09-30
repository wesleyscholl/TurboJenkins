#!/bin/bash

# This script automates the deployment process for the TurboJenkins project.

# Navigate to the project directory
cd "$(dirname "$0")/../.."

# Execute the deployment script defined in the Jenkins pipeline
jenkins/pipelines/deploy.groovy

# Check if the deployment was successful
if [ $? -eq 0 ]; then
  echo "Deployment successful!"
else
  echo "Deployment failed!"
  exit 1
fi