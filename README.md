# FastAPI MySQL Project

## Description

This project is an example of an API application built using FastAPI and MySQL. The application demonstrates basic CRUD operations with a MySQL database using SQLAlchemy ORM.

## Requirements

- Python 3.12
- MySQL (in this case, running in a Docker container)

## Installation

1. **Clone the repository:**
   First, clone the repository from GitHub:
   git clone https://github.com/kubszy/fastapi_mysql_project.git
2. **Navigate to the project folder:**
   cd fastapi_mysql_project
3. **Create a virtual environment:**
   source venv/bin/activate
4. **Install the dependencies**
   pip install -r requirements.txt
5. **Run MySQL in a Docker container**
    docker run --name mysql-server -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=fastapi_mysql_project -p 3306:3306 -d mysql:8.0
6. **Run the FastAPI application**
   uvicorn main:app --reload