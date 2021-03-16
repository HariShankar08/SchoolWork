-- WHERE Clause
SELECT * FROM student1 WHERE class='12B';

-- Not equal to: <> as well as !=
SELECT * FROM student1 WHERE no <> 4;
SELECT * FROM student1 WHERE no != 4;

--
SELECT * FROM student1 WHERE class='12A' OR class='12B' OR class='12C';
SELECT * FROM student1 WHERE class IN ('12A', '12B', '12C');

-- LIKE Clause
SELECT * FROM student1 WHERE name LIKE 'D%';

/* For LIKE clauses, can use % or _
Differences: % ==> any number of characters
_ ==> only one character (1 _ == 1 letter)
SELECT * FROM student1 WHERE class LIKE '12_'; ==> 12A, 12B, 12C

% and _ are known as wildcard characters
*/

SELECT * FROM student1 WHERE name LIKE '____';

SELECT * FROM student1 WHERE name LIKE '%n'
SELECT * FROM student1 WHERE name LIKE '%h%';

INSERT INTO student1 (No, Name, Stipend, Stream, AvgMark, Class) VALUES
(11, 'A', 350.00, 'Nonmedical', 88.5, '12A');

-- Checking NULL
SELECT * FROM student1 WHERE Grade IS NULL;

-- Checking NOT NULL
SELECT * FROM student1 WHERE Grade IS NOT NULL;

-- BETWEEN Clause
SELECT * FROM student1 WHERE Stipend BETWEEN 300 AND 400;


-- ORDER BY Clause
SELECT * FROM student1 ORDER BY name;
SELECT * FROM student1 ORDER BY name DESC;

SELECT stream, name FROM student1 ORDER BY stream, name DESC;

-- SUM(), AVG(), MIN(), MAX()
SELECT MAX(stipend) FROM student1;
SELECT MIN(stipend) FROM student1;
SELECT SUM(stipend) FROM student1;
SELECT AVG(stipend) FROM student1;

-- DATES
CREATE TABLE foo (
  rollno INT UNIQUE,
  dob DATE,
  class CHAR(3)
);

INSERT INTO foo VALUES
(1, '2000-11-12', '11A'),
(2, '2001-12-03', '11B'),
(3, '1999-02-02', '12A'),
(4, '2000-12-23', '12B');

SELECT * FROM foo WHERE MONTH(dob) = 12;
SELECT * FROM foo WHERE MONTHNAME(dob) = 'DECEMBER';
