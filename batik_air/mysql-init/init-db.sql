START TRANSACTION;
SET time_zone = "+00:00";

DROP TABLE IF EXISTS `airport`;
CREATE TABLE IF NOT EXISTS `airport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `location_code` text NOT NULL,
  `city_name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`id`, `name`, `location_code`, `city_name`) VALUES
(1, 'Metropolitan Area', 'JKT', 'Jakarta'),
(2, 'Soekarno-Hatta Intl', 'CGK', 'Jakarta'),
(3, 'Halim Perdanakusuma', 'HLP', 'Jakarta'),
(4, 'Adisutjipto', 'JOG', 'Yogyakarta'),
(5, 'New Yogyakarta Int.', 'YIA', 'Yogyakarta'),
(6, 'Bali Airport', 'BLC', 'Bali'),
(7, 'Bali Airport', 'BAJ', 'Bali'),
(8, 'Ngurah Rai', 'DPS', 'Denpasar-Bali');

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`id`, `name`) VALUES
(1, 'Business Class'),
(2, 'Economy Class');

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
CREATE TABLE IF NOT EXISTS `flight` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flight_code_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `capacity` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `date` date NOT NULL,
  `weight` int(11) NOT NULL,
  `delay` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `flight_code`
--

DROP TABLE IF EXISTS `flight_code`;
CREATE TABLE IF NOT EXISTS `flight_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `flight_code` text NOT NULL,
  `airport_origin_id` int(11) NOT NULL,
  `airport_destination_id` int(11) NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table `flight_code`
-- Using Batik Air flight codes

INSERT INTO `flight_code` (`id`, `flight_code`, `airport_origin_id`, `airport_destination_id`, `start_time`, `end_time`, `status`) VALUES
(1, 'ID 6541', 2, 5, '11:30:00', '12:50:00', 1),
(2, 'ID 6542', 5, 2, '13:30:00', '14:50:00', 1),
(3, 'ID 6543', 3, 8, '15:30:00', '17:00:00', 1),
(4, 'ID 6544', 8, 3, '17:30:00', '19:00:00', 1),
(5, 'ID 6545', 4, 6, '19:30:00', '21:00:00', 1);

-- --------------------------------------------------------

-- Dumping data for table `flight`

INSERT INTO `flight` (`id`, `flight_code_id`, `class_id`, `capacity`, `price`, `date`, `weight`, `delay`, `status`) VALUES
(1, 1, 1, 50, 3000000, CURDATE(), 30, 0, 1),
(2, 2, 2, 60, 2000000, CURDATE(), 25, 10, 1),
(3, 3, 1, 50, 3000000, CURDATE(), 30, 0, 1),
(4, 4, 2, 60, 2000000, CURDATE(), 25, 10, 1),
(5, 5, 1, 50, 3000000, CURDATE(), 30, 0, 1),
(6, 1, 2, 60, 2000000, DATE_ADD(CURDATE(), INTERVAL 1 DAY), 25, 10, 1),
(7, 2, 1, 50, 3000000, DATE_ADD(CURDATE(), INTERVAL 1 DAY), 30, 0, 1),
(8, 3, 2, 60, 2000000, DATE_ADD(CURDATE(), INTERVAL 1 DAY), 25, 10, 1),
(9, 4, 1, 50, 3000000, DATE_ADD(CURDATE(), INTERVAL 1 DAY), 30, 0, 1),
(10, 5, 2, 60, 2000000, DATE_ADD(CURDATE(), INTERVAL 1 DAY), 25, 10, 1),
(11, 1, 1, 50, 3000000, DATE_ADD(CURDATE(), INTERVAL 2 DAY), 30, 0, 1),
(12, 2, 2, 60, 2000000, DATE_ADD(CURDATE(), INTERVAL 2 DAY), 25, 10, 1),
(13, 3, 1, 50, 3000000, DATE_ADD(CURDATE(), INTERVAL 2 DAY), 30, 0, 1),
(14, 4, 2, 60, 2000000, DATE_ADD(CURDATE(), INTERVAL 2 DAY), 25, 10, 1),
(15, 5, 1, 50, 3000000, DATE_ADD(CURDATE(), INTERVAL 2 DAY), 30, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
CREATE TABLE IF NOT EXISTS `ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_name` text NOT NULL,
  `flight_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`id`, `customer_name`, `flight_id`, `status`, `timestamp`) VALUES
(1, 'Mr. Adi', 1, 1, '2024-06-10 08:26:46'),
(2, 'Ms. Siti', 2, 1, CURRENT_TIMESTAMP),
(3, 'Mr. Budi', 3, 1, CURRENT_TIMESTAMP),
(4, 'Ms. Ayu', 4, 1, CURRENT_TIMESTAMP),
(5, 'Mr. Rudi', 5, 1, CURRENT_TIMESTAMP),
(6, 'Ms. Lina', 6, 1, CURRENT_TIMESTAMP),
(7, 'Mr. Joko', 7, 1, CURRENT_TIMESTAMP),
(8, 'Ms. Maya', 8, 1, CURRENT_TIMESTAMP),
(9, 'Mr. Ali', 9, 1, CURRENT_TIMESTAMP),
(10, 'Ms. Indah', 10, 1, CURRENT_TIMESTAMP),
(11, 'Mr. Kurniawan', 11, 1, CURRENT_TIMESTAMP),
(12, 'Ms. Wati', 12, 1, CURRENT_TIMESTAMP),
(13, 'Mr. Agung', 13, 1, CURRENT_TIMESTAMP),
(14, 'Ms. Sari', 14, 1, CURRENT_TIMESTAMP),
(15, 'Mr. Hendra', 15, 1, CURRENT_TIMESTAMP);

COMMIT;
