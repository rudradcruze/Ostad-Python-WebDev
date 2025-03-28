CREATE DATABASE ostadTest;

USE ostadTest;

CREATE TABLE ostadTest.products (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	description TEXT,
	price DECIMAL(10,2) NOT NULL,
	stock INT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE ostadTest.products;

SHOW TABLES;

SELECT * FROM ostadTest.products;

INSERT INTO ostadTest.products (name, description, price, stock)
VALUES
('Laptop', 'Productivity Laptop', 1000.00, 22),
('Laptop', 'Gaming Laptop', 5000.00, 25);

SELECT * FROM ostadTest.products p WHERE p.id = 2;

SELECT * FROM ostadTest.products p WHERE p.price >= 1500;

UPDATE ostadTest.products SET
name = 'Gaming Laptop PHP',
description = 'Gaming Laptop PHP - 8gb ram 0 256gb ssd',
stock = 24
WHERE id = 3;

SELECT * FROM ostadTest.products p WHERE p.id = 3;

SELECT name, description, price, stock
FROM ostadTest.products WHERE id = 3;

DELETE FROM ostadTest.products WHERE id = 2;

SELECT * FROM ostadTest.products;


SELECT * FROM ostadTest.products p
WHERE p.stock IN (22, 25, 34, 35);

SELECT * FROM ostadTest.products p
WHERE p.stock NOT IN (22, 25, 34, 35);


INSERT INTO ostadTest.products (name, description, price, stock)
VALUES
('Smartphone', 'Latest model with OLED display', 700.00, 50),
('Tablet', '10-inch tablet with stylus support', 350.00, 30),
('Smartwatch', 'Fitness tracker with heart rate monitor', 150.00, 100),
('Headphones', 'Noise-cancelling over-ear headphones', 200.00, 80),
('Keyboard', 'Mechanical keyboard with RGB lighting', 120.00, 60),
('Mouse', 'Wireless mouse with ergonomic design', 30.00, 150),
('Monitor', '27-inch 4K UHD monitor', 500.00, 40),
('External Hard Drive', '1TB external storage device', 80.00, 70),
('Webcam', 'HD webcam for streaming', 60.00, 90),
('Printer', 'All-in-one inkjet printer', 100.00, 20);

SELECT * FROM ostadTest.products;

SELECT name AS Product_Name, description as Product_Description
FROM ostadTest.products;


SELECT * FROM ostadTest.products p ORDER BY p.price ASC;

SELECT * FROM ostadTest.products p ORDER BY p.price DESC;

SELECT * FROM ostadTest.products p ORDER BY p.created_at DESC;

SELECT * FROM ostadTest.products p ORDER BY p.created_at ASC;

SELECT * FROM ostadTest.products LIMIT 5;

SELECT * FROM ostadTest.products p ORDER BY p.price DESC LIMIT 5;

SELECT * FROM ostadTest.products p WHERE p.description LIKE 'a%';

SELECT * FROM ostadTest.products p WHERE p.description LIKE '%d';

SELECT * FROM ostadTest.products p WHERE p.description LIKE '%et%';

CREATE TABLE categories (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) UNIQUE NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

INSERT INTO ostadTest.categories (name)
VALUES
('Electronics'),
('Home Appliances'),
('Furniture'),
('Books'),
('Toys'),
('Clothing'),
('Sports Equipment'),
('Food & Beverages'),
('Beauty Products'),
('Automotive');


SELECT * FROM ostadTest.categories;

ALTER TABLE ostadTest.products ADD COLUMN category_id INT;

ALTER TABLE ostadTest.products
ADD FOREIGN KEY (category_id)
REFERENCES ostadTest.categories(id)
ON DELETE SET NULL
ON UPDATE CASCADE;

DELETE FROM ostadTest.products;

SELECT * FROM ostadTest.products;

INSERT INTO ostadTest.products (name, description, price, stock, category_id)
VALUES 
('Smartphone X', 'Latest smartphone with AI camera', 800.00, 40, 1),
('Tablet Pro', 'High-performance tablet with 12-inch display', 450.00, 30, 1),
('Smartwatch Ultra', 'Advanced fitness tracker with GPS', 200.00, 60, 1),
('Wireless Earbuds', 'Noise-cancelling earbuds with 24-hour battery life', 150.00, 70, 1),
('Gaming Laptop Elite', 'Powerful gaming laptop with RTX graphics', 1500.00, 20, 1),
('Tablet Pro', 'High-performance tablet with 12-inch display', 450.00, 30, 1),
('Refrigerator Plus', 'Energy-efficient double-door refrigerator', 1200.00, 15, 2),
('Microwave Oven', 'Compact microwave oven with multiple presets', 250.00, 50, 2),
('Air Purifier', 'HEPA filter air purifier for large rooms', 300.00, 25, 2),
('Vacuum Cleaner', 'Lightweight cordless vacuum cleaner', 180.00, 35, 2),
('Washing Machine', 'Front-loading washing machine with steam cleaning', 900.00, 10, 2),
('Sofa Set Deluxe', 'Leather sofa set with recliner', 1500.00, 5, 3),
('Dining Table', 'Modern dining table with 6 chairs', 800.00, 12, 3),
('Office Chair Ergo', 'Ergonomic office chair with lumbar support', 250.00, 20, 3),
('Bed Frame King', 'King-size bed frame with storage', 1000.00, 8, 3),
('Bookshelf Modern', 'Minimalist design bookshelf with 5 shelves', 150.00, 25, 3),
('Novel Adventure', 'Exciting adventure novel by best-selling author', 20.00, 100, 4),
('Science Textbook', 'Comprehensive guide to physics and chemistry', 50.00, 40, 4),
('Cooking Recipes', 'Collection of international recipes', 30.00, 60, 4),
('History Book', 'Detailed account of world history', 40.00, 30, 4),
('Self-Help Guide', 'Motivational book for personal growth', 25.00, 50, 4),
('Remote Control Car', 'High-speed RC car with rechargeable battery', 50.00, 30, 5),
('Building Blocks Set', 'Creative building blocks for kids', 40.00, 40, 5),
('Action Figures Pack', 'Set of action figures from popular movies', 60.00, 20, 5),
('Board Game Family', 'Fun board game for family nights', 35.00, 25, 5),
('Doll House', 'Miniature doll house with furniture', 70.00, 15, 5),
('Men T-Shirt', 'Cotton t-shirt in multiple colors', 20.00, 80, 6),
('Women Jeans', 'Slim-fit jeans for women', 50.00, 50, 6),
('Kids Jacket', 'Warm winter jacket for kids', 40.00, 30, 6),
('Sports Shorts', 'Breathable shorts for workouts', 30.00, 40, 6),
('Formal Suit', 'Classic suit for men', 200.00, 10, 6),
('Basketball Ball', 'Official size basketball for indoor/outdoor use', 30.00, 60, 7),
('Yoga Mat', 'Non-slip yoga mat with carrying strap', 25.00, 70, 7),
('Tennis Racket', 'Lightweight tennis racket for beginners', 80.00, 20, 7),
('Running Shoes', 'Comfortable running shoes with cushioning', 120.00, 30, 7),
('Cycling Helmet', 'Aerodynamic cycling helmet with ventilation', 50.00, 40, 7),
('Coffee Beans', 'Premium Arabica coffee beans', 15.00, 100, 8),
('Energy Drink', 'Refreshing energy drink with vitamins', 2.00, 200, 8),
('Chocolate Bar', 'Dark chocolate bar with 70% cocoa', 3.00, 150, 8),
('Protein Powder', 'Whey protein powder for muscle recovery', 40.00, 50, 8),
('Snack Mix', 'Healthy snack mix with nuts and dried fruits', 5.00, 120, 8),
('Moisturizer Cream', 'Hydrating moisturizer for all skin types', 30.00, 70, 9),
('Lipstick Matte', 'Long-lasting matte lipstick in bold colors', 15.00, 90, 9),
('Shampoo Anti-Dandruff', 'Anti-dandruff shampoo with natural ingredients', 20.00, 60, 9),
('Face Mask Sheet', 'Sheet mask for glowing skin', 5.00, 150, 9),
('Perfume Eau de Parfum', 'Luxurious perfume with floral notes', 100.00, 20, 9),
('Car Wax Polish', 'Protective wax polish for cars', 25.00, 50, 10),
('Tire Inflator', 'Portable tire inflator with digital gauge', 40.00, 30, 10),
('Car Seat Cover', 'Leather car seat cover set', 100.00, 20, 10),
('Headlight Restorer', 'Restores clarity to cloudy headlights', 15.00, 60, 10),
('Engine Oil Synthetic', 'Synthetic engine oil for high performance', 60.00, 40, 10);

SELECT category_id, COUNT(ostadTest.products.id) AS Product_Count
FROM ostadTest.products
GROUP BY category_id;

SELECT category_id, COUNT(id) AS Product_Count
FROM ostadTest.products
GROUP BY category_id
HAVING Product_Count >= 6;


SELECT p.id, p.name, p.description, p.price, c.name
FROM ostadTest.products p
INNER JOIN ostadTest.categories c
ON p.category_id = c.id;


SELECT *
FROM ostadTest.products p
LEFT JOIN ostadTest.categories c
ON p.category_id = c.id;

SELECT *
FROM ostadTest.products p
RIGHT JOIN ostadTest.categories c
ON p.category_id = c.id;

SELECT *
FROM ostadTest.products p
CROSS JOIN ostadTest.categories c;
-- ON p.category_id = c.id;

SELECT COUNT(*) FROM ostadTest.products;

SELECT COUNT(*) AS Product_Count FROM ostadTest.products;

SELECT SUM(p.price) AS Total_Price_Product FROM ostadTest.products p;

SELECT MIN(p.price) AS Product_Price_Min FROM ostadTest.products p;

SELECT MAX(p.price) AS Product_Price_Max FROM ostadTest.products p;

SELECT AVG(p.price) AS Product_Price_Avg FROM ostadTest.products p;

SELECT MAX(p.price) AS Second_Large_Price
FROM ostadTest.products p
WHERE p.price NOT IN (
	SELECT MAX(p.price) FROM ostadTest.products p
);


SELECT * FROM ostadTest.products p
WHERE p.price = 1000 AND p.stock = 22;