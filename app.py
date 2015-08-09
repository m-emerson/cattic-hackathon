from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth
from flask import render_template

import queries as db
auth = HTTPBasicAuth()
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

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

@app.route("/course")
def course():
	return render_template('course.html')

@app.route("/about")
def about():
	return render_template('about.html')

@auth.verify_password
def verify_password(username, password):
	user = db.authenticateUser(username, password)
	if not user:
		return False
	g.user = user
	return True	

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
