from flask import Flask
from flask import render_template, request, redirect, send_file
import io

import queries as db
app = Flask(__name__)

app.secret_key = 'omgsuchsecrets'

@app.route("/")
def hello():
	return render_template('index.html')

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

@app.route("/book/<isbn>", methods=['GET', 'POST'])
def book(isbn):
	if request.method == 'POST':
		db.create_listing(request.form['isbn'], request.form['username'], request.form['price'], request.form['condition'])
	listings = db.get_listings_for_book(isbn)
	return render_template('book.html', listings=listings)

@app.route("/listing/add/<isbn>", methods=['POST'])
def add_listing(isbn):
	db.create_listing(isbn, username, price, condition)

@app.route("/course")
def course():
	return render_template('course.html')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/images/book/<isbn>.jpg")
def render_book_image(isbn):
	image_blob = db.get_book_image_by_isbn(isbn)
	return send_file(io.BytesIO(image_blob), attachment_filename=isbn + '.jpg', mimetype='image/jpeg')

@app.route("/courses/<courseid>")
def course_books(courseid):
	course = db.get_course_by_courseid(courseid)
	required_books = db.get_books_by_courseid_and_reqstatus(courseid, 'Required')
	recommended_books = db.get_books_by_courseid_and_reqstatus(courseid, 'Recommended')
	return render_template('course.html', course=course, required=required_books, recommended=recommended_books);

@app.route("/listings/create/<editionid>", methods=['GET', 'POST'])
def create_listing():
	return "woo"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
