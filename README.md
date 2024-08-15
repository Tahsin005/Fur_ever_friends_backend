
# Fur Ever Friends Backend API


Welcome to the backend repository of Fur Ever Friends, your trusted online pet adoption platform built with Django Rest Framework. This repository contains the codebase for the RESTful API that powers the backend functionality of the Fur Ever Friends platform.
## Features

- **User Authentication:** Secure user authentication using Django's token-based authentication for accessing API endpoints.
- **Pet Listings:** Create, read operations for managing pet listings. Users can create, read, and update their product listings, but they cannot delete the products they have listed.
- **Adoption Management:** Endpoint for creating and managing adoption requests for pets.
- **Reviews:** API endpoint for users to leave reviews for adopted pets.
- **Filtering:** Implement filtering functionality for pet listings.

## Getting Started

1. Clone Repository: Clone this repository to your local machine using git clone https://github.com/Tahsin005/Fur_ever_friends_backend

2. Install Dependencies: Navigate to the project directory and install the required dependencies using pip install -r requirements.txt.

3. Database Setup: Configure your database settings in the settings.py file. By default, the project is configured to use PostgreSQL, but you can change it to use SQLite or MySQL as per your preference.

4. Migrations: Run database migrations to create the necessary database schema using python manage.py migrate.

5. Create Superuser: Create a superuser account to access the Django admin panel and manage users and product listings using python manage.py createsuperuser.

6. Run Server: Start the Django development server using python manage.py runserver.

7. Explore API Endpoints: Explore the available API endpoints by navigating to http://127.0.0.1:8000/ in your web browser or API client.
## Technology used



**Backend:** Django REST API, PostgreSQL



## Live Link

[Live Link](https://fur-ever-friends-chi.vercel.app/)


