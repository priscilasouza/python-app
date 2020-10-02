"""
Python APP
"""
import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/health')
def health():
    """
    :return: 200 with message health
    """
    return 'Health!'


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    """
    :return: 200 with message Hello World or username.
    """
    return render_template('hello.html.j2', name=name)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    DEBUG = bool(os.environ.get('DEBUG', 'true'))
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
