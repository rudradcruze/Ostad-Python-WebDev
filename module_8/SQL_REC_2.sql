USE ostadTest;

ALTER TABLE categories 
CHANGE COLUMN name category_name VARCHAR(100);
 
DESCRIBE categories;

ALTER TABLE categories 
CHANGE COLUMN category_name name VARCHAR(100);
 
RENAME TABLE categories TO categories_new;
 
DESCRIBE categories_new;

ALTER TABLE categories_new RENAME TO categories;

CREATE TABLE person (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	age INT NOT NULL,
	address VARCHAR(255) NOT NULL 
);

DESCRIBE person;

ALTER TABLE person DROP COLUMN address;

DESCRIBE person;

DROP TABLE person;

DESCRIBE person;

CREATE DATABASE hello;

DROP DATABASE hello;

USE ostadTest;

SELECT AVG(price) FROM products;

-- Subquery
SELECT id, name, price, stock, category_id
FROM products p1
WHERE price > (
	SELECT AVG(price)
	FROM products p2
	WHERE p1.category_id = p2.category_id
);


-- Common table expressions (CTEs)
WITH AvgPrice AS (
	SELECT category_id, AVG(price) as cat_avg_salary
	FROM products
	GROUP BY category_id
)
SELECT p.id, p.name, p.price, p.stock, p.category_id
FROM products p
JOIN AvgPrice a ON a.category_id = p.category_id
WHERE p.price > a.cat_avg_salary;


-- Unique Indexing
CREATE UNIQUE INDEX idx_email on categories(email);