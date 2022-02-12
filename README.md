# project-name

## Description

Just a repository to store all my main configurations that can be replicated on other projects

## Requirements
- Python3.8+
- Serverless (`npm install -g serverless`)
  
### Provide your AWS credentials

```bash
# Using serveless to create a default profile
serverless config credentials --provider aws --key AKIAIOSFODNN7EXAMPLE --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# if you multiple profiles on your system
aws configure --profile <your profile name>
# It will ask for the access key and secret key.
# Provide those values and press enter
```

For more alternate ways to provide credentials and using profiles, see [here](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)


## Structure

```
.
├── .docker                         # Required for Development Enviroment Preview
├── src                             # Main application folder
│   ├── configs                     # Folder containing configuration/default variables
│   │   ├── general.py              # Misc configs
│   │   └── sentry.py               # Sentry API key
│   ├── functions                   # Functions holding more complex structures
│   ├── helpers                     # Smaller scope functions
│   │   ├── logger.py               # Logging
│   │   ├── objects.py              # Class Objects
│   │   ├── response.py             # Response object builder
│   │   └── validator.py            # Input parser, validator and normalization
│   ├── schemas                     # JSON Schemas used for validation and response building
│   │   ├── api_params.py           # Schema Object for API inputs used for validation
│   │   ├── aws_payload.py          # Schema Object for AWS event
│   └── services                    # Classes wrapping APIs and modules
│   │   └── sentry.py               # Sentry setup
├── tests                           # Unit Tests
│   ├── __init__.py                 # File used by Pytest to interpret the folder as root for tests
│   ├── helpers.py                  # Helper file holding mock variables used on tests
│   └── test_*                      # Test file relative to its use
├── tests_live                      # Integration Tests
│   └── __init__.py                 # File used by Pytest to interpret the folder as root for tests
├── .gitignore                      # Files to be ignored by git
├── .gitlab-ci.yml                  # CI/CD file configuration of Gitlab (https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html)
├── Dockerfile                      # Container build configuration
├── docker-compose.yaml             # Wrapper of docker builder
├── README.md
├── requirements-lint.txt           # Project requirements list for linting
├── requirements-test.txt           # Project requirements list for testing
├── requirements.txt                # Project requirements list
├── serverless.test.yml             # Serverless functional tests
├── servereless.yml                 # Serverless config (https://www.serverless.com/framework/docs/providers/aws/guide/serverless.yml/)
├── setup.cfg                       # Flake8 configuration
└── sonar-project.properties        # SonarCloud.io configuration
```

## Docker

You can install and use docker by terminal, but it is highly recommended that you use the one of the visual applications available at (https://www.docker.com/get-started)

### Local Container


1. Build the container with `docker build . -t devenv:latest` or `docker-compose up`
2. Run the container with `docker run devenv`
3. OR open Docker app
4. Go to `Volumes` tab and click `Run`
5. Go to `Container/Apps` tab and click on `CLI` button

### Development Environments Preview

1. Open Docker app
2. Go to `Dev Environments Preview` tab
3. Click on `Create new Environment`
4. Follow the wizard
5. By the end, click on `Open on VSCode` (if you have VSCode Installed)

## Pre-Commit
This repository works with Pre-Commit, so we can run some scripts before sending the files to the cloud repository

1. Install Pre-Commit with `pip install pre-commit`
2. Run Pre-commit to run the config automatically: `pre-commit install`
## Setup

### Virtual Env

To create a virtual enviroment folder run `python3 -m venv .venv`
Then start it by running `source .venv/bin/activate`

### Install requirements

1. Copy content from a `example.env` to `.env` file with following variables and copy a values from GitLab
2. Install Python Dependencies: `pip install -r requirements-test.txt` (within your Python environment)
   
## Run locally

To run locally, we are going to use `serverless offline`

1. Install the package (`npm install -g serverless-offline`)
2. Run serverless offline (`sls offline`)
3. [Optional] Check the service on you browser with the default route (http://localhost:3000/dev)

## Run Tests

To check the code coverage, add the parameter `--cov`. eg. `pytest --cov`
### Unit Tests
Run: `pytest tests`

### Live Tests [TODO]

1. Run API locally
2. `pytest live_tests` (requires the server to be running: `python main.py`)


## Formating and Linting

We are using [black](https://black.readthedocs.io/en/stable/editor_integration.html) for formatting. Flake8 for linting (see `.flake8`).
Open for suggestions.

## Contact

In case of issues, reach out to me at https://github.com/lucascantos

## Extra Considerations

- Env Vars should not be protected on Gitlab
- Increasse buffer with `git config --local http.postBuffer 157286400`