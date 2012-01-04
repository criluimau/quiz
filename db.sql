-- MySQL dump 10.13  Distrib 5.1.41, for debian-linux-gnu (i486)
--
-- Host: localhost    Database: quiz
-- ------------------------------------------------------
-- Server version	5.1.41-3ubuntu12.10

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `domande`
--

DROP TABLE IF EXISTS `domande`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `domande` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `testo` text NOT NULL,
  `argomento_id` int(11) NOT NULL,
  `tipo_risposta` text COMMENT 'm = multipla; 0 = ordinamento',
  `difficolta` int(11) NOT NULL COMMENT 'valore 0 min - 10max',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domande`
--

LOCK TABLES `domande` WRITE;
/*!40000 ALTER TABLE `domande` DISABLE KEYS */;
INSERT INTO `domande` VALUES (12,'Dove si trova il file delle password?',7,'m',3),(13,'Cosa fa il comando \"grep -c fine *\"',7,'m',4),(14,'Quale Ã¨ il comando per cercare gli script nella directory bin?',7,'m',5),(15,'Quale Ã¨ il comando per installare tutte le dipendenze del software?',7,'m',6),(16,'quale Ã¨ il comando per impostare la prioritÃ  di un lavoro?',7,'m',6),(17,'in quale directory si trovano i file di configurazione?',7,'m',5);
/*!40000 ALTER TABLE `domande` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materia`
--

DROP TABLE IF EXISTS `materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `argomento` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia`
--

