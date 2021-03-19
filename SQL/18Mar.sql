/* 18th March 2021 */

-- GROUP BY clause
SELECT Class, COUNT(*) AS 'Number of Students' FROM student1 GROUP BY Class;

/* COUNT(*) -> Number of rows in table
COUNT({{ column_name }}) -> Number of non NULL values in column */

SELECT Name, Class, COUNT(*) AS 'No of Students' FROM student1 GROUP BY Class;
/* In the above query, Name shows the FIRST occurence of the group */

SELECT Class, MAX(stipend) FROM student1 GROUP BY Class;

-- HAVING CLAUSE
SELECT Class, SUM(Stipend) FROM student1 GROUP BY Class HAVING SUM(stipend) > 400;

-- UPDATE Statements
UPDATE student1
SET Grade='A'
WHERE NO=11; -- WHERE NOT COMPULSORY, WILL THEN CHANGE ALL GRADES TO 'A'

-- DELETE STATEMENTS
DELETE FROM student1
WHERE NO=11;

/* Removing rows - DELETE not DROP, ya fool! */

CREATE TABLE student2 AS (SELECT * FROM student1);
INSERT INTO student2 (SELECT * FROM student1);

SELECT * FROM employee, job; -- Cartesian Product of two tables

-- JOIN (EQUI-JOIN)
SELECT EMPLOYEEID, NAME, SALES, JOBTITLE, SALARY, employee.JOBID FROM employee, job WHERE employee.JOBID = job.JOBID;

-- SHORTENING LONG TABLE NAMES
SELECT EMPLOYEEID, NAME, SALES, JOBTITLE, SALARY, employee.JOBID FROM employee emp, job WHERE emp.JOBID = job.JOBID;
-- For such statements DON'T USE AS

SELECT NAME, JOBTITLE, SALARY FROM employee, job WHERE employee.JOBID = job.JOBID AND job.JOBTITLE = 'Vice President';
