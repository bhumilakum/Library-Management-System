# Library Management System

This the demo project of the library management system.  Here the user can list, search, lend, submit books. Book search can be filtered by author name, book title, ISBN and availability of the book. Librarian can manage books with various user requests for book lend and returning book.

## Table of contents

* [Download and setup project](#download-and-setup-project)
* [How to run project](#how-to-run-project)

## Download and setup project

* Clone this repository to your system.
* Create virtual environment.
* There are Python and Django should be installed.
* Also install some dependencies like,
    ```cmd
        pip install pillow
    ```
* To use Google Signin into this application, paste your Client ID and Client Secret into ```settings.py``` file. To grab that, follow the instructions mentioned in this page ( [https://developers.google.com/identity/protocols/OAuth2WebServer](https://developers.google.com/identity/protocols/OAuth2WebServer)).

## How to run project

* First migrate database.
    ```cmd
        python manage.py makemigrations
        python manage.py migrate
    ```
* Run application.
    ```cmd
        python manage.py runserver
    ```
* Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000)