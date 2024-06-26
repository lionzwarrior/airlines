START TRANSACTION;

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
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`id`, `flight_code_id`, `class_id`, `capacity`, `price`, `date`, `weight`, `delay`, `status`) VALUES
(1, 1, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(2, 2, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(3, 3, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(4, 4, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(5, 5, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(6, 6, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(7, 7, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(8, 8, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(9, 9, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(10, 10, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(11, 11, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(12, 12, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(13, 13, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(14, 14, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(15, 15, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(16, 16, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(17, 17, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(18, 18, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(19, 19, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(20, 20, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(21, 21, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(22, 22, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(23, 23, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(24, 24, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(25, 25, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(26, 26, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(27, 27, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(28, 28, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(29, 29, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(30, 30, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(31, 31, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(32, 32, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(33, 33, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(34, 34, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(35, 35, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(36, 36, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(37, 37, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(38, 38, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(39, 39, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(40, 40, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(41, 41, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(42, 42, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(43, 43, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(44, 44, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(45, 45, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(46, 46, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(47, 47, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(48, 48, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(49, 49, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(50, 50, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(51, 51, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(52, 52, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(53, 53, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(54, 54, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(55, 55, 1, 30, 1000000, '2024-06-27', 30, 0, 1),
(56, 1, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(57, 2, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(58, 3, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(59, 4, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(60, 5, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(61, 6, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(62, 7, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(63, 8, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(64, 9, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(65, 10, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(66, 11, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(67, 12, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(68, 13, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(69, 14, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(70, 15, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(71, 16, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(72, 17, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(73, 18, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(74, 19, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(75, 20, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(76, 21, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(77, 22, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(78, 23, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(79, 24, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(80, 25, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(81, 26, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(82, 27, 2, 27, 500000, '2024-06-27', 25, 0, 1),
(83, 28, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(84, 29, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(85, 30, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(86, 31, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(87, 32, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(88, 33, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(89, 34, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(90, 35, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(91, 36, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(92, 37, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(93, 38, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(94, 39, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(95, 40, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(96, 41, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(97, 42, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(98, 43, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(99, 44, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(100, 45, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(101, 46, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(102, 47, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(103, 48, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(104, 49, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(105, 50, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(106, 51, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(107, 52, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(108, 53, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(109, 54, 2, 25, 500000, '2024-06-27', 25, 0, 1),
(110, 55, 2, 25, 500000, '2024-06-27', 25, 0, 1);

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
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flight_code`
--

INSERT INTO `flight_code` (`id`, `flight_code`, `airport_origin_id`, `airport_destination_id`, `start_time`, `end_time`, `status`) VALUES
(1, 'GA 01020607', 1, 2, '06:00:00', '07:00:00', 1),
(2, 'GA 01030607', 1, 3, '06:00:00', '07:00:00', 1),
(3, 'GA 01040607', 1, 4, '06:00:00', '07:00:00', 1),
(4, 'GA 01050607', 1, 5, '06:00:00', '07:00:00', 1),
(5, 'GA 01060607', 1, 6, '06:00:00', '07:00:00', 1),
(6, 'GA 01070607', 1, 7, '06:00:00', '07:00:00', 1),
(7, 'GA 01080607', 1, 8, '06:00:00', '07:00:00', 1),
(8, 'GA 02010607', 2, 1, '06:00:00', '07:00:00', 1),
(9, 'GA 02030607', 2, 3, '06:00:00', '07:00:00', 1),
(10, 'GA 02040607', 2, 4, '06:00:00', '07:00:00', 1),
(11, 'GA 02050607', 2, 5, '06:00:00', '07:00:00', 1),
(12, 'GA 02060607', 2, 6, '06:00:00', '07:00:00', 1),
(13, 'GA 02070607', 2, 7, '06:00:00', '07:00:00', 1),
(14, 'GA 02080607', 2, 8, '06:00:00', '07:00:00', 1),
(15, 'GA 03010607', 3, 1, '06:00:00', '07:00:00', 1),
(16, 'GA 03020607', 3, 2, '06:00:00', '07:00:00', 1),
(17, 'GA 03040607', 3, 4, '06:00:00', '07:00:00', 1),
(18, 'GA 03050607', 3, 5, '06:00:00', '07:00:00', 1),
(19, 'GA 03060607', 3, 6, '06:00:00', '07:00:00', 1),
(20, 'GA 03070607', 3, 7, '06:00:00', '07:00:00', 1),
(21, 'GA 03080607', 3, 8, '06:00:00', '07:00:00', 1),
(22, 'GA 04010607', 4, 1, '06:00:00', '07:00:00', 1),
(23, 'GA 04020607', 4, 2, '06:00:00', '07:00:00', 1),
(24, 'GA 04030607', 4, 3, '06:00:00', '07:00:00', 1),
(25, 'GA 04050607', 4, 5, '06:00:00', '07:00:00', 1),
(26, 'GA 04060607', 4, 6, '06:00:00', '07:00:00', 1),
(27, 'GA 04070607', 4, 7, '06:00:00', '07:00:00', 1),
(28, 'GA 04080607', 4, 8, '06:00:00', '07:00:00', 1),
(29, 'GA 05010607', 5, 1, '06:00:00', '07:00:00', 1),
(30, 'GA 05020607', 5, 2, '06:00:00', '07:00:00', 1),
(31, 'GA 05030607', 5, 3, '06:00:00', '07:00:00', 1),
(32, 'GA 05040607', 5, 4, '06:00:00', '07:00:00', 1),
(33, 'GA 05060607', 5, 6, '06:00:00', '07:00:00', 1),
(34, 'GA 05070607', 5, 7, '06:00:00', '07:00:00', 1),
(35, 'GA 05080607', 5, 8, '06:00:00', '07:00:00', 1),
(36, 'GA 06010607', 6, 1, '06:00:00', '07:00:00', 1),
(37, 'GA 06020607', 6, 2, '06:00:00', '07:00:00', 1),
(38, 'GA 06030607', 6, 3, '06:00:00', '07:00:00', 1),
(39, 'GA 06040607', 6, 4, '06:00:00', '07:00:00', 1),
(40, 'GA 06050607', 6, 5, '06:00:00', '07:00:00', 1),
(41, 'GA 06070607', 6, 7, '06:00:00', '07:00:00', 1),
(42, 'GA 06080607', 6, 8, '06:00:00', '07:00:00', 1),
(43, 'GA 07010607', 7, 1, '06:00:00', '07:00:00', 1),
(44, 'GA 07020607', 7, 2, '06:00:00', '07:00:00', 1),
(45, 'GA 07030607', 7, 3, '06:00:00', '07:00:00', 1),
(46, 'GA 07040607', 7, 4, '06:00:00', '07:00:00', 1),
(47, 'GA 07050607', 7, 5, '06:00:00', '07:00:00', 1),
(48, 'GA 07060607', 7, 6, '06:00:00', '07:00:00', 1),
(49, 'GA 07080607', 7, 8, '06:00:00', '07:00:00', 1),
(50, 'GA 08010607', 8, 1, '06:00:00', '07:00:00', 1),
(51, 'GA 08020607', 8, 2, '06:00:00', '07:00:00', 1),
(52, 'GA 08030607', 8, 3, '06:00:00', '07:00:00', 1),
(53, 'GA 08040607', 8, 4, '06:00:00', '07:00:00', 1),
(54, 'GA 08050607', 8, 5, '06:00:00', '07:00:00', 1),
(55, 'GA 08060607', 8, 6, '06:00:00', '07:00:00', 1),
(56, 'GA 08070607', 8, 7, '06:00:00', '07:00:00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
CREATE TABLE IF NOT EXISTS `ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_name` text NOT NULL,
  `flight_id` int(11) NOT NULL,
  `status` int(11) NOT NULL DEFAULT 1,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`id`, `customer_name`, `flight_id`, `status`, `timestamp`) VALUES
(1, 'Mr. Adi', 1, 1, '2024-06-10 08:26:46'),
(2, 'Adi', 1, 1, '2024-06-18 11:35:56'),
(3, 'Budi', 1, 1, '2024-06-18 11:57:25');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
