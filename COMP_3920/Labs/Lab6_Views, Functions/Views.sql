USE classicmodels;
CREATE VIEW employeesAndBosses AS
SELECT 
    e.employeeNumber,
    e.lastName,
    e.firstName,
    e.extension,
    e.email,
    e.officeCode,
    e.reportsTo,
    e.jobTitle,
    b.employeeNumber AS bossEmployeeNumber,
    b.lastName AS bossLastName,
    b.firstName AS bossFirstName
FROM employees e
LEFT JOIN employees b ON e.reportsTo = b.employeeNumber;
SHOW DATABASES;
SELECT * FROM employeesPerBoss;
USE classicmodels;
SELECT * FROM employeesAndBosses;

CREATE VIEW employeesPerBoss AS
SELECT 
    count(employeeNumber) AS `count(employeenumber)`,
    bossEmployeeNumber,
    bossFirstName,
    bossLastName
FROM employeesAndBosses
GROUP BY bossEmployeeNumber, bossFirstName, bossLastName;


SELECT * FROM employeesPerBoss;

CREATE VIEW productMarkups AS
SELECT 
    productCode,
    productName,
    buyPrice,
    MSRP,
    (MSRP-buyPrice)/buyPrice*100 AS markup,
    concat("+",round((MSRP-buyPrice)/buyPrice*100,1),"%") AS markupFormatted
FROM products;


SELECT * FROM productMarkups
WHERE markup > 75;

USE classicmodels;

CREATE TABLE systemvariables (
    systemvariables_id INT(11) NOT NULL AUTO_INCREMENT,
    keyname VARCHAR(25),
    thevalue VARCHAR(250),
    PRIMARY KEY (systemvariables_id)
);

INSERT INTO systemvariables (keyname, thevalue) VALUES ('nextProductId', '5000');

SELECT * FROM systemvariables;

DELIMITER $$
CREATE FUNCTION GetProductId() RETURNS VARCHAR(15)
 DETERMINISTIC
BEGIN
 DECLARE productId varchar(15);
 UPDATE systemvariables
 SET thevalue = @newvalue := thevalue + 1
 WHERE keyname = 'nextProductId';
 SELECT CONCAT('S', substring(year(now()),3,2), '_', @newvalue) 
 into productId;
RETURN (productId);
END $$
DELIMITER ;

SELECT GetProductId();



SET SQL_SAFE_UPDATES = 0;

SELECT GetProductId();

SELECT GetProductId();
UPDATE systemvariables SET thevalue = '5000' WHERE keyname = 'nextProductId';

SELECT GetProductId();

INSERT INTO products 
(productCode, productName, productLine, productScale, productVendor, 
productDescription, quantityInStock, buyPrice, MSRP)
VALUES 
(GetProductId(), 'Stealth Bomber', 'Planes', '1:200', 'Army Replicas', 
'Lockheed F-117 Nighthawk', 1000, 52.50, 98.25);

select * from products where productName = 'stealth bomber';
INSERT INTO systemvariables
(keyname, thevalue)
VALUES
('employeeCount', (SELECT count(*) FROM employees));

SELECT * FROM systemvariables;

DELIMITER $$
CREATE TRIGGER after_employee_insert 
 AFTER INSERT ON employees
 FOR EACH ROW 
BEGIN
 UPDATE systemvariables
 SET thevalue = thevalue + 1
 WHERE keyname = 'employeeCount';
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER after_employee_delete 
 AFTER DELETE ON employees
 FOR EACH ROW 
BEGIN
 UPDATE systemvariables
 SET thevalue = thevalue - 1
 WHERE keyname = 'employeeCount';
END$$
DELIMITER ;

INSERT INTO employees VALUES (1705, 'Kim', 'Mary', 'x2323', 'mkim@classicmodelcars.com', '4', 1102, 'Sales Rep');
INSERT INTO employees VALUES (1706, 'Bal', 'Zaf', 'x2324', 'zbal@classicmodelcars.com', '5', 1621, 'Sales Rep');

SELECT * FROM systemvariables WHERE keyname = 'employeeCount';

DELETE FROM employees WHERE employeeNumber = 1705;

SELECT * FROM systemvariables WHERE keyname = 'employeeCount';

DELETE FROM employees WHERE employeeNumber = 1705;

SELECT * FROM systemvariables WHERE keyname = 'employeeCount';

SELECT * FROM employees WHERE employeeNumber = 1705;

SHOW TRIGGERS LIKE 'employees';

UPDATE systemvariables SET thevalue = '23' WHERE keyname = 'employeeCount';

SELECT * FROM systemvariables WHERE keyname = 'employeeCount';

DELIMITER $$
CREATE PROCEDURE `check_products`(IN buyPrice DECIMAL(10,2), IN MSRP DECIMAL(10,2))
BEGIN
    DECLARE _messageText varchar(250);
    
    IF buyPrice < 0 THEN
        BEGIN
            SELECT CONCAT('Check constraint on products.buyPrice failed - buyPrice ',buyPrice,' must be positive.')
            INTO _messageText;
            SIGNAL SQLSTATE '45001'
            SET MESSAGE_TEXT = _messageText;
        END;
    END IF;
    
    IF MSRP < buyPrice THEN
        BEGIN
            SELECT CONCAT('Check constraint on products.buyPrice & products.MSRP failed - MSRP ',MSRP,' must be larger than buyPrice ',buyPrice)
            INTO _messageText;
            SIGNAL SQLSTATE '45002'
            SET MESSAGE_TEXT = _messageText;
        END;
    END IF;
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER `products_before_insert` BEFORE INSERT ON `products`
FOR EACH ROW
BEGIN
    CALL check_products(new.buyPrice, new.MSRP);
END$$ 
DELIMITER ;

DELIMITER $$
CREATE TRIGGER `products_before_update` BEFORE UPDATE ON `products`
FOR EACH ROW
BEGIN
    CALL check_products(new.buyPrice, new.MSRP);
END$$ 
DELIMITER ;

INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) VALUES (GetProductId(), 'Stealth Bomber 2', 'Planes', '1:200', 'Army Replicas', 'Northrop Grumman B-2 Spirit', 100, 52.50, 8.25);





SELECT productCode, productName, buyPrice, MSRP 
FROM products 
LIMIT 5;


SELECT productCode, productName, buyPrice, MSRP 
FROM products 
LIMIT 5;


UPDATE `classicmodels`.`products` 
SET `buyPrice` = '-53.50' 
WHERE `productCode` = 'S10_1678';


18:51:53	UPDATE `classicmodels`.`products`  SET `buyPrice` = '-53.50'  WHERE `productCode` = 'S10_1678'	Error Code: 1644. Check constraint on products.buyPrice failed - buyPrice -53.50 must be positive.	0.0011 sec

























