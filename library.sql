-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2022 at 05:22 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `genre` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `name`, `author`, `genre`) VALUES
(22, 'The 7 Habits of Highly Effective People', 'Steven Covey', 'self help book'),
(23, 'House of Leaves', 'Mark Z. Danielewski', 'horror'),
(24, 'The Haunting of Hill House', 'Shirley Jackson', 'horror'),
(25, 'The Shining', 'Stephen King', 'horror'),
(27, 'Ghost Story', 'Peter Straub', 'horror'),
(28, 'It', 'Stephen King', 'horror'),
(29, 'The Exorcist', 'William Peter Blatty', 'horror'),
(30, 'Hell House', 'Richard Matheson', 'horror'),
(31, 'Salem\'s Lot', 'Stephen King', 'horror'),
(32, 'Dracula', 'Bram Stroker', 'horror'),
(34, 'The Power of Now', 'Eckhart Tolle', 'self help book'),
(35, 'Atomic Habits', 'James Clear', 'self help book'),
(36, 'The Secret', 'Rhonda Byrne', 'self help book'),
(37, 'The 48 Laws of Power', 'Robert Greene', 'self help book'),
(38, 'Treasure Island', 'Robert Louis Stevenson', 'Adventure fiction'),
(40, 'Harry Potter and the Philosopher\'s Stone', 'J. K. Rowling', 'Adventure fiction'),
(41, 'Harry Potter and the Deathly Hallows', 'J. K. Rowling', 'Adventure fiction'),
(42, 'Harry Potter and the Goblet of Fire', 'J. K. Rowling', 'Adventure fiction'),
(43, 'Harry Potter and the Prisoner of Azkaban', 'J. K. Rowling', 'Adventure fiction'),
(44, 'Better Off Dead', 'Andrew Child ', 'Adventure fiction'),
(45, 'Billy Summers', 'Stephen King', 'Adventure fiction');

-- --------------------------------------------------------

--
-- Table structure for table `lending`
--

CREATE TABLE `lending` (
  `id` int(11) NOT NULL,
  `user_fk` int(225) NOT NULL,
  `book_fk` int(225) NOT NULL,
  `lending_date` varchar(255) NOT NULL,
  `returning_date` varchar(255) NOT NULL,
  `fine` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lending`
--

INSERT INTO `lending` (`id`, `user_fk`, `book_fk`, `lending_date`, `returning_date`, `fine`) VALUES
(11, 1, 23, '2021-12-30', '2022-01-22', '0'),
(12, 1, 29, '2021-12-31', '2022-01-18', '0'),
(13, 1, 32, '2022-01-01', '2022-01-19', NULL),
(14, 1, 31, '2022-01-01', '2022-01-19', NULL),
(15, 1, 27, '2022-01-01', '2022-01-18', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `password` varchar(255) NOT NULL,
  `adress` varchar(225) NOT NULL,
  `privilage` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `phone`, `password`, `adress`, `privilage`) VALUES
(1, 'hassan', 'hassan123@gmail.com', '03002567841', '123', 'house#61,street#2,Bahria Town, Karachi', 'student'),
(5, 'usaid', 'usaid123@gmail.com', '03008523697', '0', 'house#42,street#10,Apara, Islamabad', 'manager'),
(6, 'abdullah', 'abdullah123@gmail.com', '03007542135', '0', 'house#39,street#28,British Home, Rawalpindi', 'student'),
(7, 'hasnat', 'hasnat123@gmail.com\r\n', '03005778963', '0', 'house#51,street#80,Jamil Colony, Multan', 'student'),
(8, 'moiz', 'moiz123@gmail.com', '03219875462', '0', 'house#78,street#81,Ghauri Town, Islamabad', 'student'),
(9, 'shayad', 'shayad123@gmail.com', '03215574586', '0', 'house#66,street#9,Bahria Town, Islamabad', 'student'),
(10, 'ibrahim', 'ibrahim123@gmail.com\r\n', '03215685452', '0', 'house#41,street#79,Sadqabad, Rawalpindi', 'student'),
(11, 'saad', 'saad123@gmail.com', '03515544778', '0', 'house#32,street#33,Salman Town, Islamabad', 'student'),
(12, 'haseeb', 'haseeb123@gmail.com', '03108788951', '0', 'house#6,street59,Bahria Town, Islamabad', 'manager'),
(13, 'waqar', 'waqar123@gmail.com', '03215896523', '123', 'house#42,street#10,Apara, karachi', 'student');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `lending`
--
ALTER TABLE `lending`
  ADD PRIMARY KEY (`id`,`lending_date`),
  ADD KEY `user_fk` (`user_fk`),
  ADD KEY `book_fk` (`book_fk`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `lending`
--
ALTER TABLE `lending`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `lending`
--
ALTER TABLE `lending`
  ADD CONSTRAINT `lending_ibfk_1` FOREIGN KEY (`book_fk`) REFERENCES `books` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `lending_ibfk_2` FOREIGN KEY (`user_fk`) REFERENCES `users` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
