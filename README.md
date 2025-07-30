# Azure DevOps CI/CD Demo - Flask Application

A demonstration project showcasing Azure DevOps capabilities including continuous integration, automated testing, and artifact management using a Flask web application.

## Overview

This project demonstrates the implementation of DevOps practices using Microsoft Azure DevOps services. It features a Flask web application with automated CI/CD pipelines, unit testing, and Python package distribution through Azure Artifacts.

## Architecture

The project utilizes a self-hosted Windows agent to execute pipeline operations, providing hands-on experience with Azure DevOps infrastructure management.

## Technology Stack

- **Backend**: Python Flask
- **Testing**: Python unittest framework
- **CI/CD**: Azure DevOps Pipelines
- **Package Management**: Azure Artifacts
- **Agent**: Self-hosted Windows machine

## Project Structure

```
DevOps-Demo-WebApp/
├── app.py                   # Flask application entry point
├── requirements.txt         # Python dependencies
├── tests/
│   └── test_app.py         # Unit tests
├── azure-pipelines.yml     # CI/CD pipeline configuration
├── setup.py                # Python package setup
└── dist/                   # Build artifacts (excluded from version control)
```

## Azure DevOps Services Integration

### Azure Repos
- Source code version control
- Branch management and collaboration

### Azure Pipelines
- Automated continuous integration
- Dependency installation and testing
- Package building and distribution

### Azure Test Plans
- Manual test case management
- Test execution tracking

### Azure Artifacts
- Python package hosting
- Secure artifact distribution

## Test Cases

The project includes comprehensive test coverage:

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC001 | Verify root endpoint accessibility | HTTP 200 status code |
| TC002 | Validate response content | Contains "Hello from Azure DevOps" |

## Pipeline Workflow

The automated CI/CD pipeline performs the following operations:

1. **Source Code Checkout**: Retrieves latest code from repository
2. **Dependency Installation**: Installs required Python packages
3. **Unit Test Execution**: Runs automated test suite
4. **Package Building**: Creates distributable Python packages
5. **Artifact Publishing**: Uploads packages to Azure Artifacts feed

## Manual Package Build and Upload

For manual package management:

```bash
# Install required tools
pip install setuptools wheel twine

# Build package
python setup.py sdist bdist_wheel

# Upload to Azure Artifacts
twine upload --repository-url https://pkgs.dev.azure.com/<ORG>/<PROJECT>/_packaging/<FEED>/pypi/upload/ dist/*
```

## Configuration Requirements

### Pipeline Variables
- `TWINE_PAT`: Personal Access Token for Azure Artifacts authentication

### Self-Hosted Agent Setup
1. Register agent with Azure DevOps organization
2. Approve agent in Azure DevOps portal
3. Ensure agent service is running and online

## Repository

**GitHub**: [https://github.com/getAzeem/Azure-devops-project01](https://github.com/getAzeem/Azure-devops-project01)

## Prerequisites

- Python 3.x
- Azure DevOps organization access
- Self-hosted agent configuration
- Azure Artifacts feed setup

## Getting Started

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Execute tests: `python -m unittest discover tests`

## Contributing

This project serves as a learning resource for Azure DevOps implementation. Contributions that enhance the demonstration of DevOps practices are welcome.

## License

This project is created for educational and demonstration purposes.
