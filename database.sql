CREATE DATABASE  IF NOT EXISTS `donation` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `donation`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: donation
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `aid` int NOT NULL AUTO_INCREMENT,
  `adminid` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','4321');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank_details`
--

DROP TABLE IF EXISTS `bank_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank_details` (
  `bid` int NOT NULL AUTO_INCREMENT,
  `bname` varchar(255) NOT NULL,
  `pan` varchar(45) DEFAULT NULL,
  `bank` varchar(45) NOT NULL,
  `account` varchar(45) NOT NULL,
  `bmobile` varchar(45) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank_details`
--

LOCK TABLES `bank_details` WRITE;
/*!40000 ALTER TABLE `bank_details` DISABLE KEYS */;
INSERT INTO `bank_details` VALUES (1,'sandhya','7896541232145698','bank of india','4568971236547896','1236547896'),(2,'abhisekh','1236547896','boi','4568971236547845','5236547896'),(3,'nikki','yfviufguofo','SBI','6316416469464445','1641648458'),(5,'nikki','bgkjuhoii','SBI','62646946464464','4596321456');
/*!40000 ALTER TABLE `bank_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection`
--

DROP TABLE IF EXISTS `collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collection` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `pid` varchar(45) DEFAULT NULL,
  `collection` int DEFAULT NULL,
  `cdate` date DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection`
--

LOCK TABLES `collection` WRITE;
/*!40000 ALTER TABLE `collection` DISABLE KEYS */;
/*!40000 ALTER TABLE `collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `cname` varchar(255) DEFAULT NULL,
  `cemail` varchar(255) DEFAULT NULL,
  `csub` varchar(255) DEFAULT NULL,
  `cmobile` varchar(255) DEFAULT NULL,
  `cdesc` longtext,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (1,'anjali','anjali5236@gmail.com','issue ','1236589741','get lost');
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donar`
--

DROP TABLE IF EXISTS `donar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donar` (
  `did` int NOT NULL AUTO_INCREMENT,
  `dname` varchar(255) DEFAULT NULL,
  `demail` varchar(255) DEFAULT NULL,
  `dpan` varchar(255) DEFAULT NULL,
  `damt` int DEFAULT NULL,
  `caseid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donar`
--

LOCK TABLES `donar` WRITE;
/*!40000 ALTER TABLE `donar` DISABLE KEYS */;
INSERT INTO `donar` VALUES (26,'khushi','rahul@gmail.com','4561245',1000,'6'),(27,'anji','anji@gmail.com','45612',5000,'4'),(28,'pogo','pogo@gmail.com','4569852',2500,'1'),(29,'khushi','khushi@gmail.com','4569852',10000,'6'),(30,'nisha','nisha@gmail.com','dgfvsg',5000,'8'),(31,'anu','anu@gmail.com','fvkpmv',50000,'4'),(32,'anu','anu@gmail.com','csfvfsfc',20000,'4'),(33,'anu','anu@gmail.com','ZSC ',5000,'4'),(34,'neha','neha@gmail.com','sdjbadf',8000,'9'),(35,'abhi','abhi@gmail.com','djndfoi',2500,'9'),(36,'sonu','sonu@gmail.com','sdjdlk',1000,'6'),(37,'sonu','sonu@gmail.com','sdjdlk',1000,'6'),(38,'anji','anji@gmail.com','sfvsz',5000,'11');
/*!40000 ALTER TABLE `donar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `caseid` int NOT NULL AUTO_INCREMENT,
  `pname` varchar(255) NOT NULL,
  `pid` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `hname` varchar(255) NOT NULL,
  `haddress` varchar(255) NOT NULL,
  `cdetails` varchar(255) NOT NULL,
  `paddress` varchar(255) NOT NULL,
  `amt` int NOT NULL,
  `blood` varchar(255) NOT NULL,
  `p1` varchar(255) DEFAULT NULL,
  `p2` varchar(255) DEFAULT NULL,
  `p3` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  `status` int DEFAULT '1',
  PRIMARY KEY (`caseid`),
  UNIQUE KEY `pid_UNIQUE` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (6,'Shruti','45612345698','FEMALE','28','orchid','lalpur','asthma','lalpur',500000,'o-ve','bg1.jpg','bg2.jpg','What-Are-Plants.jpg','araj40132@gmail.com',0),(8,'kunal','1235648975','MALE','32','gandhinagar','kanke','kidney transplant','dharbhanga',5500000,'O+','liver.png','med.png','donate.png','araj40132@gmail.com',1),(9,'suraj','4562354897','MALE','16','orchid','FIRAYALAL','asthma','lalpur',1000000,'B+','med.png','hero-bg2.jpg','17.jpg','araj40132@gmail.com',1),(10,'titli','kjnxjklnxc','FEMALE','19','gandhi nagar','gandhi nagar','kidney transplant','kanke',2500000,'A+','med.png','agent-7.jpg','16.jpg','sandhyak23901@gmail.com',0),(11,'nirmal','gviugigo','MALE','26','gandhinagar','ranchi','typhoid','khalari',50000,'AB+','post-3.jpg','post-2.jpg','agent-6.jpg','sandhyak23901@gmail.com',1),(12,'Anish','hgukhgloi','MALE','25','apollo','ranchi','fever','lalpur',60000,'B+','post-3.jpg','about-2.jpg','post-1.jpg','sandhyak23901@gmail.com',1);
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `pid` int NOT NULL AUTO_INCREMENT,
  `caseid` varchar(45) DEFAULT NULL,
  `payid` varchar(45) DEFAULT NULL,
  `ord_id` varchar(45) DEFAULT NULL,
  `amt` int DEFAULT NULL,
  `donor_id` int DEFAULT NULL,
  `pay_date` varchar(45) DEFAULT NULL,
  `payable` float DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (7,'6','pay_NBMIi7RC8lx0Dp','order_NBMIQcfJW1Bwlq',1000,26,'2023-12-12',950),(8,'4','pay_NC3P3sFOVJeMDm','order_NC3OiG81Oal3Kt',5000,27,'2023-12-14',4750),(9,'1','pay_NC3QId0kvsIT7P','order_NC3PuG8ouE1t9T',2500,28,'2023-12-14',2375),(10,'6','pay_NC3T4pD7D0BsqA','order_NC3SjliLFKz9UN',10000,29,'2023-12-14',9500),(11,'8','pay_NDhvIz8hPvcHWY','order_NDhut2CRQ2ZZQA',5000,30,'2023-12-18',4750),(12,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(13,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(14,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(15,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(16,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(17,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(18,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(19,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(20,'4','pay_NDifLvq9XP2zHV','order_NDif3HyIbyoHai',5000,33,'2023-12-18',4750),(21,'9','pay_NDisexI0FlmFul','order_NDisQkPfR9JX3E',8000,34,'2023-12-18',7600),(22,'9','pay_NDisexI0FlmFul','order_NDisQkPfR9JX3E',8000,34,'2023-12-18',7600),(23,'9','pay_NDisexI0FlmFul','order_NDisQkPfR9JX3E',8000,34,'2023-12-18',7600),(24,'9','pay_NDisexI0FlmFul','order_NDisQkPfR9JX3E',8000,34,'2023-12-18',7600),(25,'9','pay_NDisexI0FlmFul','order_NDisQkPfR9JX3E',8000,34,'2023-12-18',7600),(26,'9','pay_NDisexI0FlmFul','order_NDisQkPfR9JX3E',8000,34,'2023-12-18',7600),(27,'9','pay_NDisexI0FlmFul','order_NDisQkPfR9JX3E',8000,34,'2023-12-18',7600),(28,'9','pay_NDj7ZVrWf11wxq','order_NDj7ED07DDbY10',2500,35,'2023-12-18',2375),(29,'9','pay_NDj7ZVrWf11wxq','order_NDj7ED07DDbY10',2500,35,'2023-12-18',2375),(30,'6','pay_NDjGgAX35v1gwb','order_NDjGQt9zr6oHVZ',1000,37,'2023-12-18',950),(31,'6','pay_NDjGgAX35v1gwb','order_NDjGQt9zr6oHVZ',1000,37,'2023-12-18',950);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photo`
--

DROP TABLE IF EXISTS `photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `photo` (
  `photo_id` int NOT NULL AUTO_INCREMENT,
  `p1` varchar(255) NOT NULL,
  `p2` varchar(255) DEFAULT NULL,
  `p3` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`photo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photo`
--

LOCK TABLES `photo` WRITE;
/*!40000 ALTER TABLE `photo` DISABLE KEYS */;
INSERT INTO `photo` VALUES (1,'1699876765.','1699876765.','1699876765.',NULL),(2,'1699876973.jpg','1699876973.jpg','1699876973.',NULL);
/*!40000 ALTER TABLE `photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `proid` int NOT NULL AUTO_INCREMENT,
  `propic` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`proid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (1,'ice.jpg','araj40132@gmail.com'),(2,'18.jpg','sandhyak23901@gmail.com');
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `name` varchar(255) NOT NULL,
  `id` varchar(255) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Abhishekh','4526589652354789','1256985689','araj40132@gmail.com','81dc9bdb52d04dc20036dbd8313ed055'),('soni','75623148','7896541235','kumarisoni39300@gmail.com','81dc9bdb52d04dc20036dbd8313ed055'),('sandhya','4561236547896541','4585652567','sandhyak23901@gmail.com','81dc9bdb52d04dc20036dbd8313ed055');
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

-- Dump completed on 2023-12-23  8:57:12
