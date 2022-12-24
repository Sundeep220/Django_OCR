# Django_OCR
- A small app that will allow the users to login and upload PDF and image documents. The server will generate text from the image/document by OCR or Optical Character Recognition using Tesseract.

## APP DEMO

https://drive.google.com/file/d/1h9u3k_ubcC5y34Go23hr7nAqr0tTCpcV/view?usp=sharing

##

This Django web app uses pytesseract(https://pypi.org/project/pytesseract/) for OCR.

Note: This app requires you to install https://github.com/tesseract-ocr/tesseract in your Operating System to be able to use the OCR.

## Features

- User authentication and login
- Handles both PDF and image files 
- Copy and generate text from images or PDF docs using OCR
- Ability to download the original upload files

## Installation

This app uses PostgreSQL for DBMS. Download it from - https://www.postgresql.org/download/

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
    2. Before Applying the below steps make sure you have integerated postgres in you application.
         Make the migrations:\
            `python manage.py makemigrations` 
         Migrate the tables: \
            `python manage.py migrate` 
    3. Create a superuser for your project: \
        `python manage.py createsuperuser`   
        This will prompt you to enter username, email and password for the superuser.  
    4. Run the server using: \
        `python manage.py runserver`


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file in the root folder

`SECRET_KEY`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`

`DB_PORT`


##App view: 

- Home Page: 


![dashboard](https://user-images.githubusercontent.com/93663329/209426494-4e962a8f-7417-4b26-ba35-35fa979b2234.png)


- Uploaded doc page:


![files](https://user-images.githubusercontent.com/93663329/209426517-452a06a9-0a85-478f-a475-bae38a2dc259.png)


- Extracted text page:


![details](https://user-images.githubusercontent.com/93663329/209426527-d77f4673-dd52-4030-ba68-86e9e9e492ea.png)


- Login Page:


![login1](https://user-images.githubusercontent.com/93663329/209426536-90078580-6796-4118-81e0-320fcd91fcfb.png)


- Register Page:


![registetr2](https://user-images.githubusercontent.com/93663329/209426546-04d810e9-ab21-46a0-8c2f-dcfcb6892ec3.png)






