Task Management API
Project Overview
The Task Management API is a backend application built with Django and Django REST Framework (DRF) to provide task management functionalities. Users can create, update, delete, and manage their tasks, complete with user authentication to ensure task ownership and privacy.

The API adheres to RESTful principles, supports advanced features like filtering, sorting, and task categories, and is designed for deployment in a production environment.

Features
Core Features:
Task Management (CRUD):
Users can create, read, update, and delete tasks with attributes like title, description, due date, priority, and status.
User Authentication:
Built-in authentication ensures users can only access and manage their own tasks.
Mark as Complete/Incomplete:
Tasks can be marked as complete or incomplete, with timestamps for status changes.
Filters and Sorting:
Tasks can be filtered by status, priority, and due date and sorted by priority or due date.
Additional Features:
Task Categories:
Tasks can be grouped into categories such as "Work," "Personal," or "Other."
Recurring Tasks:
Option to set tasks to repeat on a daily, weekly, or custom schedule.
Task History:
Tracks changes in task statuses over time for better task management.
Technologies Used
Backend Framework: Django, Django REST Framework (DRF)
Database: SQLite (default for development), can be switched to PostgreSQL for production
Authentication: Django's built-in authentication, with optional JWT for token-based security
Deployment: Ready for deployment on platforms like Heroku or PythonAnywhere
Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.8+
Pip (Python package installer)
Virtualenv (recommended for environment isolation)
Installation Steps
Clone the repository:

bash
Copy code
git clone <repository-url>
cd task-management-api
Set up a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate     # For Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations to set up the database:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
API Endpoints
Authentication
POST /api/auth/login/ - User login
POST /api/auth/register/ - User registration
Task Management
GET /api/tasks/ - List all tasks (with filters and sorting)
POST /api/tasks/ - Create a new task
GET /api/tasks/<id>/ - Retrieve a specific task
PUT /api/tasks/<id>/ - Update a task
DELETE /api/tasks/<id>/ - Delete a task
Task Actions
PATCH /api/tasks/<id>/complete/ - Mark a task as complete
PATCH /api/tasks/<id>/incomplete/ - Revert a task to incomplete
Deployment
To deploy this API:

Set up a PostgreSQL database and update the DATABASES setting in settings.py.
Install gunicorn and configure it as the WSGI server.
Deploy the project to Heroku or PythonAnywhere.
Challenges and Learnings
Throughout this project, challenges such as setting up complex validations, ensuring proper authentication, and designing efficient database relationships were overcome. This experience reinforced the importance of clean code, thorough testing, and user-focused design.

Contributions
Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request.



