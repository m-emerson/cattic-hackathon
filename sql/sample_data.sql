TRUNCATE TABLE COURSES;
TRUNCATE TABLE TEXTBOOKS;
TRUNCATE TABLE TEXTBOOK_EDITIONS;
TRUNCATE TABLE COURSE_TEXTBOOK_LINK;
TRUNCATE TABLE LISTINGS;
TRUNCATE TABLE USERS;
-- COURSES (COURSEID INT(6) UNSIGNED NOT NULL AUTO_INCREMENT, CODE VARCHAR(8) NOT NULL, NAME VARCHAR(100) NOT NULL, SEMESTER VARCHAR(1) NOT NULL)
INSERT INTO COURSES(CODE, NAME, SEMESTER) VALUES ("CSSE2310", "Computer Systems Principles and Programming", 2);
INSERT INTO COURSES(CODE, NAME, SEMESTER) VALUES ("INFS1200", "Introduction to Information Systems", 1);
INSERT INTO COURSES(CODE, NAME, SEMESTER) VALUES ("INFS2200", "Relational Database Systems", 2);
-- TEXTBOOKS (TEXTBOOKID INT UNSIGNED NOT NULL AUTO_INCREMENT, NAME VARCHAR(300) NOT NULL, PRIMARY KEY(TEXTBOOKID))
INSERT INTO TEXTBOOKS(NAME) VALUES ("C: A Reference Manual");
INSERT INTO TEXTBOOKS(NAME) VALUES ("Linux for Programmers and Users");
INSERT INTO TEXTBOOKS(NAME) VALUES ("Fundamentals of Database Systems");
-- TEXTBOOK_EDITIONS (ISBN BIGINT UNSIGNED NOT NULL, MASTER_TEXTBOOKID INT UNSIGNED NOT NULL, PHOTO VARCHAR(300), NAME VARCHAR(300) NOT NULL, DESCRIPTION VARCHAR(1000), AUTHOR VARCHAR(200), EDITION VARCHAR(40), PRIMARY KEY(ISBN))
INSERT INTO TEXTBOOK_EDITIONS(ISBN, MASTER_TEXTBOOKID, PHOTO, DESCRIPTION, AUTHOR, EDITION) VALUES (9780130895929, 1, LOAD_FILE("/var/textbook_images/9780130895929.jpg"), "This authoritative reference manual provides a complete description of the C language, the run-time libraries, and a style of C programming that emphasizes correctness, portability, and maintainability. The authors describe the C language more clearly and in more detail than in any other book.", "Samuel P. Harbison", "5");
INSERT INTO TEXTBOOK_EDITIONS(ISBN, MASTER_TEXTBOOKID, PHOTO, DESCRIPTION, AUTHOR, EDITION) VALUES (9780131857483, 2, LOAD_FILE("/var/textbook_images/9780131857483.jpg"), "Offering full coverage of Linux in one source, this book documents the most commonly needed topics for new and experienced Linux users and programmers - including over 100 utilities and their common options. Provides a good foundation of understanding for the most often-used Linux utilities. Devotes a chapter to helpful installation information for those who must install their own systems. Includes hundreds of command and code examples throughout. Provides approximately 50 diagrams throughout. ", "Graham Glass, King Ables", "1");
INSERT INTO TEXTBOOK_EDITIONS(ISBN, MASTER_TEXTBOOKID, PHOTO, DESCRIPTION, AUTHOR, EDITION) VALUES (9781292025605, 3, LOAD_FILE("/var/textbook_images/9781292025605.jpg"), "Clear explanations of theory and design, broad coverage of models and real systems, and an up-to-date introduction to modern database technologies result in a leading introduction to database systems. Intended for computer science majors, this text emphasizes math models, design issues, relational algebra, and relational calculus. A lab manual and problems give students opportunities to practice the fundamentals of design and implementation. Real-world examples serve as engaging, practical illustrations of database concepts. The Sixth Edition maintains its coverage of the most popular database topics, including SQL, security, and data mining, and features increased emphasis on XML and semi-structured data.", "Ramez Elmasri, Shamkant B. Navathe", "6");
-- USERS (USERID INT UNSIGNED NOT NULL AUTO_INCREMENT, USERNAME VARCHAR(50) NOT NULL, PASSWORD VARCHAR(500) NOT NULL, EMAIL VARCHAR(200) NOT NULL, NAME VARCHAR(200) NOT NULL, PRIMARY KEY(USERID), UNIQUE KEY user_username (USERNAME))
INSERT INTO USERS(USERNAME, PASSWORD, EMAIL, NAME) VALUES ('dcf', 'b8dfd29b2dd922fd494fb63a427e519dfaabc4489a4ade985c8eaaaef051a0f5272fd75ddda34211039997f8896b5f3693cd92eb75ea2bf786884aa0e31b9b36', 'dcf@example.com', 'Dcf Test');
INSERT INTO USERS(USERNAME, PASSWORD, EMAIL, NAME) VALUES ('quack', 'b8dfd29b2dd922fd494fb63a427e519dfaabc4489a4ade985c8eaaaef051a0f5272fd75ddda34211039997f8896b5f3693cd92eb75ea2bf786884aa0e31b9b36', 'quack@example.com', 'Quack Test');
-- COURSE_TEXTBOOK_LINK (COURSE_TEXTBOOK_LINK_ID INT UNSIGNED NOT NULL AUTO_INCREMENT, COURSEID INT UNSIGNED NOT NULL, TEXTBOOKID BIGINT UNSIGNED NOT NULL, REQUIRED_STATUS VARCHAR(15),  PRIMARY KEY(COURSE_TEXTBOOK_LINK_ID))
INSERT INTO COURSE_TEXTBOOK_LINK(COURSEID, TEXTBOOKID, REQUIRED_STATUS) VALUES (1, 1, 'Recommended');
INSERT INTO COURSE_TEXTBOOK_LINK(COURSEID, TEXTBOOKID, REQUIRED_STATUS) VALUES (1, 2, 'Required');
INSERT INTO COURSE_TEXTBOOK_LINK(COURSEID, TEXTBOOKID, REQUIRED_STATUS) VALUES (2, 3, 'Required');
INSERT INTO COURSE_TEXTBOOK_LINK(COURSEID, TEXTBOOKID, REQUIRED_STATUS) VALUES (3, 3, 'Required');
-- LISTINGS (LISTINGID INT UNSIGNED NOT NULL AUTO_INCREMENT, TEXTBOOK_ISBN INT UNSIGNED NOT NULL, USERID INT UNSIGNED NOT NULL, PRICE INT NOT NULL, ITEM_CONDITION VARCHAR(20), PRIMARY KEY(LISTINGID))
INSERT INTO LISTINGS(TEXTBOOK_ISBN, USERID, PRICE, ITEM_CONDITION) VALUES (9780130895929, 1, 129.90, 'Used');
INSERT INTO LISTINGS(TEXTBOOK_ISBN, USERID, PRICE, ITEM_CONDITION) VALUES (9780131857483, 1, 200, 'As new');
INSERT INTO LISTINGS(TEXTBOOK_ISBN, USERID, PRICE, ITEM_CONDITION) VALUES (9780130895929, 2, 50, 'Used');
COMMIT;
