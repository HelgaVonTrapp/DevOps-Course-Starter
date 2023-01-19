from flask import Flask, redirect,request,render_template
from todo_app.data.trello_items import get_items, add_item, update_item
from todo_app.flask_config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        todos = get_items()
        return render_template('index.html',todos=todos)

    @app.route('/todo', methods=['POST'])
    def addtodo():
        title=request.form["title"]
        add_item(title)
        return redirect('/')

    @app.route('/completeitem/<id>', methods=['POST'])  
    def complete_item(id):
        update_item(id)
        return redirect('/')
    return app




