/* 18th March 2021 */

-- GROUP BY clause
SELECT Class, COUNT(*) as 'Number of Students' FROM student1 GROUP BY Class;

/* COUNT(*) -> Number of rows in table
COUNT({{ column_name }}) -> Number of non NULL values in column */
