import os
from flask import Flask, redirect,request,render_template
from flask_login import LoginManager, login_required, login_user
import requests
from todo_app.data.todo_items import get_items, add_item, update_item
from todo_app.data.user import User
from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        client_id = os.getenv('GITHUB_CLIENT_ID')
        return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}")
#        pass # Add logic to redirect to the GitHub OAuth flow when unauthenticated

    @login_manager.user_loader
    def load_user(user_id):
        #pass # We will return to this later
        return User(user_id)


    login_manager.init_app(app)

    @app.route('/')
    @login_required
    # def route_function():
    def index():
        todos = get_items()
        return render_template('index.html',todos=todos)

    @app.route('/login/callback/')
    def login():
        authorisation_code = request.args.get('code')
        client_id = os.getenv('GITHUB_CLIENT_ID')
        client_secret = os.getenv('GITHUB_CLIENT_SECRET')
        #code = authorisation_code
        params = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code" : authorisation_code
        }
        headers = {
            "Accept" : "application/json"

        }
        response = requests.post("https://github.com/login/oauth/access_token", params = params, headers= headers)

        response.raise_for_status()

        access_token = response.json()["access_token"]

        headers = {
            "Authorization" : f"Bearer {access_token}"

        }
        user_data_response = requests.get("https://api.github.com/user", headers = headers)
        
        user_id = user_data_response.json()["id"]

        login_user(User(user_id))
        return redirect('/')

    @app.route('/todo', methods=['POST'])
    @login_required
    def addtodo():
     title=request.form["title"]
     description=request.form["description"]
     add_item(title,description)
     return redirect('/')

    @app.route('/completeitem/<id>', methods=['POST'])
    @login_required
    def complete_item(id):
        update_item(id)
        return redirect('/')
    return app




