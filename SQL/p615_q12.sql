CREATE TABLE IF NOT EXISTS employee (
EMPLOYEEID CHAR(2),
NAME CHAR(25),
SALES INT,
JOBID INT);

INSERT INTO employee VALUES ('E1', 'SUMIT SINHA', '1100000', '102');
INSERT INTO employee VALUES ('E2', 'VIJAY SINGH TOMAR', '1300000', '101');
INSERT INTO employee VALUES ('E3', 'AJAY RAJPAL', '1400000', '103');
INSERT INTO employee VALUES ('E4', 'MOHIT RAMNANI', '1250000', '102');
INSERT INTO employee VALUES ('E5', 'SHAILJA SINGH', '1450000', '103');

CREATE TABLE IF NOT EXISTS job (
JOBID INT,
JOBTITLE CHAR(25),
SALARY INT);

INSERT INTO job VALUES ('101', 'President', '200000');
INSERT INTO job VALUES ('102', 'Vice President', '125000');
INSERT INTO job VALUES ('103', 'Administration Assistant', '80000');
INSERT INTO job VALUES ('104', 'Accounting Manager', '70000');
INSERT INTO job VALUES ('105', 'Accountant', '65000');
INSERT INTO job VALUES ('106', 'Sales Manager', '80000');
