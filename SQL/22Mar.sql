-- Inner/ Nested Query (Not part of syllabus)
SELECT * FROM student1 WHERE stipend=(SELECT MAX(stipend) FROM student1);
