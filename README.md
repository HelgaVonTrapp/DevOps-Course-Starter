# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.
This is also used to add your own Trello API Key, Token and Board ID as these are spefic to your Trello account, so please add them using the follwing Variable names:
TRELLO_KEY='YOUR API KEY ID'
TRELLO_TOKEN='YOUR TOKEN ID'
TRELLO_BOARD='YOUR BOARD ID' 

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

With Module 5 we have containerised the to-do app with Docker
There are two environments you can run from the one dockerfile: Development using flask or Production using Gunicorn

To run the development server, first build the image using this command:
docker build --target development --tag todo-app-v0.3:dev .
  
Then to run the container, run this command:
docker run --env-file ./.env -p 5100:5000 -it --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app-v0.3:dev

To run the production server, first build the image using this command:
docker build --target production --tag todo-app-v0.3:prod .

Then to run the container, run this command:
docker run --env-file ./.env -p 5100:8000 -it --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app-v0.3:prod

Note: Port 5100 can be changed to another local port if preferred, if you wish to run the container in the background please enter docker run -d at the beginning of the command
Any updates made to the 'Todo_app' code will be automatically displayed within the browser once the webpage has been refreshed

If you wish to view context, container and component diagrams please view all files in the documentation folder of this repository. The .drawio files can be opened in Visual Studio Code and viewed providing you have installed the Draw.io Integration extension. 

Basic tests have been added in tests and tests_end2end folder. Docker-compose.yml has been added so you can run docker compose up to launch a test docker container that will run the tests. You can launch the application by opening browser and going to http://localhost:5100/.

A Github actions workflow has been added, this ignores any updates to this document (README.md)
The workflow will test building the docker container on push and pull requests. The workflow will run the tests on the main branch and exercise-7#2 branch you can amend this in ci-workflow.yml for any branch you wish.
Open Github and then open actions to view the workflow tests to see if the have run successfully.
