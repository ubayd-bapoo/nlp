# Deel Technical Test
# Setting Up and Running an Application with Docker Python using FastAPI

This README file provides step-by-step instructions on how to set up and run the Python application
 using both Docker and a normal Python environment. This guide assumes you have Docker installed on your system,
  a basic understanding of Python.

## Table of Contents
- [Clone the Repository](#1-clone-the-repository)
- [Setting Up the Python Application](#2-setting-up-the-python-application)
- [Running the Python Application Locally](#3-running-the-python-application-locally)
- [Building the Docker Image](#4-building-the-docker-image)
- [Running the Dockerized Application](#5-running-the-dockerized-application)
- [API Documentation](#6-api-documentation)
- [Unit Test](#7-unit-test)
- [Task 3](#Task-3)

### 1. Clone the Repository
Clone the repository containing the Python application to your local machine using Git 
or by downloading the ZIP file from the source code on GitHub.
```bash
git clone git@github.com:ubayd-bapoo/nlp.git
cd nlp
```

### 2. Setting Up the Python Application
Lets make sure the Python application works correctly in a normal Python environment. 
This typically involves creating a virtual environment, installing dependencies, and 
testing the application.

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install application dependencies
pip install -r requirements.txt

# Test the application
uvicorn  service:app --host 0.0.0.0 --port 8000
```

### 3. Running the Python Application Locally
To run the application in your local Python environment, you can use the following command:
```bash
uvicorn  service:app --host 0.0.0.0 --port 8000  # In the service_app folder
```

### 4. Building the Docker Image
The Dockerfile sets up a basic Python environment and copies the application files into 
the container. It also installs all necessary dependencies from requirements.txt and 
specifies the command to run when the container starts.
To build a Docker image of the Python application, navigate to the project directory 
(where the Dockerfile is located) and run the following command:
```
docker build -t nlp .
```

### 5. Running the Dockerized Application
Once the Docker image is built successfully, you can run the Python application within 
a Docker container:
```bash
docker run -p 8000:8000 nlp
```

### 6. API Documentation
The API documentation is powered by FastAPI's built-in Swagger integration. This interactive documentation makes it 
easy to explore and understand the API endpoints.
- **Access API Documentation**: To explore our API documentation and test the endpoints 
interactively, simply visit [Swagger UI](http://localhost:8000/docs) (http://localhost:8000/docs) when the application
 is running locally.

- **Automatic Documentation**: We've designed our API using FastAPI, which automatically
 generates documentation based on the code, including request and response models and 
 descriptions.

FastAPI's Swagger UI provides a user-friendly way to understand and use our API. You can
 interact with the available endpoints, view request and response models, and even make
  test requests right from the documentation.

Feel free to dive into the documentation to get a better understanding of how to use our
 API effectively.

![FastAPI Swagger UI](https://fastapi.tiangolo.com/img/tutorial/tutorial-02-swagger-ui.png)

Note: In a production environment, replace `http://localhost:8000/docs` with the actual
 URL where your API is hosted.

### 7. Unit Test
To run the unit tests for this application, follow these steps:
```bash
   pytest -v -s test_service.py
```
#### Automated Testing with GitHub Actions

I have set up a GitHub Actions workflow that automatically runs pytest for our unit tests
 whenever changes are pushed to the repository's `main` branch. This ensures that our code
  is continuously tested for correctness.

The workflow configuration can be found in the [`.github/workflows/unit_tests.yml`](.github/workflows/unit_tests.yml) file. Here's how it works:

- Whenever you push changes to the `main` branch, GitHub Actions will automatically 
trigger the workflow.
- The workflow will use the `pytest` command to execute the tests defined in the 
`test_service.py` file.
- The results of the tests will be displayed in the GitHub Actions logs.

You can always check the status of the tests by visiting the "Actions" tab in this 
repository. If there are any issues with the tests, you will be notified.

By leveraging GitHub Actions, we ensure that our codebase remains reliable and that new
 contributions are thoroughly tested before being merged into the main branch.

# Task 3
## Given additional resources, suggest, how you might take this proof of concept to production. Include any changes or improvements you might make.

* Performance Optimization:
    - Review and optimize code for performance bottlenecks.
    - Implement caching mechanisms for frequently accessed data.
* Database Management:
    - Choose a production-grade database system.
    - Implement database migrations and version control.
* Asynchronous Processing:
    - Use async programming for I/O-bound operations.
    - Consider task queues for background processing.
* Logging and Monitoring:
    - Implement comprehensive logging and set up monitoring tools.
    - Monitor system health and implement alerts.
* Security Enhancements:
    - Implement input validation and authentication mechanisms.
     -Use HTTPS for secure communication and regular dependency updates.
* Deployment and Scalability:
    - Containerize the application using Docker.
    - Use container orchestration platforms like Kubernetes.
    - Implement autoscaling policies.
* CI/CD Pipeline:
    - Set up a CI/CD pipeline for automated testing and deployment.
    - Automate deployment workflows and implement rollback mechanisms.
* Documentation and Testing:
    - Maintain comprehensive documentation and implement unit tests.
    - Use frameworks like pytest for testing and enforce coding standards.
* Backup and Disaster Recovery:
    - Implement regular backups and disaster recovery plans.
* Compliance and Regulations:
    - Ensure compliance with relevant regulations and standards.
    - Implement features for data privacy and audit logging.

By implementing these changes and improvements, you can enhance the reliability, scalability, security, and 
maintainability of your FastAPI application as you transition from a proof of concept to a production-ready system.

