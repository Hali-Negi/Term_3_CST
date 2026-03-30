-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: chat_system
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `message`
--

DROP DATABASE IF EXISTS chat_messaging;
CREATE DATABASE IF NOT EXISTS chat_messaging;

USE chat_messaging;

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `message_id` int NOT NULL AUTO_INCREMENT,
  `room_user_id` int NOT NULL,
  `sent_datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `text` text NOT NULL,
  PRIMARY KEY (`message_id`),
  KEY `message_room_user` (`room_user_id`),
  CONSTRAINT `message_room_user` FOREIGN KEY (`room_user_id`) REFERENCES `room_user` (`room_user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,16,'2023-01-19 13:05:16','My favourite is orange tabbys'),(2,15,'2023-01-19 13:05:48','Mine is siamese'),(3,17,'2023-01-19 13:06:16','My cat likes to sleep in my bookshelf'),(4,15,'2023-01-19 13:06:52','Argh! I can\'t get my cat to stop stratching the couch!'),(5,6,'2023-01-19 13:07:51','I can\'t believe they raised the parking prices again!'),(6,18,'2023-01-19 13:08:26','German shepards are the smartest dogs.'),(7,7,'2023-01-19 13:09:08','I think they should raise prices. Maybe fewer people will drive and more will take transit.'),(8,8,'2023-01-19 13:09:50','We should get a discount if we are employees.'),(9,19,'2023-01-19 13:10:17','I like pugs'),(10,20,'2023-01-19 13:11:02','My dog loves to go for long hikes with me. He even packs his own food.'),(11,30,'2023-01-20 14:44:14','I saw a great movie about databases today. I can’t wait for the SQL.'),(12,23,'2023-01-20 14:52:32','Quiz next week on how to install the software'),(13,31,'2023-01-20 14:52:58','I keep all my dad jokes in a \"Dad-a-base\".'),(14,29,'2023-01-20 15:23:05','3 SQL databases walked into a NoSQL bar. A little while later they walked out, because they couldn’t find a table.'),(15,21,'2023-01-20 15:33:01','My bucket list includes: Mexico, Bahamas, New Zealand and Scotland'),(16,9,'2023-01-20 15:33:25','I can\'t get enough Pizza! :P'),(17,12,'2023-01-20 15:34:05','I just made myself some lazagne. Gonna freeze some and take it for lunches this week.'),(18,31,'2023-01-20 15:34:24','To understand what recursion is, you must first understand recursion.'),(19,31,'2023-01-20 15:36:17','Interviewer: \"Explain deadlock and we\'ll hire you.\"  Interviewee: \"Hire me and I\'ll explain it to you.\"'),(20,31,'2023-01-20 15:37:54','Why did the programmer quit his job? Because he couldn\'t get arrays.'),(21,31,'2023-01-20 15:38:41','There are 2 hard problems in computer science: caching, naming, and off-by-1 errors.'),(22,31,'2023-01-20 15:40:00','What’s the best thing thing about UDP jokes? I don’t care if you get them.'),(23,1,'2023-01-20 19:02:14','Who wants to go to the Mall on Saturday?'),(24,4,'2023-01-20 19:05:52','I will!'),(25,2,'2023-01-20 19:07:17','What about 5PM?');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `room_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `start_datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`room_id`),
  UNIQUE KEY `Unique_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (1,'Besties','2023-01-19 12:34:10'),(2,'Controversies','2023-01-19 12:35:40'),(3,'Fav Foods','2023-01-19 12:36:02'),(4,'Cats','2023-01-19 12:37:08'),(5,'Dogs','2023-01-19 12:41:31'),(6,'Vacations','2023-01-19 12:46:52'),(7,'School Notes','2023-01-19 12:57:08'),(8,'Jokes','2023-01-19 13:02:24');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room_user`
--

DROP TABLE IF EXISTS `room_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_user` (
  `room_user_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `room_id` int NOT NULL,
  PRIMARY KEY (`room_user_id`),
  UNIQUE KEY `unique_room_user` (`user_id`,`room_id`) /*!80000 INVISIBLE */,
  KEY `room_user_room_idx` (`room_id`),
  CONSTRAINT `room_user_room` FOREIGN KEY (`room_id`) REFERENCES `room` (`room_id`),
  CONSTRAINT `room_user_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_user`
--

LOCK TABLES `room_user` WRITE;
/*!40000 ALTER TABLE `room_user` DISABLE KEYS */;
INSERT INTO `room_user` VALUES (1,1,1),(2,4,1),(3,5,1),(4,6,1),(5,5,2),(6,2,2),(7,3,2),(8,4,2),(9,1,3),(10,6,3),(11,5,3),(12,4,3),(13,3,3),(14,2,3),(15,2,4),(16,3,4),(17,6,4),(18,5,5),(19,6,5),(20,4,5),(21,2,6),(22,3,6),(23,1,7),(24,3,7),(25,2,7),(26,6,7),(27,4,7),(28,5,7),(29,6,8),(30,1,8),(31,2,8);
/*!40000 ALTER TABLE `room_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(250) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(100) NOT NULL,
  `profile_img` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `Unique_user` (`username`) /*!80000 INVISIBLE */,
  UNIQUE KEY `Unique_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'bunny@gmail.com','fluffybunny91','hash',NULL),(2,'purplegreatness@gmail.com','greatbigpurple','hash','purple.png'),(3,'bigdude19421@hotmail.com','iamthedude','hash','dude.png'),(4,'justine_gilbert@yahoo.com','justice4all','hash','justy123.png'),(5,'regular_nothing@gmail.com','nothingspecial','hash',NULL),(6,'love4all@yahoo.com','iloveyou2','hash','heart_301.png');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-23 18:36:05
