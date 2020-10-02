from src import app
from flask import render_template

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    """
    :return: 200 with message Hello World or username.
    """
    return render_template('hello.html.j2', name=name)
