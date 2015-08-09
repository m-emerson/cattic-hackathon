import MySQLdb.cursors
import hashlib

db = None

# here be the queries
def get_books_by_courseid(courseid):
	books = list()
	db = do_mysql_connect()
	cur = db.cursor()
	cur.execute("SELECT t.NAME, te.ISBN, te.PHOTO, te.DESCRIPTION, te.AUTHOR, te.EDITION, ctl.REQUIRED_STATUS FROM TEXTBOOKS t, TEXTBOOK_EDITIONS te, COURSE_TEXTBOOK_LINK ctl, COURSES c WHERE t.TEXTBOOKID = te.MASTER_TEXTBOOKID AND c.COURSEID = ctl.COURSEID AND ctl.TEXTBOOKID = t.TEXTBOOKID AND c.CODE = %s GROUP BY te.ISBN", [courseid]);
	for row in cur.fetchall():
		books.append(row)
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

def get_books_by_courseid_and_reqstatus(courseid, reqstatus):
        books = list()
        db = do_mysql_connect()
        cur = db.cursor()
        cur.execute("SELECT t.NAME, te.ISBN, te.PHOTO, te.DESCRIPTION, te.AUTHOR, te.EDITION, ctl.REQUIRED_STATUS FROM TEXTBOOKS t, TEXTBOOK_EDITIONS te, COURSE_TEXTBOOK_LINK ctl, COURSES c WHERE t.TEXTBOOKID = te.MASTER_TEXTBOOKID AND c.COURSEID = ctl.COURSEID AND ctl.TEXTBOOKID = t.TEXTBOOKID AND c.CODE = %s AND ctl.REQUIRED_STATUS = %s GROUP BY te.ISBN", [courseid, reqstatus]);
        for row in cur.fetchall():
                books.append(row)
        return books

def get_book_image_by_isbn(isbn):
	db = do_mysql_connect()
	cur =  db.cursor()
	cur.execute("SELECT te.PHOTO FROM TEXTBOOK_EDITIONS te WHERE te.ISBN = %s", [isbn]);
        if cur.rowcount == 1:
                return cur.fetchone()['PHOTO']
        else:
                return 0

def get_listings_for_book(bookid):
	# search by ISBN
	listings = list()
	db = do_mysql_connect()
	cur = db.cursor()
	cur.execute("SELECT t.NAME, te.ISBN, te.PHOTO, te.DESCRIPTION, te.AUTHOR, te.EDITION, l.USERID, l.PRICE, l.ITEM_CONDITION, l.LISTINGID FROM TEXTBOOKS t, TEXTBOOK_EDITIONS te, LISTINGS l WHERE te.ISBN = l.TEXTBOOK_ISBN AND t.TEXTBOOKID = te.MASTER_TEXTBOOKID AND l.TEXTBOOK_ISBN = %s GROUP BY l.TEXTBOOK_ISBN", [bookid]);
	for row in cur.fetchall():
		listings.append(row)
	return listings

def get_book_by_isbn(isbn):
        db = do_mysql_connect()
        cur = db.cursor()
	cur.execute("SELECT t.NAME, te.ISBN, te.PHOTO, te.DESCRIPTION, te.AUTHOR, te.EDITION FROM TEXTBOOKS t, TEXTBOOK_EDITIONS te WHERE t.TEXTBOOKID = te.MASTER_TEXTBOOKID AND te.ISBN = %s", [isbn]);
	if cur.rowcount == 1:
		return cur.fetchone()
	else:
		return 0

def get_listings_by_username(username):
	listings = list()
	db = do_mysql_connect()
	cur = db.cursor()
	cur.execute("SELECT l.TEXTBOOK_ISBN, l.PRICE, l.ITEM_CONDITION, t.NAME, te.DESCRIPTION, te.AUTHOR, te.EDITION, te.PHOTO FROM LISTINGS l, TEXTBOOKS t, TEXTBOOK_EDITIONS te WHERE l.TEXTBOOK_ISBN = te.ISBN AND te.MASTER_TEXTBOOKID = t.TEXTBOOKID AND l.USERID = (SELECT USERID FROM USERS WHERE USERNAME=%s)", [username])
	for row in cur.fetchall():
		listings.append(row)
	return listings

def get_user_profile(username):
	db = do_mysql_connect()
	cur = db.cursor()
	cur.execute("SELECT USERNAME, NAME, EMAIL FROM USERS WHERE USERNAME=%s", [username])
	if cur.rowcount == 1:
		return cur.fetchone()
	else:
		return 0

def create_listing(isbn, username, price, condition):
	db = do_mysql_connect()
	cur = db.cursor()
	userid = None
	cur.execute("SELECT USERID FROM USERS WHERE USERNAME = %s", [username]);
	if cur.rowcount == 1:
		userid = cur.fetchone()['USERID']
	else:
		return -1
	try:
		cur.execute("INSERT INTO LISTINGS (TEXTBOOK_ISBN, USERID, PRICE, ITEM_CONDITION) VALUES (%s, %s, %s, %s)", [isbn, userid, price, condition]);
		db.commit()
	except MySQLdb.Error as e:
		db.rollback()
		return 0
	return 1

def update_listing(listingid, price, condition):
	db = do_mysql_connect()
	cur = db.cursor()
	try:
		cur.execute("UPDATE LISTINGS SET PRICE = %s, ITEM_CONDITION = %s WHERE LISTINGID = %s", [price, condition, listingid])
		db.commit()
	except MySQLdb.Error as e:
		db.rollback()
		return 0
	return 1

def delete_listing(listingid):
	db = do_mysql_connect()
	cur = db.cursor()
	try:
		cur.execute("DELETE FROM LISTINGS WHERE LISTINGID = %s", [listingid]);
		db.commit()
	except MySQLdb.Error as e:
		db.rollback()
		return 0
	return 1

def register_user(username, password, email, name):
	# hash up password before putting in the databus
	hashed_password = hashlib.sha512(password).hexdigest()
	db = do_mysql_connect()
	cur = db.cursor()
	try:
		cur.execute("INSERT INTO USERS(username, password, email, name) VALUES(%s, %s, %s, %s)", [username, hashed_password, email, name])
		db.commit()
	except MySQLdb.Error as e:
		db.rollback()
		return 0
	return 1

def update_user_profile(username, email, name):
	db = do_mysql_connect()
	cur = db.cursor()
	try:
		cur.execute("UPDATE USERS SET EMAIL = %s, NAME = %s WHERE USERNAME = %s", [email, name, username])
		db.commit()
	except MySQLdb.Error as e:
		db.rollback()
		return 0
	return 1

def change_user_password(username, newpassword):
	hashed_password = hashlib.sha512(newpassword).hexdigest()
	db = do_mysql_connect()
	cur = db.cursor()
	try:
		cur.execute("UPDATE USERS SET PASSWORD = %s WHERE USERNAME = %s", [hashed_password, username])
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
	for i in range(len(keys)):
		print i
		kv[keys[i]] = values[i]
	return kv
