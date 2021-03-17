CREATE TABLE IF NOT EXISTS student1(
NO INT UNIQUE,
Name CHAR(25),
Stipend DECIMAL(5, 2),
Stream CHAR(25),
AvgMark DECIMAL(3, 1),
Grade CHAR(1),
Class CHAR(3));

INSERT INTO student1 VALUES ('1', 'Karan', '400.00', 'Medical', '78.5', 'B', '12B');

INSERT INTO student1 VALUES ('2', 'Divakar', '450.00', 'Commerce', '89.2', 'A', '11C');

INSERT INTO student1 VALUES ('3', 'Divya', '300.00', 'Commerce', '68.6', 'C', '12C');

INSERT INTO student1 VALUES ('4', 'Arun', '350.00', 'Humanities', '73.1', 'B', '12C');

INSERT INTO student1 VALUES ('5', 'Sabina', '500.00', 'Nonmedical', '90.6', 'A', '11A');

INSERT INTO student1 VALUES ('6', 'John', '400.00', 'Medical', '75.4', 'B', '12B');

INSERT INTO student1 VALUES ('7', 'Robert', '250.00', 'Humanities', '64.4', 'C', '11A');

INSERT INTO student1 VALUES ('8', 'Rubina', '450.00', 'Nonmedical', '88.5', 'A', '12A');

INSERT INTO student1 VALUES ('9', 'Vikas', '500.00', 'Nonmedical', '92.0', 'A', '12A');

INSERT INTO student1 VALUES ('10', 'Mohan', '300.00', 'Commerce', '67.5', 'C', '12C');
