CREATE TABLE Analysis (
    an_id INT PRIMARY KEY,
    an_name VARCHAR(255),
    an_cost DECIMAL(10, 2),
    an_price DECIMAL(10, 2),
    an_group INT
);

CREATE TABLE `Groups` (
    gr_id INT PRIMARY KEY,
    gr_name VARCHAR(255),
    gr_temp VARCHAR(255)
);

CREATE TABLE Orders (
    ord_id INT PRIMARY KEY,
    ord_datetime DATETIME,
    ord_an INT,
    FOREIGN KEY (ord_an) REFERENCES Analysis(an_id)
);


INSERT INTO Analysis (an_id, an_name, an_cost, an_price, an_group) VALUES
(1, 'Blood Test', 10.00, 20.00, 1),
(2, 'Urine Test', 5.00, 15.00, 1),
(3, 'X-Ray', 50.00, 100.00, 2);

INSERT INTO `Groups` (gr_id, gr_name, gr_temp) VALUES
(1, 'Basic Tests', 'Room Temperature'),
(2, 'Advanced Tests', 'Refrigerated Storage'),
(3, 'Specialized Tests', 'Freezer Storage');


INSERT INTO Orders (ord_id, ord_datetime, ord_an) VALUES
(1, '2020-02-05 10:00:00', 1),
(2, '2020-02-06 12:00:00', 2),
(3, '2020-02-10 14:00:00', 3),
(4, '2020-02-13 16:00:00', 1);


SELECT a.an_name, a.an_price
FROM Orders o
JOIN Analysis a ON o.ord_an = a.an_id
WHERE o.ord_datetime BETWEEN '2020-02-05 00:00:00' AND '2020-02-12 23:59:59';