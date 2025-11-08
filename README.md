Automating a Simple Web Application Deployment using AWS, Ansible, Docker, and GitHub Actions 

Overview
This project demonstrates the automation of a Flask web application deployment using modern DevOps tools. Each time new code is pushed to the main branch, GitHub Actions automatically rebuilds the Docker image and redeploys it to an AWS EC2 instance.

Tools Used

AWS CloudFormation – For automated infrastructure provisioning (EC2, networking, security groups).

Ansible – For server configuration and installing Docker.

Docker – For containerizing the Flask app.

GitHub Actions – For CI/CD automation pipeline.

Architecture
The pipeline works in four layers:

Infrastructure (CloudFormation) – Creates and manages the EC2 instance.

Configuration (Ansible) – Installs Docker and prepares the environment.

Containerization (Docker) – Packages the Flask app into a portable image.

Automation (GitHub Actions) – Deploys automatically on every code push.

Deployment Workflow
When you push to GitHub:

The workflow file located at .github/workflows/deploy.yml runs automatically.

It copies project files to the EC2 instance using SCP.

It connects via SSH and rebuilds the Docker container.

The updated Flask app becomes live on port 80.

Verification
You can verify deployment by visiting your EC2 public IP in a web browser:
http://16.16.92.152 

You should see the message:
"Hello everyone — this is my containerized networking app!"

Repository Structure
myapp/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
└── requirements.txt 

Author
Eze Ubachukwu
MSc Information Systems with Computing
Dublin Business School (2025)

redeploy Sat Nov  8 21:28:49 GMT 2025
redeploy Sat Nov  8 21:45:47 GMT 2025
