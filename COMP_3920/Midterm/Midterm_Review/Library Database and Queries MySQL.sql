DROP DATABASE IF EXISTS Library;

CREATE DATABASE Library;

USE Library;


CREATE TABLE book(
	book_id int auto_increment NOT NULL,
	title varchar(250) NOT NULL,
	author varchar(150) NOT NULL,
	book_type_id int NOT NULL,
 CONSTRAINT PK_book PRIMARY KEY CLUSTERED 
(
	book_id ASC
));


CREATE TABLE book_loan(
	book_loan_id int auto_increment NOT NULL,
	person_id int NOT NULL,
	book_id int NOT NULL,
 CONSTRAINT PK_book_loan PRIMARY KEY CLUSTERED 
(
	book_loan_id ASC
));


CREATE TABLE book_type(
	book_type_id int auto_increment NOT NULL,
	type varchar(50) NOT NULL,
 CONSTRAINT PK_book_type PRIMARY KEY CLUSTERED 
(
	book_type_id ASC
));


CREATE TABLE person(
	person_id int auto_increment NOT NULL,
	name varchar(50) NOT NULL,
 CONSTRAINT PK_person PRIMARY KEY CLUSTERED 
(
	person_id ASC
));


INSERT book (book_id, title, author, book_type_id) VALUES (1, 'Green Eggs and Ham', 'Dr. Seuss', 1);
INSERT book (book_id, title, author, book_type_id) VALUES (2, 'Cat in the Hat', 'Dr. Seuss', 1);
INSERT book (book_id, title, author, book_type_id) VALUES (3, 'My First Atlass of the World', 'National Geographic', 2);
INSERT book (book_id, title, author, book_type_id) VALUES (4, 'Everything Sharks', 'National Geographic', 2);
INSERT book (book_id, title, author, book_type_id) VALUES (5, 'Infopedia 2019', 'National Geographic', 2);

INSERT book_loan (book_loan_id, person_id, book_id) VALUES (1, 1, 1);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (2, 1, 2);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (3, 1, 3);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (4, 2, 3);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (5, 2, 4);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (7, 2, 5);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (8, 3, 1);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (9, 3, 2);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (10, 3, 3);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (11, 3, 4);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (12, 3, 5);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (13, 4, 4);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (14, 4, 4);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (15, 4, 4);
INSERT book_loan (book_loan_id, person_id, book_id) VALUES (16, 5, 1);


INSERT book_type (book_type_id, type) VALUES (1, 'fictio');
INSERT book_type (book_type_id, type) VALUES (2, 'non-fictio');


INSERT person (person_id, name) VALUES (1, 'Sam');
INSERT person (person_id, name) VALUES (2, 'Joe');
INSERT person (person_id, name) VALUES (3, 'Mary');
INSERT person (person_id, name) VALUES (4, 'Pal');
INSERT person (person_id, name) VALUES (5, 'Li');


ALTER TABLE book  ADD  CONSTRAINT FK_book_type FOREIGN KEY(book_type_id)
REFERENCES book_type (book_type_id);

ALTER TABLE book_loan   ADD  CONSTRAINT FK_book_loan_book FOREIGN KEY(book_id)
REFERENCES book (book_id);


ALTER TABLE book_loan   ADD  CONSTRAINT FK_book_loan_person FOREIGN KEY(person_id)
REFERENCES person (person_id);





-- #1	How many books are in the library?
SELECT COUNT(*) AS 'Number of Books'
FROM book;

-- #2	How many books are there of each type?
SELECT type, COUNT(*) AS 'Number of Books'
FROM book
INNER JOIN book_type ON book_type.book_type_id = book.book_type_id
GROUP BY type;

-- #3	How many books are there by 'Dr. Seuss'?
SELECT title, author
FROM book
WHERE author = 'Dr. Seuss';

-- #4	Show all books loaned out sorted by popularity
SELECT title, author, COUNT(*) AS 'Number of Loans'
FROM book_loan
INNER JOIN book ON book.book_id = book_loan.book_id
GROUP BY title, author
ORDER BY COUNT(*) DESC;

-- #5	Show only the most popular book.
SELECT title, author, COUNT(*) AS 'Number of Loans'
FROM book_loan
INNER JOIN book ON book.book_id = book_loan.book_id
GROUP BY title, author
HAVING COUNT(*) = (
	SELECT COUNT(*) AS 'Number of Loans'
	FROM book_loan
	INNER JOIN book ON book.book_id = book_loan.book_id
	GROUP BY title, author
	ORDER BY COUNT(*) DESC
    LIMIT 1
)
;

-- #6	Show each person and the total number of books they have loaned.
SELECT name, COUNT(book_id) AS 'Number of books loaned'
FROM person
INNER JOIN book_loan ON person.person_id = book_loan.person_id
GROUP BY name;

-- #7	Show each person and the types of books they borrowed 
-- (sort by the perso's name, then by the book type).
SELECT name, type, COUNT(type) AS 'Number of books loaned'
FROM person
INNER JOIN book_loan ON person.person_id = book_loan.person_id
INNER JOIN book ON book_loan.book_id = book.book_id
INNER JOIN book_type ON book_type.book_type_id = book.book_type_id
GROUP BY name, type
ORDER BY name, type;

-- #8	How many times has the book 'Everything Sharks' been loaned out?
SELECT count(*) AS 'Number of loans'
FROM book_loan 
INNER JOIN book ON book.book_id = book_loan.book_id
WHERE title = 'Everything Sharks';

