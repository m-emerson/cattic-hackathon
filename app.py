from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth
from flask import render_template, request, redirect

import queries as db
auth = HTTPBasicAuth()
app = Flask(__name__)

app.secret_key = 'omgsuchsecrets'

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/test")
def test():
	return "HELLO!!!!"

@app.route("/profile")
def profile():
	return jsonify({ 'data' : 'Hello %s!' % g.user.username })

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/book")
def book():
	return render_template('book.html')

@app.route("/images/book/<bookid>")
def render_book_image(bookid):
	return "render the book image by the id of the book"

@auth.verify_password
def verify_password(username, password):
	user = db.authenticateUser(username, password)
	if not user:
		return False
	g.user = user
	return True	

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
