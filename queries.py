import MySQLdb.cursors
import hashlib
import pprint

db = None

# here be the queries
def get_books_by_courseid(courseid):
	books = []
	return books

def get_course_by_courseid(courseid):
	# Course information
	db = do_mysql_connect()
	cur = db.cursor()
	cur.execute("SELECT CODE, NAME FROM COURSES WHERE CODE = %s", [courseid]);
	if cur.rowcount == 1:
		return cur.fetchone()
	else:
		return 0

def search(search_query):
	# e.g. GET COURSE LIKE "CSSE%"
	return true

def get_listings_for_book(bookid):
	return true

def register_user(username, password, email, name):
	# hash up password before putting in the databus
	hashed_password = hashlib.sha512(password).hexdigest()
	db = do_mysql_connect()
	cur = db.cursor()
	try:
		cur.execute("INSERT INTO USERS(username, password, email, name) VALUES(%s, %s, %s, %s)", [username, hashed_password, email, name]);
		db.commit()
	except MySQLdb.Error as e:
		db.rollback()
		return 0
	return 1

def authenticate_user(username, password):
	# hash the password
	hashed_password = hashlib.sha512(password).hexdigest()
	# check against database
	db = do_mysql_connect()
	cur = db.cursor()
	
	cur.execute("SELECT * FROM USERS WHERE username = %s and password = %s", [username, hashed_password]);
	if cur.rowcount != 0:
		return username
	# return the user if the password is correct
	# return false otherwise
	return 0

def read_mysql_password():
	f = open('mysql.passwd', 'r')
	passwd = f.read()
	f.close()
	return passwd.rstrip()

def do_mysql_connect():
	global db
	if db == None:
		db = MySQLdb.connect(db='booksearch', host='localhost', port=3306, user='book_interface', passwd=read_mysql_password(), cursorclass=MySQLdb.cursors.DictCursor)
	return db

def map_keys_to_values(keys, values):
	kv = dict()
	print keys[0]
	print values[0]
	for i in range(len(keys)):
		print i
		kv[keys[i]] = values[i]
	return kv
