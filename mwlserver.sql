-- MariaDB dump 10.17  Distrib 10.4.14-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: mwlserver
-- ------------------------------------------------------
-- Server version	10.4.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aetitlles`
--

DROP TABLE IF EXISTS `aetitlles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aetitlles` (
  `id_aetitle` int(11) NOT NULL AUTO_INCREMENT,
  `AEtitle` varchar(64) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `state` int(11) DEFAULT 1,
  PRIMARY KEY (`id_aetitle`),
  UNIQUE KEY `AEtitle` (`AEtitle`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aetitlles`
--

LOCK TABLES `aetitlles` WRITE;
/*!40000 ALTER TABLE `aetitlles` DISABLE KEYS */;
INSERT INTO `aetitlles` VALUES (1,'testmodality','for test purposes',1);
/*!40000 ALTER TABLE `aetitlles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conditions`
--

DROP TABLE IF EXISTS `conditions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `conditions` (
  `id_condition` int(11) NOT NULL AUTO_INCREMENT,
  `condition` varchar(100) DEFAULT NULL,
  `state` int(11) DEFAULT 1,
  PRIMARY KEY (`id_condition`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conditions`
--

LOCK TABLES `conditions` WRITE;
/*!40000 ALTER TABLE `conditions` DISABLE KEYS */;
INSERT INTO `conditions` VALUES (1,'igual',1),(2,'menor',1),(3,'mayor',1),(4,'contiene',1);
/*!40000 ALTER TABLE `conditions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parametros`
--

DROP TABLE IF EXISTS `parametros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parametros` (
  `idParametro` int(11) NOT NULL AUTO_INCREMENT,
  `nombreParametro` varchar(100) DEFAULT NULL,
  `valorINT` int(11) DEFAULT NULL,
  `valorChar` varchar(200) DEFAULT NULL,
  `state` int(11) DEFAULT 1,
  PRIMARY KEY (`idParametro`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parametros`
--

LOCK TABLES `parametros` WRITE;
/*!40000 ALTER TABLE `parametros` DISABLE KEYS */;
INSERT INTO `parametros` VALUES (1,'AEtitle',NULL,'r192mwl',1),(2,'port',11113,NULL,1);
/*!40000 ALTER TABLE `parametros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patients` (
  `id_patient` int(11) NOT NULL AUTO_INCREMENT,
  `PatientID` varchar(64) DEFAULT NULL,
  `PatientName` varchar(64) DEFAULT NULL,
  `PatientBirthDate` date DEFAULT NULL,
  `PatientSex` varchar(2) DEFAULT NULL,
  `state` int(11) DEFAULT 1,
  PRIMARY KEY (`id_patient`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,'12915084-k','CAMUS CACERES FLAVIO','1975-12-06','M',1);
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rule_conditions`
--

DROP TABLE IF EXISTS `rule_conditions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rule_conditions` (
  `id_rule_condition` int(11) NOT NULL AUTO_INCREMENT,
  `id_field` int(11) NOT NULL,
  `id_condition` int(11) DEFAULT NULL,
  `argument` varchar(100) DEFAULT NULL,
  `state` int(11) DEFAULT 1,
  PRIMARY KEY (`id_rule_condition`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rule_conditions`
--

LOCK TABLES `rule_conditions` WRITE;
/*!40000 ALTER TABLE `rule_conditions` DISABLE KEYS */;
/*!40000 ALTER TABLE `rule_conditions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rules`
--

DROP TABLE IF EXISTS `rules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rules` (
  `id_rule` int(11) NOT NULL,
  `rule_name` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `AEtitle` varchar(64) DEFAULT NULL,
  `state` int(11) DEFAULT 1,
  PRIMARY KEY (`id_rule`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rules`
--

LOCK TABLES `rules` WRITE;
/*!40000 ALTER TABLE `rules` DISABLE KEYS */;
INSERT INTO `rules` VALUES (0,'US de testmodality','Todas las US antes de las 12AM a testmodality','testmodality',1);
/*!40000 ALTER TABLE `rules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studies`
--

DROP TABLE IF EXISTS `studies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studies` (
  `study_id` varchar(64) DEFAULT NULL,
  `study_date` date DEFAULT NULL,
  `accession_number` varchar(64) DEFAULT NULL,
  `modality` varchar(8) DEFAULT NULL,
  `procedure` varchar(64) DEFAULT NULL,
  `patient_id` varchar(32) DEFAULT NULL,
  `patient_name` varchar(64) DEFAULT NULL,
  `patient_birth_date` date DEFAULT NULL,
  `patient_sex` varchar(3) DEFAULT NULL,
  `ref_physician` varchar(64) DEFAULT NULL,
  `state` int(11) DEFAULT 1,
  UNIQUE KEY `study_id` (`study_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studies`
--

LOCK TABLES `studies` WRITE;
/*!40000 ALTER TABLE `studies` DISABLE KEYS */;
INSERT INTO `studies` VALUES ('5fdbd054f3ad1f002af09689','2021-01-18','1054785681562759','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd39c59b1fa6b002a385de5','2021-02-01','4448641386393843','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd2e2589986dd002a365780','2021-01-18','2361036757721460','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd39cf2b1fa6b002a385dec','2021-01-18','9576969430088225','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd4e75af56962002a88ed4a','2021-01-25','7100290491009331','US','','25553351-7','UNKNOWN','0000-00-00','O','',1),('5fd913d1e3c7214a8e6d1cf6','2021-01-25','8935657503345522','US','','25553351-7','UNKNOWN','0000-00-00','O','',1),('5fd7cf0595e4c5002a0eee86','2021-02-08','7806882264173144','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd39d30b1fa6b002a385df3','2021-01-11','9764383114340335','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd39b99b1fa6b002a385dde','2021-01-18','4388910600815318','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd2e2929986dd002a365785','2021-01-04','1161630516698931','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd79b91aa0f4f002ab618e5','2020-12-21','0324405725651386','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd7c68595e4c5002a0eee52','2021-01-04','7374424635267448','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd7cc2e95e4c5002a0eee5c','2020-12-21','3197933591292655','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd7cd7095e4c5002a0eee7b','2021-01-04','3204575016755921','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd2e35b9986dd002a36578c','2021-01-11','6500651522512171','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd7cd5b95e4c5002a0eee6a','2020-12-21','1511657267234463','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fdf6bac8ea577002a63812a','2021-01-11','2107864330411036','US','','25553351-7','UNKNOWN','0000-00-00','O','',1),('5fd3cd6d942825002a80ad29','2021-01-04','3798940459811648','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('5fd4e4cdf56962002a88ed43','2021-02-01','9469324328587483','US','','25553351-7','UNKNOWN','0000-00-00','O','',1),('5fd7c6ee95e4c5002a0eee57','2021-01-04','9228939329061016','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('6025d78cf11a9d002adf6770','2021-02-16','5819957419609322','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('6025d9f2f11a9d002adf677c','2021-02-22','9395061825566995','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('6025da1df11a9d002adf6781','2021-02-22','9029469270622902','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('60273d0916ae34002a44ccff','2021-02-18','7644552249665264','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('602746a016ae34002a44cd38','2021-02-28','0398887933149100','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60274934ddcaa5002a037c86','2021-02-28','5018718009226945','US','','16029256-3','UNKNOWN','0000-00-00','O','',1),('602749b7ddcaa5002a037c8d','2021-02-15','9024514265930841','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60274a5eddcaa5002a037c94','2021-02-16','7231134358254053','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60274cd4ddcaa5002a037c9b','2021-02-22','5173949121390711','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60274d07ddcaa5002a037ca6','2021-02-22','5642190567276311','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60274d1bddcaa5002a037cab','2021-03-03','5573465710960049','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60274e88ddcaa5002a037cb2','2021-03-03','9569326787564575','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60274eacddcaa5002a037cba','2021-03-03','4826003950368630','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('6027d9f081d3e7eb9fab5ea8','2021-02-22','5480266976948350','US','','445645645','UNKNOWN','0000-00-00','O','',1),('60296a169d1636002a46e1ba','2021-02-22','4552705783243761','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60296af79d1636002a46e1c1','2021-02-15','9605728099878655','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60296e1f9d1636002a46e203','2021-02-22','2171553542400014','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60296f249d1636002a46e210','2021-03-03','4542811116824801','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('60296fe69d1636002a46e217','2021-03-03','6180792284342257','US','','345345343-2','UNKNOWN','0000-00-00','O','',1),('602bdd80859d0839d7badea0','2021-02-27','2612032350665050','US','','7787897887','UNKNOWN','0000-00-00','O','',1),('602bdf357b9ab03aa1416d30','2021-02-27','0258367173425439','US','','7787897887','UNKNOWN','0000-00-00','O','',1),('602be22590bb3c3b476586ed','2021-02-27','0568160354450792','US','','7787897887','UNKNOWN','0000-00-00','O','',1);
/*!40000 ALTER TABLE `studies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-16 16:52:02
