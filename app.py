from flask import Flask
from flask.ext.httpauth import HTTPBasicAuth

import queries as db
auth = HTTPBasicAuth()
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/profile")
@auth.login_required
def profile():
	return jsonify({ 'data' : 'Hello %s!' % g.user.username })

@auth.verify_password
def verify_password(username, password):
	user = db.authenticateUser(username, password)
	if not user:
		return False
	g.user = user
	return True	

if __name__ == "__main__":
	app.run()
