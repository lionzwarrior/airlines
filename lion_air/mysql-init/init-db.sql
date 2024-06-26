START TRANSACTION;

DROP TABLE IF EXISTS `airport`;
CREATE TABLE IF NOT EXISTS airport (
  id int(11) NOT NULL AUTO_INCREMENT,
  name text NOT NULL,
  location_code text NOT NULL,
  city_name text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table airport
--

INSERT INTO airport (`id`, `name`, `location_code`, `city_name`) VALUES
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
-- Table structure for table class
--

DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS class (
  id int(11) NOT NULL AUTO_INCREMENT,
  name text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table class
--

INSERT INTO class (`id`, `name`) VALUES
(1, 'Business Class'),
(2, 'Economy Class');

-- --------------------------------------------------------

--
-- Table structure for table flight
--

DROP TABLE IF EXISTS `flight`;
CREATE TABLE IF NOT EXISTS flight (
  id int(11) NOT NULL AUTO_INCREMENT,
  flight_code_id int(11) NOT NULL,
  class_id int(11) NOT NULL,
  capacity int(11) NOT NULL,
  price int(11) NOT NULL,
  date date NOT NULL,
  weight int(11) NOT NULL,
  delay int(11) NOT NULL,
  status tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table flight_code
--

DROP TABLE IF EXISTS `flight_code`;
CREATE TABLE IF NOT EXISTS flight_code (
  id int(11) NOT NULL AUTO_INCREMENT,
  flight_code text NOT NULL,
  airport_origin_id int(11) NOT NULL,
  airport_destination_id int(11) NOT NULL,
  start_time time NOT NULL,
  end_time time NOT NULL,
  status tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table flight_code
--

INSERT INTO flight_code (`id`, `flight_code`, `airport_origin_id`, `airport_destination_id`, `start_time`, `end_time`, `status`) VALUES
(1, 'JT 101', 2, 5, '11:30:00', '12:50:00', 1),
(2, 'JT 102', 5, 2, '14:00:00', '15:20:00', 1),
(3, 'JT 103', 2, 8, '16:00:00', '17:30:00', 1),
(4, 'JT 104', 8, 2, '18:00:00', '19:30:00', 1),
(5, 'JT 105', 4, 6, '08:00:00', '09:30:00', 1),
(6, 'JT 106', 6, 4, '10:00:00', '11:30:00', 1);

-- --------------------------------------------------------

--
-- Table structure for table ticket
--

DROP TABLE IF EXISTS `ticket`;
CREATE TABLE IF NOT EXISTS ticket (
  id int(11) NOT NULL AUTO_INCREMENT,
  customer_name text NOT NULL,
  flight_id int(11) NOT NULL,
  status int(11) NOT NULL,
  timestamp timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Populating flight table for the next 3 days
--

INSERT INTO flight (`id`, `flight_code_id`, `class_id`, `capacity`, `price`, `date`, `weight`, `delay`, `status`) VALUES
(1, 1, 1, 50, 3000000, '2024-06-26', 30, 0, 1),
(2, 2, 2, 200, 1500000, '2024-06-26', 25, 5, 1),
(3, 3, 1, 50, 3000000, '2024-06-26', 30, 0, 1),
(4, 4, 2, 200, 1500000, '2024-06-26', 25, 5, 1),
(5, 5, 1, 50, 3000000, '2024-06-26', 30, 0, 1),
(6, 6, 2, 200, 1500000, '2024-06-26', 25, 5, 1),
(7, 1, 1, 50, 3000000, '2024-06-27', 30, 0, 1),
(8, 2, 2, 200, 1500000, '2024-06-27', 25, 5, 1),
(9, 3, 1, 50, 3000000, '2024-06-27', 30, 0, 1),
(10, 4, 2, 200, 1500000, '2024-06-27', 25, 5, 1),
(11, 5, 1, 50, 3000000, '2024-06-27', 30, 0, 1),
(12, 6, 2, 200, 1500000, '2024-06-27', 25, 5, 1),
(13, 1, 1, 50, 3000000, '2024-06-28', 30, 0, 1),
(14, 2, 2, 200, 1500000, '2024-06-28', 25, 5, 1),
(15, 3, 1, 50, 3000000, '2024-06-28', 30, 0, 1),
(16, 4, 2, 200, 1500000, '2024-06-28', 25, 5, 1),
(17, 5, 1, 50, 3000000, '2024-06-28', 30, 0, 1),
(18, 6, 2, 200, 1500000, '2024-06-28', 25, 5, 1);

-- --------------------------------------------------------

--
-- Populating ticket table with sample data
--

INSERT INTO ticket (`id`, `customer_name`, `flight_id`, `status`, `timestamp`) VALUES
(1, 'Mr. Adi', 1, 1, '2024-06-10 08:26:46'),
(2, 'Ms. Budi', 2, 1, '2024-06-10 08:30:00'),
(3, 'Mr. Chandra', 3, 1, '2024-06-10 08:35:00'),
(4, 'Ms. Dewi', 4, 1, '2024-06-10 08:40:00'),
(5, 'Mr. Eko', 5, 1, '2024-06-10 08:45:00'),
(6, 'Ms. Farah', 6, 1, '2024-06-10 08:50:00');

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

