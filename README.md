## Contelizer Task
This project is a simple Django application that includes two functionalities:

Text Processing: A feature that allows users to upload a text file and then processes the content by scrambling the letters in each word, except for the first and last letter.

PESEL Validator: A feature that allows users to input a PESEL number (Polish ID number) and validates it, displaying whether the PESEL is correct and providing additional details such as birth date and gender.

Features
Text Processor: Allows users to upload a text file, processes the content, and displays the modified version with scrambled letters.

PESEL Validator: Users can input a PESEL number, and the application will validate it and show information about the PESEL (validity, birth date, and gender).

Prerequisites
Before running the application, you need to have the following installed:

Docker (for containerization)

Make (for managing build automation)

Alternatively, you can run the application without Docker by setting up a virtual environment and installing the necessary dependencies manually.

# Project Architecure

```
CONTELIZER_TA/                 
│
├── container/                  
│   ├── __init__.py             
│   ├── models.py               
│   ├── views.py               
│   ├── urls.py                
│   └── tests.py               
│
├── media/                    
│   └── ...                   
│
├── pesel_validation/         
│   ├── __init__.py
│   ├── validator.py           
│   └── tests.py
│
├── templates/                  
│   ├── base.html             
│   └── ...                   
│
├── text_processor/           
│   ├── __init__.py
│   ├── processor.py           
│   └── tests.py
│
├── db.sqlite3                 
│
├── manage.py                 
│
├── .gitignore                
│
├── Dockerfile                 
│
├── Makefile                  
│
└── requirements.txt           
```

# Installation
1. Using Docker
To run the application using Docker, follow these steps:

Build the Docker Image:

From the project root directory, build the Docker image with the following command:

```
make docker-build
```
Run the Docker Container:

Once the image is built, run the container with this command:

```
make docker-run
```
The application will be available at http://127.0.0.1:8000.

2. Without Docker (Using Virtual Environment)
If you prefer to run the application locally without Docker, follow these steps:

## Create a Virtual Environment:

```
python3 -m venv venv
```
# Activate the Virtual Environment:

On Linux/macOS:

```
source venv/bin/activate
```
On Windows:

```
venv\Scripts\activate
```
# Install Dependencies:

Install the required Python packages using requirements.txt:

```
pip install -r requirements.txt
```
# Run Migrations:

Run database migrations to set up the SQLite database:

```
python manage.py migrate
```
# Start the Django Development Server:

Run the Django development server:

```
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000.


## Usage
# Main Page:

The main page at http://127.0.0.1:8000 offers two options:

Text Processing: Upload a .txt file and get a processed version of the file with scrambled letters.

PESEL Validation: Input a PESEL number to validate and display related information like birth date and gender.

# Text Processing:

Click on "Text Processing".

Upload a .txt file.

The processed text will be shown with scrambled letters in the body of the file, while the first and last letter of each word remain unchanged.

# PESEL Validation:

Click on "PESEL Validation".

Input a valid PESEL number (11 digits).

The application will display whether the PESEL number is valid, the birth date, and gender.

## Makefile Commands: 
```
make install
```
Create a virtual environment and install dependencies.
```
make docker-build
```
Build the Docker image for the project.
```
make docker-run
```
Run the project using Docker, mapping port 8000.
```
make server
```
Run the Django development server locally (useful for testing or development).
```
make migrate
```
Run Django migrations to set up the database.
```
make clean
```
Remove the virtual environment.
