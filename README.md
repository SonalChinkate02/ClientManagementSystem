# Client Management System

This is a Client Management System built using Django and Django REST Framework. It allows users to manage clients and projects, assign users to projects, and track project details.

## Features
- **Client Management**: Add, view, update, and delete clients.
- **Project Management**: Create, view, update, and delete projects.
- **User Assignment**: Assign users to projects for collaboration.
- **API Integration**: The system exposes REST APIs for managing clients and projects.

## Technologies Used
- **Django**: Web framework for building the application.
- **Django REST Framework**: For creating REST APIs.
- **MySQL**: Database for storing client and project information.
- **Git**: Version control for managing the codebase.

## Requirements
- Python 3.x
- MySQL
- Django 5.x
- Django REST Framework

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using the following command:

git clone https://github.com/SonalChinkate02/ClientManagementSystem.git


2. Install Dependencies
Navigate to the project directory and install the required Python packages using pip:

cd ClientManagementSystem

pip install -r requirements.txt


3. Set Up the Database
Make sure you have MySQL installed and running. Create a new database for the project.

For example, create a new database named mydatabase:

CREATE DATABASE mydatabase;


4. Configure Database Settings
Update the DATABASES section in the settings.py file to match your MySQL setup.


5. Run Migrations
Run the Django migrations to create the necessary tables in the database:


python manage.py migrate


6. Create a Superuser
Create an admin user so you can access the Django admin panel:


python manage.py createsuperuser
Follow the prompts to create the superuser.


7. Start the Development Server
Run the Django development server:

python manage.py runserver


8. Access the Application
The application will be running at http://localhost:8000.
You can access the Django admin panel at http://localhost:8000/admin using the superuser credentials you created.



10. Access the API Endpoints
The API for clients and projects is accessible at the following endpoints:

## Clients:
- GET /api/clients/ - List all clients
- POST /api/clients/ - Create a new client
- PUT /api/clients/{id}/ - Update an existing client
- DELETE /api/clients/{id}/ - Delete a client
  
## Projects:
- GET /api/projects/ - List all projects
- POST /api/projects/ - Create a new project
- PUT /api/projects/{id}/ - Update an existing project
- DELETE /api/projects/{id}/ - Delete a project

  
GitHub Repository
You can find the source code on GitHub: https://github.com/SonalChinkate02/ClientManagementSystem
