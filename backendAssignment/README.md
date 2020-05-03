# FullThrotle_Assignment

This is a design and implementation of a Django application with User and ActivityPeriod models through
a custom management command to populate the database with some dummy data, and designing
an API to serve that data in the json format.

# Development Setup

## Windows 64 bit

1. Install these tools
    * [Python v3.6.2 64 bit](https://www.python.org/downloads/)
    * [Git](https://git-scm.com/download/win)


1. Upgrade pip

    ```bash
    python -m pip install --upgrade pip
    ```

1. Setup virtualenv

    ```bash
    python -m venv venv
    venv\ Scripts\ activate.bat
    ```


1. Download backendApp repository

    ```bash
    https://github.com/Gopinathpanda/FullThrotle_Assignment.git
    ```

1. Install project dependencies

    ```bash
    Go to requirements.txt folder and run command
    pip install -r requirements.txt
    ```
1. To store Data in DataBase

     ```bash
    python manage.py populate_users users
    ```
1. To check Json format Through API

    ```bash
    python manage.py runserver
    go to /backendApp/users
    ```

