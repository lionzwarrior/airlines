-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 15, 2024 at 05:06 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `airline`
--
CREATE DATABASE IF NOT EXISTS `airline` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `airline`;

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
CREATE TABLE IF NOT EXISTS `airport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`id`, `name`) VALUES
(1, 'Jakarta Airport'),
(2, 'Juanda Airport'),
(3, 'Russian Airport'),
(4, 'German Airport'),
(5, 'Chinese Airport'),
(6, 'America Airport');

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`id`, `name`) VALUES
(1, 'First Class'),
(2, 'Business Class'),
(3, 'Economy Class');

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
CREATE TABLE IF NOT EXISTS `flight` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_type` int(11) NOT NULL,
  `airport_origin` int(11) NOT NULL,
  `airport_destination` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `class_fk` (`class_type`),
  KEY `airport_origin_fk` (`airport_origin`),
  KEY `airport_destination_fk` (`airport_destination`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`id`, `class_type`, `airport_origin`, `airport_destination`, `capacity`, `price`) VALUES
(1, 1, 1, 3, 50, 2000000),
(2, 2, 2, 4, 30, 1500000);

-- --------------------------------------------------------

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
CREATE TABLE IF NOT EXISTS `reservation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ticket_id` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `ticket_fk` (`ticket_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reservation`
--

INSERT INTO `reservation` (`id`, `ticket_id`, `timestamp`) VALUES
(1, 1, '2024-05-15 08:43:47'),
(2, 1, '2024-05-15 10:27:39'),
(3, 1, '2024-05-15 10:27:43');

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
CREATE TABLE IF NOT EXISTS `ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flight_type` int(11) NOT NULL,
  `start_datetime` datetime NOT NULL,
  `end_datetime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `flight_type` (`flight_type`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`id`, `flight_type`, `start_datetime`, `end_datetime`) VALUES
(1, 1, '2024-05-15 18:00:00', '2024-05-15 20:00:00'),
(2, 2, '2024-05-16 18:00:00', '2024-05-16 20:00:00');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `airport_destination_fk` FOREIGN KEY (`airport_destination`) REFERENCES `airport` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `airport_origin_fk` FOREIGN KEY (`airport_origin`) REFERENCES `airport` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `class_fk` FOREIGN KEY (`class_type`) REFERENCES `class` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `reservation`
--
ALTER TABLE `reservation`
  ADD CONSTRAINT `ticket_fk` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`id`) ON UPDATE CASCADE;

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `flight_type` FOREIGN KEY (`flight_type`) REFERENCES `flight` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
