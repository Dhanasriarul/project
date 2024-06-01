-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 05, 2023 at 11:58 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `oneyesinfotechsolutions`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `categoryId` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `image` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`categoryId`, `name`, `image`) VALUES
(1, 'Restaurant2', 'https://assets.gqindia.com/photos/62a9d4653e8cdc9b632eb2ad/16:9/w_1920,h_1080,c_limit/10%20restaurants%20in%20Mumbai%20that%20offer%20the%20best%20sunset%20views.jpg'),
(3, 'Business', 'https://images.unsplash.com/photo-1665686310934-8fab52b3821b');

-- --------------------------------------------------------

--
-- Table structure for table `enquiries`
--

CREATE TABLE `enquiries` (
  `enquiryId` bigint(20) NOT NULL,
  `serviceId` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `enquiries`
--

INSERT INTO `enquiries` (`enquiryId`, `serviceId`, `name`, `email`, `phone`, `message`) VALUES
(1, 5, 'Yugi', 'yyugi64@gmail.com', '8838669898', 'asdadnasdn');

-- --------------------------------------------------------

--
-- Table structure for table `gallery`
--

CREATE TABLE `gallery` (
  `galleryId` bigint(20) NOT NULL,
  `serviceId` bigint(20) NOT NULL,
  `image` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gallery`
--

INSERT INTO `gallery` (`galleryId`, `serviceId`, `image`) VALUES
(2, 3, 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg'),
(3, 5, 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg'),
(4, 5, 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `reviewId` bigint(20) NOT NULL,
  `serviceId` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `rating` int(15) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reviews`
--

INSERT INTO `reviews` (`reviewId`, `serviceId`, `name`, `rating`, `message`) VALUES
(1, 1, 'Yugi', 3, 'Test'),
(2, 1, 'Yugi', 4, 'Test'),
(3, 2, 'Yugi', 5, 'Test'),
(4, 3, 'Yugi', 1, 'Test'),
(5, 1, 'Yugendiran', 4, 'Test msg'),
(6, 2, 'Yugi', 5, 'asdasd'),
(7, 2, 'Yugi', 4, 'asd'),
(8, 1, 'Yugi', 5, 'asd'),
(9, 6, 'yugi', 5, 'asd');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `serviceId` bigint(20) NOT NULL,
  `categoryId` bigint(20) NOT NULL,
  `image` text NOT NULL,
  `title` text NOT NULL,
  `impressions` int(11) NOT NULL,
  `address` text NOT NULL,
  `city` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`serviceId`, `categoryId`, `image`, `title`, `impressions`, `address`, `city`, `phone`, `email`) VALUES
(1, 1, 'https://imageio.forbes.com/specials-images/imageserve/61d52d4e3a76ed81ac034ea8/0x0.jpg', 'Test 1', 0, 'Address', 'chennai', '9112233449', 'yyugi64@gmail.com'),
(3, 1, 'https://imageio.forbes.com/specials-images/imageserve/61d52d4e3a76ed81ac034ea8/0x0.jpg', 'Test 3', 200, 'Address3', 'bangalore', '9112233449', ''),
(5, 1, 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg', 'Hello', 6, 'Address', 'mumbai', '9112233449', 'yyugi64@gmail.com'),
(6, 1, 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg', 'Hello', 0, 'Address', 'mumbai', '9112233449', 'yyugi64@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `userId` bigint(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `gender` varchar(15) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`userId`, `name`, `email`, `phone`, `dob`, `gender`, `password`) VALUES
(1, 'Yugendiran G', 'yyugi64@gmail.com', '', '', '', 'Yugi@GB2810');

-- --------------------------------------------------------

--
-- Table structure for table `visits`
--

CREATE TABLE `visits` (
  `visitId` bigint(20) NOT NULL,
  `page` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `visits`
--

INSERT INTO `visits` (`visitId`, `page`) VALUES
(1, 'home'),
(2, 'home'),
(3, 'home'),
(4, 'home'),
(5, 'home'),
(6, 'home'),
(7, 'home'),
(8, 'home'),
(9, 'home'),
(10, 'home'),
(11, 'home'),
(12, 'home'),
(13, 'home'),
(14, 'home'),
(15, 'home');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`categoryId`);

--
-- Indexes for table `enquiries`
--
ALTER TABLE `enquiries`
  ADD PRIMARY KEY (`enquiryId`);

--
-- Indexes for table `gallery`
--
ALTER TABLE `gallery`
  ADD PRIMARY KEY (`galleryId`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`reviewId`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`serviceId`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userId`);

--
-- Indexes for table `visits`
--
ALTER TABLE `visits`
  ADD PRIMARY KEY (`visitId`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `categoryId` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `enquiries`
--
ALTER TABLE `enquiries`
  MODIFY `enquiryId` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `gallery`
--
ALTER TABLE `gallery`
  MODIFY `galleryId` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `reviews`
--
ALTER TABLE `reviews`
  MODIFY `reviewId` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `serviceId` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `userId` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `visits`
--
ALTER TABLE `visits`
  MODIFY `visitId` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
