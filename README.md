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

Basic tests have been added in tests and tests_end2end folder. Docker-compose.yml has been added so you can run 'docker compose up' to launch a test docker container that will run the tests. You can launch the application by opening browser and going to http://localhost:5100/.
You can run these tests without Docker by using this command 'poetry run pytest'

A Github actions workflow has been added, this ignores any updates to this document (README.md)
The workflow will test building the docker container on push and pull requests. The workflow will run the tests on the main branch and exercise-7#2 branch you can amend this in ci-workflow.yml for any branch you wish.
Open Github and then open actions to view the workflow tests to see if they have run successfully.
Images are now deployed to DockerHub for development you can access using this link: 'https://hub.docker.com/repository/docker/helencurtis02/todo-app-dev/general'

You can now run your production docker image using Azure.
--------------------------------------------------------
Prerequisite is you have an azure account and you have installed the azure cli, follow these steps to deploy the production Todo App docker image to docker hub and to run the web app using azure.
1.	From a terminal window login to azure: ‘az login’
2.	Build the docker file: ‘docker build --target production --tag helencurtis02/todo-app-prod:latest .’
3.	Push the image to docker hub: ‘docker push helencurtis02/todo-app-prod:latest’
4.	Image should now be in docker hub.
5.	Next you need to create a web app within your azure portal environment. Create a WebApp resource for a docker container name ‘helcur-todoapp-prod’. 
6.	For Docker image and tag use ‘helencurtis02/todo-app-prod:latest’.
7.	Remaining settings should be defaults, add tags if you wish then click create.
8.	From the azure portal for your web app, you will need to go to configuration and enter the following application settings adding values for your Trello board, do not forget to click Save once they have all been created.
WEBSITES_PORT
8000

Name: FLASK_APP
Value: todo_app/app

Name: FLASK_ENV
Value: production

Name: SECRET_KEY
Value: [Your SECRET_KEY]

Name: TRELLO_BOARD_URL
Value: [Your TRELLO_BOARD_URL]

Name: TRELLO_KEY
Value: [Your TRELLO_KEY]

Name: TRELLO_TOKEN
Value: [Your TRELLO_TOKEN]

Name: TRELLO_TODO_LIST
Value: [Your TRELLO_TODO_LIST]

Name: TRELLO_DONE_LIST
Value: [Your TRELLO_DONE_LIST]

9.	Now browse to this url ‘https://helcur-todoapp-prod.azurewebsites.net/’and the website should be displayed in your browser.

Updating the container
----------------------
1.	Locate the Webhook URL from the Deployment Center Settings page
2.	Add in a backslash to escape the $ , and run: 
    ‘curl -dH -X POST https://\$<your_deployment_username>:<your_deployment_password>@<your_webap_name>.scm.azurewebsites.net/api/registry/webhook’
3.	This will return a link that you can click on to see the log stream which show the image restarting.
4.	Logs should look like this:
Status: Image is up to date for helencurtis02/todo-app-prod:latest
2023-04-05T17:23:21.207Z INFO  - Docker Hook Operation 0e17fc02-7440-4392-9fe5-51ef075fd6ae successful, Time taken: 0 Minutes and 4 Seconds
2023-04-05T17:23:21.425Z INFO  - Starting container for site

Updated for Continuous Deployment
---
When code is updated on the main branch the pipeline will now automatically run the built in tests and if successfull will update the DockerHub image for production and then updates the build in Azure. 

To-Do-App now uses MongoDB instead of Trello
--
To configure to use with your own MongoDB, update these new variables in the .env to match your MongoDB in Azure, You can now remove all references to Trello:

MONGO_CONNECTION_STRING: Set this to your PRIMARY CONNECTION STRING found in Azure

MONGO_DB_NAME: Set this to your Mongo DB name

Add the above as application settings to the Azure application, again the Trello settings can now be removed. 

1. Create a new collection for your database:

2. From your MongoDB in Azure click --> New Collection
Set Collection id = <b>todoapp-Collection</b>

3. Sharding --> select Unsharded

4. Analytical store is default to Off --> leave as default

5. Under Advanced - indexing for create a Wildcard index.. is enabled leave as default
