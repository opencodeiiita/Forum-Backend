# Forum(BACKEND)

Forum is a discussion forum designed for the students of IIITA to ask questions, share their experiences and to know what their peeps are up to.

This repository holds the backend of the project. The backend is being built in **Django-REST framework** with **Python** as the driver language.

The backend will consist of creating **Application Programming Interfaces (APIs)** and **Database Models (SQL)** for the app. These will be used directly by the frontend team.

## Requirements

- Python v3.7 or higher
- Pip (latest version is recommended)
- Django v4.1.4 or higher
- Django REST framework v3.14.0 or higher


These are the main packages required. Some other packages are specified in the `requirements.txt` file. However, they are automatically installed while installing the above packages.

## Setup on local machine

To set-up the development environment on your local machine, follow the below steps:

1. Fork the repository to your github account.
2. Clone the forked repository to your local machine.
3. Download and install Python from [here](https://www.python.org/downloads/).
   _Downloading python is mandatory for windows users. On macOS you may have python 2.x pre-installed, consider installing python 3.7 or higher. This step is generally not required for most linux users since most linux distros come with pre-installed python (typically 3.7 or higher)._

**Make sure you add python to your system path if it's not already added**

### Windows

- Open command prompt and navigate to the directory where you want to create a virtual environment (preferably the parent directory of the one in which the cloned project resides).
- Create a virtual environment: `python -m venv env`. Here, `env` can be replaced by any name of your choice.
- Activate the virtual environment: `env\Scripts\activate.bat`.
- Navigate into the project directory where you have the `manage.py` file
- Now run the server: `python manage.py runserver`.
- Open a browser and go to: `https://localhost:8000/`. You should see a working django app showing that "the install worked successfully."

### Linux/macOS

- Open the terminal and follow the same steps as in the above **Windows** section with a few changes described below.
- Instead of using `python` in commands, use `python3`.
- To activate the virtual environment: `source env/bin/activate`.
- Other steps are same as in Windows.

---
### Running Migrations 

- Run the command:  `python manage.py makemigrations`.
- Run the command:  `python manage.py makemigrations <app name>` when you want to create migrations for a particular app.
- Run the command:  `python manage.py migrate` to apply migrations and create database tables.
- Linux/macOS users,instead of using `python` in commands, use `python3`.

### Creating a Super User for Admin Site

- Create a user by running command:  `python manage.py createsuperuser`.
- Enter desired username and email-address after that.
- Enter a password for the the admin site.
  To access the admin site, run the server, open a browser, and go to: `https://localhost:8000/admin/` and enter your username and password there.


Once django is installed successfully and working, it's time to install the **django-REST framework**. This is the key tool for building the APIs. So, open the terminal (cmd on windows) and activate the virtual environment. Now install the REST framework with the following command: `pip install djangorestframework`

Now you have the required tools to start contributing! Enjoy! :)

---

**For testing purposes, consider using tools like httpie (command-line tool) or Postman.** This is because browsable API interface doesn't allow passing a token under the authentication header.
