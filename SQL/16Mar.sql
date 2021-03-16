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
(10, 'A', 350.00, 'Nonmedical', 88.5, '12A');

-- Checking NULL
SELECT * FROM student1 WHERE Grade IS NULL;

-- Checking NOT NULL
SELECT * FROM student1 WHERE Grade IS NOT NULL;

-- BETWEEN Clause
SELECT * FROM student1 WHERE Stipend BETWEEN 300 AND 400;


-- ORDER BY Clause
SELECT * FROM student1 ORDER BY name;
SELECT * FROM student1 ORDER BY name DESC;
