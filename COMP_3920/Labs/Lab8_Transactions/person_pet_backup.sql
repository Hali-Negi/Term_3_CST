CREATE DATABASE IF NOT EXISTS lab_example;
USE lab_example;

CREATE TABLE plane_seat (
    plane_seat_id INT PRIMARY KEY AUTO_INCREMENT,
    seat_number INT,
    description VARCHAR(10),
    occupied_by VARCHAR(255)
);

INSERT INTO plane_seat (seat_number, description) VALUES
(1,'1A'),(2,'1B'),(3,'1C'),(4,'1D'),
(5,'2A'),(6,'2B'),(7,'2C'),(8,'2D'),
(9,'3A'),(10,'3B'),(11,'3C'),(12,'3D'),
(13,'4A'),(14,'4B'),(15,'4C'),(16,'4D'),
(17,'5A'),(18,'5B'),(19,'5C'),(20,'5D');

SELECT * FROM plane_seat;
UPDATE plane_seat SET occupied_by = NULL WHERE plane_seat_id > 0;