# FAQ Management API - Django Backend

## Overview

This is a Django REST API for managing Frequently Asked Questions (FAQs) with multi-language translation and WYSIWYG editor support.  
- Uses Google Translate API for automatic translations.  
- Implements django-ckeditor for formatted answers.  
- Caching is handled using Redis for improved performance.  
- Fully tested with unit tests and follows PEP8 conventions.  

## Features

- REST API to manage FAQs  
- Multi-language support (English, Hindi, Bengali)  
- Query FAQs by language using `?lang=hi`, `?lang=bn`, etc.  
- WYSIWYG editor (`django-ckeditor`) for formatting answers  
- Redis caching for translations  
- Unit tests and PEP8 compliance  
- Docker support (`Dockerfile` and `docker-compose.yml`)  

## Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/<your-username>/faqs-backend.git
cd faqs-backend
Create a Virtual Environment

python -m venv venv
Activate the virtual environment:

Windows

venv\Scripts\activate
macOS/Linux

source venv/bin/activate
Install Dependencies

pip install -r requirements.txt
Apply Migrations

python manage.py makemigrations
python manage.py migrate
Run the Server

python manage.py runserver
The API will be available at:


http://127.0.0.1:8000/api/faqs/
API Endpoints
Fetch All FAQs (Default: English)

curl http://127.0.0.1:8000/api/faqs/
Fetch FAQs in Hindi

curl http://127.0.0.1:8000/api/faqs/?lang=hi
Fetch FAQs in Bengali

curl http://127.0.0.1:8000/api/faqs/?lang=bn
Running Tests
To run unit tests, execute:


python manage.py test
Linting and Code Quality
To check for PEP8 compliance:

flake8
