-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 03, 2020 at 05:41 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatbot_final`
--

-- --------------------------------------------------------

--
-- Table structure for table `infotable`
--

CREATE TABLE `infotable` (
  `question` varchar(300) DEFAULT NULL,
  `anstype1` varchar(300) DEFAULT NULL,
  `anstype2` varchar(300) DEFAULT NULL,
  `anstype3` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `infotable`
--

INSERT INTO `infotable` (`question`, `anstype1`, `anstype2`, `anstype3`) VALUES
('what is coronavirus disease 2019', 'Coronavirus disease 2019 is a respiratory illness that can spread from person to person', 'COVID 19 is a new disease caused by a novel that has not previously been seen in humans', 'It is an new virus which was found out in early 2020'),
('how can i prevent covid 19', 'The best way to prevent illness is to avoid being exposed to the virus', 'cdc recommends everyday preventive actions to help prevent the spread of respiratory diseases', 'CDC recommends washing your hands often with soap and water for at least 20 seconds especially after you have been in a public place'),
('how does covid 19 spread', 'covid 19 is thought to spread mainly through close contact from person to person', 'We are still learning about how the virus spreads and the severity of illness it causes', 'it is known to spread through physical contact between the person to person'),
('should i wear a face mask when i go out in public', 'yes it is recommended to use face mask when going outside', 'cdc recommends wearing cloth face coverings in public when exposed to atmosphere', 'wearing face mask ensures your own safety so please do wear it'),
('what treatments are available for covid 19', 'currently there are no fda approved medicines specifically for covid 19', 'the research for the vaccine is still going on', 'the research for the vaccine is still going on'),
('is hand sanitizer effective against covid 19', 'yes it is proven that hand sanitizer are effective in slowing down the spread of covid-19', 'use of sanitizer is effective against covid-19 ', 'it is recommended to use hand sanitizer when going outside'),
('can i make my own hand sanetizer', 'The FDA does not recommend that consumers make their own hand sanitizer', 'If made incorrectly hand sanitizer can be ineffective', 'yes you can but there have been reports of skin burns from homemade hand sanitizer so be carefull'),
('Is it safe for me to donate blood during the coronavirus pandemic', 'yes you can donate blood if you are healthy and not suffering from disease', 'yes you can donate blood if you are healthy and not suffering from disease', 'yes you can donate blood if you are healthy and not suffering from disease'),
('how are people tested for covid 19', 'In general for diagnostic tests samples are collected from a persons nose andor throat using swabs and tests are done', 'In general for diagnostic tests samples are collected from a persons nose andor throat using swabs and tests are done', 'In general for diagnostic tests samples are collected from a persons nose andor throat using swabs and tests are done'),
('hello', 'Hello iam  a chatbot', 'Hello sir or maam', 'Today i welcome you'),
('hello how are you', 'Hello iam  a chatbot', 'Hello sir or maam', 'Today i welcome you'),
('good day', 'thankyou', 'same to you', 'have a nice day'),
('how are you', 'Hello i am fine thankyou for asking ', 'Hello sir or mam what can i do for you', 'Today is a nice day'),
('nice to meet you', 'nice to meet you too', 'nice to meet you too', 'nice to meet you too'),
('what is iot', 'It is the network of devices vehicles and home appliances that contain electronics software actuators and connectivity which allows these things to connect interact and exchange data', 'It is the network of devices vehicles and home appliances that contain electronics software actuators and connectivity which allows these things to connect interact and exchange data', 'It is the network of devices vehicles and home appliances that contain electronics software actuators and connectivity which allows these things to connect interact and exchange data'),
('what is bioinformatics', 'It is interdisciplinary field that develops methods and software tools for understanding biological data', 'It is interdisciplinary field that develops methods and software tools for understanding biological data', 'It is interdisciplinary field that develops methods and software tools for understanding biological data'),
('what is cyber security', 'It is the protection of computer systems from theft or damage to their hardware, software or electronic data', 'It is the protection of computer systems from theft or damage to their hardware, software or electronic data', 'It is the protection of computer systems from theft or damage to their hardware, software or electronic data'),
('clear', 'cleared the screen', 'cleared the screen', 'cleared the screen'),
('what is virtual reality', 'The Computer-generated simulation of a three-dimensional image or environment that can be interacted with in a seemingly real or physical way by a person using special electronic equipment', 'The Computer-generated simulation of a three-dimensional image or environment that can be interacted with in a seemingly real or physical way by a person using special electronic equipment', 'The Computer-generated simulation of a three-dimensional image or environment that can be interacted with in a seemingly real or physical way by a person using special electronic equipment'),
('what is virtual assistant', 'It is Software Agent that can perform tasks or services for an individual', 'It is Software Agent that can perform tasks or services for an individual', 'It is Software Agent that can perform tasks or services for an individual'),
('what is computer assisted education', 'The use of Computers to aid or support education or training of people', 'The use of Computers to aid or support education or training of people', 'The use of Computers to aid or support education or training of people'),
('who are you', 'i am elsa nice to meet you', 'my name is elsa user friendly bot', 'everyones loves elsa'),
('are you a machine', 'yes but i am smart machine', 'no i am elsa but yes i am a machine', 'i stay above all the machines in the world');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `contact_no` int(11) DEFAULT NULL,
  `plan` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`firstname`, `lastname`, `email`, `password`, `contact_no`, `plan`) VALUES
('sunil', 'pattar', 'sunilpattar99@gmail.com', '123456', 109, 'free'),
('soumya', 'bhadani', '123.soumyabhadani@gmail.com', '123456', 108, 'free'),
('anna', 'smith', 'anna@gmail.com', 'anna123', 899, 'free'),
('pratik', 'kumbhar', 'pratik@gmail.com', '123456', 789, 'free'),
('bipin', 'bangera', 'bipin123', 'bipin123', 213, 'free');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