LOCK TABLES `materia` WRITE;
/*!40000 ALTER TABLE `materia` DISABLE KEYS */;
INSERT INTO `materia` VALUES (7,'Linux'),(5,'php'),(8,'Python');
/*!40000 ALTER TABLE `materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionario`
--

DROP TABLE IF EXISTS `questionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questionario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` date NOT NULL,
  `utente_id` int(11) NOT NULL,
  `nr_max_domande` int(11) NOT NULL,
  `convalida` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionario`
--

LOCK TABLES `questionario` WRITE;
/*!40000 ALTER TABLE `questionario` DISABLE KEYS */;
INSERT INTO `questionario` VALUES (1,'2012-01-04',15,10,0),(2,'2012-01-04',16,10,0),(3,'2012-01-04',16,10,0),(4,'2012-01-04',16,10,0),(5,'2012-01-04',16,10,0),(6,'2012-01-04',16,10,0),(7,'2012-01-04',16,10,0),(8,'2012-01-04',16,10,0),(9,'2012-01-04',16,10,0),(10,'2012-01-04',16,10,0),(11,'2012-01-04',16,10,0),(12,'2012-01-04',16,10,0),(13,'2012-01-04',16,10,0),(14,'2012-01-04',16,10,0),(15,'2012-01-04',16,10,0),(16,'2012-01-04',16,10,0),(17,'2012-01-04',16,10,0),(18,'2012-01-04',16,10,0),(19,'2012-01-04',16,10,0);
/*!40000 ALTER TABLE `questionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `risposte`
--

DROP TABLE IF EXISTS `risposte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `risposte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_domanda` int(11) NOT NULL,
  `testo` text NOT NULL,
  `valore` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `risposte`
--

LOCK TABLES `risposte` WRITE;
/*!40000 ALTER TABLE `risposte` DISABLE KEYS */;
INSERT INTO `risposte` VALUES (10,12,'/etc/passw',0),(11,12,'/etc/shadow',1),(12,13,'elenca tutti i file contenuti nella directory corrente',0),(13,13,'elenca tutti i file della directory corrente che iniziano per la lettera c',0),(14,13,'elenca tutti i file nella directory corrente che contengono la parola fine',1),(15,14,'file * /bin/* | grep -i script',1),(16,14,'grep -c script /bin/*',0),(17,15,'dpkg -configure a',0),(18,15,'apt-get -f install',1),(19,16,'prty   ',0),(20,16,'nice     ',1),(21,17,'/config ',0),(22,17,'/etc  ',0),(23,17,'/boot',0),(24,17,'/etc/fstab',1);
/*!40000 ALTER TABLE `risposte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scheda`
--

DROP TABLE IF EXISTS `scheda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scheda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domanda_id` int(11) NOT NULL,
  `risposta` text NOT NULL,
  `id_utente` int(11) NOT NULL,
  `id_questionario` int(11) NOT NULL,
  `id_risposta` int(11) NOT NULL,
  `risposta_ute` tinyint(1) NOT NULL,
  `risposta_ok` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=92 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheda`
--

LOCK TABLES `scheda` WRITE;
/*!40000 ALTER TABLE `scheda` DISABLE KEYS */;
INSERT INTO `scheda` VALUES (1,16,'nice   ',16,12,20,0,1),(2,13,'elenca tutti i file contenuti nella directory corrente',16,14,12,0,0),(3,13,'elenca tutti i file della directory corrente che iniziano per la lettera c',16,14,13,0,0),(4,13,'elenca tutti i file nella directory corrente che contengono la parola fine',16,14,14,0,1),(5,15,'dpkg -configure a',16,14,17,0,0),(6,15,'apt-get -f install',16,14,18,0,1),(7,16,'prty   ',16,14,19,0,0),(8,16,'nice     ',16,14,20,0,1),(9,14,'file * /bin/* | grep -i script',16,14,15,0,1),(10,14,'grep -c script /bin/*',16,14,16,0,0),(11,17,'/config ',16,14,21,0,0),(12,17,'/etc  ',16,14,22,0,0),(13,17,'/boot',16,14,23,0,0),(14,17,'/etc/fstab',16,14,24,0,1),(15,12,'/etc/passw',16,14,10,0,0),(16,12,'/etc/shadow',16,14,11,0,1),(17,17,'/config ',16,15,21,0,0),(18,17,'/etc  ',16,15,22,0,0),(19,17,'/boot',16,15,23,0,0),(20,17,'/etc/fstab',16,15,24,0,1),(21,13,'elenca tutti i file contenuti nella directory corrente',16,15,12,0,0),(22,13,'elenca tutti i file della directory corrente che iniziano per la lettera c',16,15,13,0,0),(23,13,'elenca tutti i file nella directory corrente che contengono la parola fine',16,15,14,0,1),(24,12,'/etc/passw',16,15,10,0,0),(25,12,'/etc/shadow',16,15,11,0,1),(26,15,'dpkg -configure a',16,15,17,0,0),(27,15,'apt-get -f install',16,15,18,0,1),(28,14,'file * /bin/* | grep -i script',16,15,15,0,1),(29,14,'grep -c script /bin/*',16,15,16,0,0),(30,16,'prty   ',16,15,19,0,0),(31,16,'nice     ',16,15,20,0,1),(32,15,'dpkg -configure a',16,16,17,0,0),(33,15,'apt-get -f install',16,16,18,1,1),(34,16,'prty   ',16,16,19,0,0),(35,16,'nice     ',16,16,20,1,1),(36,13,'elenca tutti i file contenuti nella directory corrente',16,16,12,0,0),(37,13,'elenca tutti i file della directory corrente che iniziano per la lettera c',16,16,13,0,0),(38,13,'elenca tutti i file nella directory corrente che contengono la parola fine',16,16,14,1,1),(39,14,'file * /bin/* | grep -i script',16,16,15,1,1),(40,14,'grep -c script /bin/*',16,16,16,0,0),(41,17,'/config ',16,16,21,0,0),(42,17,'/etc  ',16,16,22,0,0),(43,17,'/boot',16,16,23,0,0),(44,17,'/etc/fstab',16,16,24,1,1),(45,12,'/etc/passw',16,16,10,0,0),(46,12,'/etc/shadow',16,16,11,1,1),(47,14,'file * /bin/* | grep -i script',16,17,15,0,1),(48,14,'grep -c script /bin/*',16,17,16,0,0),(49,12,'/etc/passw',16,17,10,0,0),(50,12,'/etc/shadow',16,17,11,0,1),(51,17,'/config ',16,17,21,0,0),(52,17,'/etc  ',16,17,22,0,0),(53,17,'/boot',16,17,23,0,0),(54,17,'/etc/fstab',16,17,24,0,1),(55,13,'elenca tutti i file contenuti nella directory corrente',16,17,12,0,0),(56,13,'elenca tutti i file della directory corrente che iniziano per la lettera c',16,17,13,0,0),(57,13,'elenca tutti i file nella directory corrente che contengono la parola fine',16,17,14,0,1),(58,16,'prty   ',16,17,19,0,0),(59,16,'nice     ',16,17,20,0,1),(60,15,'dpkg -configure a',16,17,17,0,0),(61,15,'apt-get -f install',16,17,18,0,1),(62,12,'/etc/passw',16,18,10,0,0),(63,12,'/etc/shadow',16,18,11,1,1),(64,15,'dpkg -configure a',16,18,17,0,0),(65,15,'apt-get -f install',16,18,18,1,1),(66,16,'prty   ',16,18,19,0,0),(67,16,'nice     ',16,18,20,1,1),(68,14,'file * /bin/* | grep -i script',16,18,15,1,1),(69,14,'grep -c script /bin/*',16,18,16,0,0),(70,13,'elenca tutti i file contenuti nella directory corrente',16,18,12,0,0),(71,13,'elenca tutti i file della directory corrente che iniziano per la lettera c',16,18,13,0,0),(72,13,'elenca tutti i file nella directory corrente che contengono la parola fine',16,18,14,1,1),(73,17,'/config ',16,18,21,0,0),(74,17,'/etc  ',16,18,22,0,0),(75,17,'/boot',16,18,23,0,0),(76,17,'/etc/fstab',16,18,24,1,1),(77,13,'elenca tutti i file contenuti nella directory corrente',16,19,12,0,0),(78,13,'elenca tutti i file della directory corrente che iniziano per la lettera c',16,19,13,0,0),(79,13,'elenca tutti i file nella directory corrente che contengono la parola fine',16,19,14,1,1),(80,14,'file * /bin/* | grep -i script',16,19,15,1,1),(81,14,'grep -c script /bin/*',16,19,16,0,0),(82,12,'/etc/passw',16,19,10,0,0),(83,12,'/etc/shadow',16,19,11,1,1),(84,16,'prty   ',16,19,19,0,0),(85,16,'nice     ',16,19,20,1,1),(86,15,'dpkg -configure a',16,19,17,0,0),(87,15,'apt-get -f install',16,19,18,1,1),(88,17,'/config ',16,19,21,0,0),(89,17,'/etc  ',16,19,22,0,0),(90,17,'/boot',16,19,23,0,0),(91,17,'/etc/fstab',16,19,24,1,1);
/*!40000 ALTER TABLE `scheda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utente`
--

DROP TABLE IF EXISTS `utente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `utente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` text NOT NULL,
  `pass` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utente`
--

LOCK TABLES `utente` WRITE;
/*!40000 ALTER TABLE `utente` DISABLE KEYS */;
INSERT INTO `utente` VALUES (15,'admin','root'),(16,'mau','mu');
/*!40000 ALTER TABLE `utente` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-01-04 18:00:00
