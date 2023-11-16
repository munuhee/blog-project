# Flask Blog API

This Flask-based API allows you to manage blog posts through CRUD (Create, Read, Update, Delete) operations. It includes endpoints to create, retrieve, update, and delete blog posts.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Database Migration](#database-migration)
- [Testing](#testing)
- [Endpoints](#endpoints)
- [Tools](#tools)
- [Contributing](#contributing)

## Introduction

This Flask application provides an API for creating, fetching, updating, and deleting blog posts. It uses Flask, SQLAlchemy for database interactions, and Flask-Migrate for database migrations.

## Installation

### Virtual Environment Setup (Optional)

To set up a virtual environment and install the necessary packages:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install Flask
pip install flask_sqlalchemy
pip install flask_migrate
```

### Project Structure

- `app/__init__.py`: Initializes the Flask app and configurations.
- `app/models.py`: Contains SQLAlchemy model classes (e.g., `Post` model).
- `app/routes.py`: Includes API routes for managing blog posts.
- `run.py`: Runs the Flask application.

### Usage

To run the Flask application:

```bash
python run.py
```

## Database Migration

To manage database migrations, follow these steps:

1. Initialize the migration environment:
   ```bash
   flask db init
   ```

2. Create an initial migration:
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. Apply the migration to the database:
   ```bash
   flask db upgrade
   ```

### Testing

You can test the API endpoints using tools like Postman. Follow the instructions below to perform CRUD operations on blog posts.

## Endpoints

- **POST** `/posts`: Create a new blog post.
- **GET** `/posts`: Retrieve all blog posts.
- **GET** `/posts/<post_id>`: Retrieve a specific blog post by ID.
- **PUT** `/posts/<post_id>`: Update an existing blog post by ID.
- **DELETE** `/posts/<post_id>`: Delete a blog post by ID.

## Tools

Postman, cURL, or HTTPie can be used to simulate HTTP requests and interact with the API endpoints effectively.

## Contributing

Contributions are welcome! If you want to contribute to this project, feel free to fork this repository, make changes, and create a pull request.
