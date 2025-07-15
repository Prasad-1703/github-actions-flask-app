# 🚀 Flask CI/CD with GitHub Actions and Docker

This project demonstrates a complete CI/CD pipeline for deploying a Flask-based web application using **GitHub Actions**, **Docker**, and an **EC2 instance**.

## 📌 Features

- Dockerized Python Flask App
- GitHub Actions Workflow:
  - Builds and pushes Docker image to Docker Hub
  - SSHs into EC2 to pull and run the latest container
- Secure credential management using GitHub Secrets
- Fully automated deployment on every `main` branch push

---

## 🛠️ Tech Stack

- Python 3 / Flask
- Docker
- GitHub Actions
- Docker Hub
- EC2 (Ubuntu)

---

## 📂 Project Structure

```bash
.
├── app.py              # Main Flask application
├── Dockerfile          # Docker build instructions
└── .github
    └── workflows
        └── flask-app.yml  # GitHub Actions workflow file

