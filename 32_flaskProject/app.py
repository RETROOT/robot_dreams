from flask import Flask, render_template, jsonify, request, redirect, url_for, abort
import logging
import re

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


users_data = ["Alice", "Bob", "Charlie", "David", "Eve"]
books_data = ["Book 1", "Book 2", "Book 3", "Book 4", "Book 5"]

def validate_username(username):
    return len(username) >= 5

def validate_password(password):
    return len(password) >= 8 and re.search(r'\d', password) and re.search(r'[A-Z]', password)

@app.route('/users', methods=['GET'])
def get_users():
    logger.info('Handling /users endpoint')
    count = request.args.get('count')
    if count:
        try:
            count = int(count)
        except ValueError:
            abort(400, "Invalid count parameter")
    else:
        count = len(users_data)
    return jsonify(users_data[:count])

@app.route('/books', methods=['GET'])
def get_books():
    logger.info('Handling /books endpoint')
    count = request.args.get('count')
    if count:
        try:
            count = int(count)
        except ValueError:
            abort(400, "Invalid count parameter")
    else:
        count = len(books_data)
    if 'html' in request.args:
        return render_template('books.html', books=books_data[:count])
    else:
        return jsonify(books_data[:count])

@app.route('/params', methods=['GET'])
def get_params():
    logger.info('Handling /params endpoint')
    params = request.args.items()
    return render_template('params.html', params=params)

@app.route('/login', methods=['GET', 'POST'])
def login():
    logger.info('Handling /login endpoint')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if validate_username(username) and validate_password(password):
            return redirect(url_for('get_users'))
        else:
            abort(400, "Invalid username or password")
    return render_template('login_form.html')

@app.route('/')
def index():
    logger.info('Handling / endpoint')
    return '''
    <h1>Welcome to Flask Example</h1>
    <ul>
        <li><a href="/login">Login</a></li>
        <li><a href="/users">Users</a></li>
        <li><a href="/books">Books</a></li>
        <li><a href="/params">Query Parameters</a></li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)
