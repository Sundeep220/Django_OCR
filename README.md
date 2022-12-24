# Django_OCR
- A small app that will allow the users to login and upload PDF and image documents. The server will generate text from the image/document using OCR or Optical Character Recognition.

This Django web app uses pytesseract(https://pypi.org/project/pytesseract/) for OCR.

Note: This app requires you to install https://github.com/tesseract-ocr/tesseract to be able to use the OCR. Also, this app is a MVP.

## Features

- User authentication and login
- Handles both PDF and image files 
- Copy and generate text from images or PDF docs using OCR
- Ability to download the original upload files

## Installation

This app uses PostgreSQL for DBMS. Download it from - https://github.com/tesseract-ocr/tesseract

Make sure you download and install tesseract(https://github.com/tesseract-ocr/tesseract) for OCR.
## Run Locally

Clone the project

```bash
  git clone: https://github.com/Sundeep220/Django_OCR
```
- Before running this project: 

  -> Create a virtual environment, in Windows command is as follows: \
    `pythom -m venv env` \
   -> To activate: \
     `env/Scripts/activate`

- To run this project do the following:

    Pre-requisites: Python, pip and django should be installed in your system. All the coding is done using VScode.
    1. To install the dependencies: \
       `pip install -r requirements.txt` 
    2. Make the migrations:\
        `python manage.py makemigrations` 
    3. Migrate the tables: \
        `python manage.py migrate` 
    4. Create a superuser for your project: \
        `python manage.py createsuperuser`   
        This will prompt you to enter username, email and password for the superuser.  
    5. Run the server using: \
        `python manage.py runserver`


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file in the root folder

`SECRET_KEY`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`

`DB_PORT`
