from flask import Flask, redirect,request,render_template
from flask_login import LoginManager
from todo_app.data.todo_items import get_items, add_item, update_item
from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    
    login_manager = LoginManager()
    @login_manager.unauthorized_handler
    def unauthenticated():
        pass # Add logic to redirect to the GitHub OAuth flow when unauthenticated
    @login_manager.user_loader
    def load_user(user_id):
        pass # We will return to this later
    login_manager.init_app(app)

    @app.route('/')
    def index():
        todos = get_items()
        return render_template('index.html',todos=todos)

    @app.route('/todo', methods=['POST'])
    def addtodo():
        title=request.form["title"]
        description=request.form["description"]
        add_item(title,description)
        return redirect('/')

    @app.route('/completeitem/<id>', methods=['POST'])
    def complete_item(id):
        update_item(id)
        return redirect('/')
    return app




