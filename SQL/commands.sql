/* Multi-line comment like this...
Close with this. */

-- Single line comments like this

-- Or with a #(space){comment text}

SHOW DATABASES;

CREATE DATABASE grade12;

CREATE DATABASE IF NOT EXISTS grade12;

USE grade12;

-- IF NOT EXISTS; optional keyword-phrase, creates (if not exists haha)

CREATE TABLE IF NOT EXISTS student (
    rollno INT,
    name CHAR(25)
);

SHOW TABLES;

DESC student;

/* For multiple alters, write full command;
ALTER TABLE student
ADD marks INT, m INT; -> DOES NOT WORK */

ALTER TABLE student
ADD marks INT,
ADD m INT;

ALTER TABLE student
DROP COLUMN m;


-- Use CHANGE for changing column names
ALTER TABLE student
CHANGE marks total_marks INT;
