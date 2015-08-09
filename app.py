from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth
from flask import render_template, request, redirect

import queries as db
auth = HTTPBasicAuth()
app = Flask(__name__)

app.secret_key = 'omgsuchsecrets'

@app.route("/")
def index():
	return "Hello World!"

@app.route("/test")
def test():
	return "HELLO!!!!"

@app.route("/profile")
def profile():
	return jsonify({ 'data' : 'Hello %s!' % g.user.username })

@app.route("/login", methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		user = db.authenticate_user(request.form['username'],
					    request.form['password'])
		if user:
			session['username'] = request.form['username']
			return redirect(url_for('index'))
		else:
			error = "Incorrect login details"
	return render_template('login.html', error=error)

@app.route("/book/<editionid>")
def book():
	return render_template('book.html')

@app.route("/images/book/<editionid>")
def render_book_image(bookid):
	return "render the book image by the id of the book"

@app.route("/courses/<courseid>")
def course_books(courseid):
	return "here is the course id"

@app.route("/listings/create/<editionid>", methods=['GET', 'POST'])
def create_listing():
	return "woo"

@auth.verify_password
def verify_password(username, password):
	user = db.authenticateUser(username, password)
	if not user:
		return False
	g.user = user
	return True	

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
