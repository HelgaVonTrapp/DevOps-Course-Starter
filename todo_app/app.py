from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items
from todo_app.flask_config import Config
app = Flask(__name__)
app.config.from_object(Config())
#Application code for listing predefined todo list from session_items.py
@app.route('/')
def index():
    todos = get_items()
    return render_template('index.html',todos=todos)
#Application code to add items when clicking on the button to post to list, uses add_item from session_items.py 
@app.route('/todo', methods=['POST'])
def addtodo():
    title=request.form["title"]
    add_item(title)
    return redirect('/')



