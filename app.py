from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()
