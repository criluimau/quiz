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
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionario`
--

LOCK TABLES `questionario` WRITE;
/*!40000 ALTER TABLE `questionario` DISABLE KEYS */;
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
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scheda`
--

LOCK TABLES `scheda` WRITE;
/*!40000 ALTER TABLE `scheda` DISABLE KEYS */;
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
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utente`
--

LOCK TABLES `utente` WRITE;
/*!40000 ALTER TABLE `utente` DISABLE KEYS */;
INSERT INTO `utente` VALUES (15,'admin','root');
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

-- Dump completed on 2012-01-04 13:45:05
