-- NATURAL JOIN
SELECT * FROM employee NATURAL JOIN job;
/* Same Column Name, Same Column Datatype required */


-- FOREIGN KEYS
CREATE TABLE cust (
  c_id INT PRIMARY KEY,
  name CHAR(10)
);

INSERT INTO cust VALUES
(1, 'AA'),
(2, 'BB'),
(3, 'CC');

CREATE TABLE ord (
  o_id INT,
  o_name CHAR(10),
  c_id INT
);

INSERT INTO ord VALUES
(11, 'Bed', 1),
(12, 'Table', 1),
(13, 'TV', 2),
(14, 'Phone', 3);

DELETE FROM cust WHERE c_id = 3;
INSERT INTO cust VALUES (3, 'CC');

-- Making a Foreign Key
CREATE TABLE ord (
  o_id INT PRIMARY KEY,
  o_name CHAR(10),
  c_id INT,
  FOREIGN KEY (c_id) REFERENCES cust(c_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO ord VALUES (15, 'Items', 4); -- Error!!!

DELETE FROM cust WHERE c_id = 3; -- Automatically deletes in ord because of ON DELETE CASCADE

/* For later versions of MySQL, default table engine is innodb. Previous versions would require you
to change the table engine with an ALTER statements */
