# Banking App

## Prerequisites
1. A Terminal (preferred) or a CMD
2. Python 3.4 or above installed.

## Installation
1. Open a Terminal, and clone the current repository.
    ```
    git clone https://github.com/BobadeKenny/BankApp.git
    ```
2. Enter the root directory.
    ```
    cd Bankapp
    ```

3. Create a virtual environment or docker container
    ```
    python -m venv .venv
    ```
    Activate the virtual environments and install the requirements
    ```
    .venv\Scripts\activate
    pip install -r requirements.txt
    ```

    If using docker, create and start the container with the following command
    ```
    docker-compose up
    ```

3. Now start the setup by entering the following command.
    ```
    python manage.py runserver
    ```
