# TurboJenkins - Jenkins Pipeline Optimizer (POC)

Day-1 POC: connect to Jenkins, fetch Jenkinsfile and recent builds, ask Gemini (Google Generative AI) for optimization suggestions.

Environment variables:
- `JENKINS_URL`
- `JENKINS_USER`
- `JENKINS_TOKEN`
- `GEMINI_API_KEY` or `GOOGLE_API_KEY`

Quick start:

```bash
cd /Users/wscholl/TurboJenkins
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export JENKINS_URL=...
export JENKINS_USER=...
export JENKINS_TOKEN=...
export GEMINI_API_KEY=...
python -m turbojenkins.cli analyze --job my-pipeline
```
# TurboJenkins Project

## Overview
TurboJenkins is a Jenkins-based project designed to automate the build and deployment processes for applications. It utilizes Groovy scripts to define the pipeline stages and provides a structured approach to managing the application lifecycle.

## Project Structure
```
TurboJenkins
├── jenkins
│   ├── Jenkinsfile          # Pipeline configuration for Jenkins
│   └── pipelines
│       ├── build.groovy     # Build process logic
│       └── deploy.groovy    # Deployment process logic
├── src
│   ├── main.groovy          # Main entry point for the application
│   └── libs
│       └── helpers.groovy   # Utility functions and helper methods
├── scripts
│   └── deploy.sh            # Shell script for automating deployment
├── .vscode
│   └── extensions.json       # Recommended extensions for the project
└── README.md                 # Project documentation
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Ensure you have Jenkins installed and configured.
4. Install the recommended extensions in your development environment.

## Usage Guidelines
- To trigger the build and deployment process, navigate to the Jenkins dashboard and start the pipeline defined in the `Jenkinsfile`.
- Modify the Groovy scripts in the `pipelines` directory to customize the build and deployment logic as needed.
- Use the `helpers.groovy` file to add any utility functions that can be reused across the application.

## Contributing
Contributions are welcome! Please submit a pull request with your changes and a description of the modifications made.
