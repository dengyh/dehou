-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2014 年 09 月 12 日 06:58
-- 服务器版本: 5.6.12-log
-- PHP 版本: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `dehou_v1`
--
CREATE DATABASE IF NOT EXISTS `dehou_v1` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
USE `dehou_v1`;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=49 ;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add user info', 7, 'add_userinfo'),
(20, 'Can change user info', 7, 'change_userinfo'),
(21, 'Can delete user info', 7, 'delete_userinfo'),
(22, 'Can add nav', 8, 'add_nav'),
(23, 'Can change nav', 8, 'change_nav'),
(24, 'Can delete nav', 8, 'delete_nav'),
(25, 'Can add news', 9, 'add_news'),
(26, 'Can change news', 9, 'change_news'),
(27, 'Can delete news', 9, 'delete_news'),
(28, 'Can add job', 10, 'add_job'),
(29, 'Can change job', 10, 'change_job'),
(30, 'Can delete job', 10, 'delete_job'),
(31, 'Can add resume', 11, 'add_resume'),
(32, 'Can change resume', 11, 'change_resume'),
(33, 'Can delete resume', 11, 'delete_resume'),
(34, 'Can add comments', 12, 'add_comments'),
(35, 'Can change comments', 12, 'change_comments'),
(36, 'Can delete comments', 12, 'delete_comments'),
(37, 'Can add message', 13, 'add_message'),
(38, 'Can change message', 13, 'change_message'),
(39, 'Can delete message', 13, 'delete_message'),
(40, 'Can add feedback', 14, 'add_feedback'),
(41, 'Can change feedback', 14, 'change_feedback'),
(42, 'Can delete feedback', 14, 'delete_feedback'),
(43, 'Can add advantages', 15, 'add_advantages'),
(44, 'Can change advantages', 15, 'change_advantages'),
(45, 'Can delete advantages', 15, 'delete_advantages'),
(46, 'Can add page_keywords', 16, 'add_page_keywords'),
(47, 'Can change page_keywords', 16, 'change_page_keywords'),
(48, 'Can delete page_keywords', 16, 'delete_page_keywords');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `email` varchar(75) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=4 ;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$10000$c9WhqTUux4xy$042oTsyCr7/gS6kf+X5+e/2vFGFxHy/0jT4nrUM2VXI=', '2014-09-10 06:15:57', 1, 'admin', '超级管理员', '', '', 1, 1, '2014-08-29 03:15:15'),
(2, 'pbkdf2_sha256$10000$ml9tfmfhI1oB$xCvwwrG3QH0eDFgZ1KfU0bseYd5SnV/0UDj0hA4q8vg=', '2014-08-29 06:12:41', 0, 'yoyo', 'yoyo', '', '', 0, 1, '2014-08-29 06:12:41'),
(3, 'pbkdf2_sha256$10000$V5GQT25Kdotb$YneEZXv5UxG/zNwBzVIrYP9hcrs1ofKcRoQ/G48BE7g=', '2014-09-05 12:28:25', 0, 'aa', 'aa', '', '', 0, 1, '2014-09-05 12:28:25');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `backend_advantages`
--

CREATE TABLE IF NOT EXISTS `backend_advantages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `problem` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `big_title` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `big_title_en` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `title1` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `title1_en` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `title2` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `title2_en` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `solution1` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `solution2` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `solution3` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `solution4` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `problem_en` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `solution1_en` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `solution2_en` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `solution3_en` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  `solution4_en` varchar(120) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=7 ;

--
-- 转存表中的数据 `backend_advantages`
--

INSERT INTO `backend_advantages` (`id`, `problem`, `big_title`, `big_title_en`, `title1`, `title1_en`, `title2`, `title2_en`, `solution1`, `solution2`, `solution3`, `solution4`, `problem_en`, `solution1_en`, `solution2_en`, `solution3_en`, `solution4_en`) VALUES
(1, '第一个问题', 'AAAAAAAAAAA', 'AAAAAAAAAAA', 'AAAAAAAAAA', 'AAAAAAAAAAAA', 'AAAAAAAAAA', 'AAAAAAAAAAAA', 'AAAA', 'AAAAAAAAAAA', 'AAAAAAAAAAAAA', 'AAAAAAAAAAAAA', 'AAAAAAAAAAAAAA', 'AAAAAAAAAAAAAA', 'AAAAAAAAAAA', 'AAAAAAAAAAAAA', 'AAAAAAAAAAAAAAA'),
(2, '第二个问题', 'BBBBBBBBBB', 'BBBBBBBBBBB', 'BBBBBBB', 'BBBBBBBB', 'BBBBBBBBBBBBB', 'BBBBBBBBBB', 'BBBBBBBB', 'BBBBBBBBBB', 'BBBBBBBBBB', 'BBBBBBBBBBBB', 'BBBBBBBBBBB', 'BBBBBBBB', 'BBBBBBBBBBBB', 'BBBBBBBBB', 'BBBBBBBBBB'),
(3, '第三个问题 ', 'CCCCCCCCCCC', 'CCCCCCCC', 'CCCCCCCC', 'CCCCCCCCCCC', 'CCCCCCCC', 'CCCCCCCCCCCC', 'CCCCCCCCC', 'CCCCCCCCCC', 'CCCCCCCCCCCCC', 'CCCCCCCCCCCC', 'CCCCCCCCCC', 'CCCCCCCCCCC', 'CCCCCCCCCCCCC', 'CCCCCCCCCCCC', 'CCCCCCCCCCCCC'),
(4, '第四个问题', 'DDDDDDDDDD', 'DDDDDDDDDDDD', 'DDDDDDDDDD', 'DDDDDDDDDDD', 'DDDDDDDDDDDDDD', 'DDDDDDDDDDDDD', 'DDDDDDDD', 'DDDDDDDD', 'DDDDDDDDDDDD', 'DDDDDDDDDD', 'DDDDDDDDDDDDD', 'DDDDDDDDDDD', 'DDDDDDDDDDD', 'DDDDDDDDDD', 'DDDDDDDDDDDDDD'),
(5, '第五个问题', 'EEEEEEEEEEE', 'EEEEEEEEEE', 'EEEEEEEEEEEE', 'EEEEEEEEEEEEEEEE', 'EEEEEEEEEEE', 'EEEEEEEEEEEEE', 'EEEEEEEEEEE', 'EEEEEEEEEEEE', 'EEEEEEEEEEEEEE', 'EEEEEEEEEEEE', 'EEEEEEEEEEEEEEEE', 'EEEEEEEEEEEEEEEE', 'EEEEEEEEEEEEEE', 'EEEEEEEEEEEEEE', 'EEEEEEEEEEEEEEEE'),
(6, '第六个问题', 'FFFFFFFFFFFF', 'FFFFFFFFFFF', 'FFFFFFFFF', 'FFFFFFFFF', 'FFFFFFFFFFFFF', 'FFFFFFFFFFFFF', 'FFFFFFFFFFFFFF', 'FFFFFFFFFFFFF', 'FFFFFFFFFFFFFFFFF', 'FFFFFFFFFFFFFFFFFF', 'FFFFFFFFFFFFFF', 'FFFFFFFFFFFFFF', 'FFFFFFFFFFFFF', 'FFFFFFFFFFFFFF', 'FFFFFFFFFFFFFFFFF');

-- --------------------------------------------------------

--
-- 表的结构 `backend_comments`
--

CREATE TABLE IF NOT EXISTS `backend_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_bin NOT NULL,
  `title` varchar(100) COLLATE utf8_bin NOT NULL,
  `content` longtext COLLATE utf8_bin NOT NULL,
  `send_time` datetime NOT NULL,
  `admin` varchar(20) COLLATE utf8_bin NOT NULL,
  `replay_content` longtext COLLATE utf8_bin NOT NULL,
  `replay_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `backend_job`
--

CREATE TABLE IF NOT EXISTS `backend_job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position` varchar(20) COLLATE utf8_bin NOT NULL,
  `position_en` varchar(20) COLLATE utf8_bin NOT NULL,
  `content` longtext COLLATE utf8_bin NOT NULL,
  `content_en` longtext COLLATE utf8_bin NOT NULL,
  `datetime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `backend_nav`
--

CREATE TABLE IF NOT EXISTS `backend_nav` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_bin NOT NULL,
  `name_en` varchar(20) COLLATE utf8_bin NOT NULL,
  `pid_id` int(11) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `title` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `title_en` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `keywords` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `keywords_en` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `description` varchar(256) COLLATE utf8_bin DEFAULT NULL,
  `description_en` varchar(256) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `backend_nav_664e8aab` (`pid_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=48 ;

--
-- 转存表中的数据 `backend_nav`
--

INSERT INTO `backend_nav` (`id`, `name`, `name_en`, `pid_id`, `level`, `title`, `title_en`, `keywords`, `keywords_en`, `description`, `description_en`) VALUES
(1, '首页', '首页_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '佳易得产品', '佳易得产品_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '工程应用', '工程应用_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(4, '核心技术', '核心技术_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(5, '荣誉与资质', '荣誉与资质_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(6, '共赢专区', '共赢专区_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(7, '德厚新闻', '德厚新闻_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(8, '关于德厚', '关于德厚_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(9, '联系德厚', '联系德厚_en', NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL),
(10, '玻璃隔热涂膜', '玻璃隔热涂膜_en', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(11, '建筑玻璃应用', '建筑玻璃应用_en', 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(12, '其它玻璃应用', '其它玻璃应用_en', 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(13, '隔热中空玻璃', '隔热中空玻璃', 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(14, '墙体材料', '墙体材料_en', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(15, '内墙涂料', '内墙涂料_en', 14, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(16, '外墙涂料', '外墙涂料_en', 14, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17, '墙体防水涂料', '墙体防水涂料_en', 14, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(18, '最新工程', '最新工程_en', 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(19, '家庭项目', '家庭项目_en', 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(20, '办公项目', '办公项目_en', 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(21, '工程项目', '工程项目_en', 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(22, '技术研发', '技术研发_en', 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(23, '博士团队', '博士团队_en', 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(24, '施工团队', '施工团队_en', 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(25, '半自动淋涂设备', '半自动淋涂设备_en', 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(26, '全自动生产线', '全自动生产线_en', 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(27, '专利证书', '专利证书_en', 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(28, '荣誉奖项', '荣誉奖项_en', 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(29, '国家标准、行业标准', '国家标准_en', 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(30, '检测报告', '检测报告_en', 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(31, '合作伙伴', '合作伙伴_en', 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(32, '代理加盟', '代理加盟_en', 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(33, '工程项目合作', '工程项目合作_en', 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(34, '旗舰店', '旗舰店_en', 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(35, '合同能源管理（EMC）', 'EMC_en', 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(36, '公司动态', '公司动态_en', 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(37, '行业新闻', '行业新闻_en', 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(38, '节能科普小知识', '节能科普小知识', 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(39, '德厚简介', '德厚简介_en', 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(40, '商标释义', '商标释义_en', 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(41, '总经理介绍和致辞', '总经理介绍和致辞_en', 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(42, '公司实力', '公司实力_en', 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(43, '人才资源', '人才资源_en', 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(44, '人才理念', '人才理念_en', 43, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(45, '成长空间', '成长空间_en', 43, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(46, '职位信息', '职位信息_en', 43, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(47, '合作伙伴', '合作伙伴_en', 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `backend_news`
--

CREATE TABLE IF NOT EXISTS `backend_news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_id` int(11) NOT NULL,
  `s_id` int(11) DEFAULT NULL,
  `t_id` int(11) DEFAULT NULL,
  `page_title` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `page_title_en` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `page_keywords` varchar(256) COLLATE utf8_bin NOT NULL,
  `page_keywords_en` varchar(256) COLLATE utf8_bin DEFAULT NULL,
  `page_description` varchar(256) COLLATE utf8_bin NOT NULL,
  `page_description_en` varchar(256) COLLATE utf8_bin DEFAULT NULL,
  `title` varchar(150) COLLATE utf8_bin DEFAULT NULL,
  `title_en` varchar(150) COLLATE utf8_bin DEFAULT NULL,
  `remark` varchar(150) COLLATE utf8_bin DEFAULT NULL,
  `remark_en` varchar(150) COLLATE utf8_bin DEFAULT NULL,
  `url` varchar(150) COLLATE utf8_bin DEFAULT NULL,
  `url_en` varchar(150) COLLATE utf8_bin DEFAULT NULL,
  `img` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `content` longtext COLLATE utf8_bin NOT NULL,
  `content_en` longtext COLLATE utf8_bin NOT NULL,
  `datetime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `backend_page_keywords`
--

CREATE TABLE IF NOT EXISTS `backend_page_keywords` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nav_id` int(11) NOT NULL,
  `title` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `title_en` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `keywords` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `keywords_en` varchar(128) COLLATE utf8_bin DEFAULT NULL,
  `description` varchar(256) COLLATE utf8_bin DEFAULT NULL,
  `description_en` varchar(256) COLLATE utf8_bin DEFAULT NULL,
  `datetime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `backend_resume`
--

CREATE TABLE IF NOT EXISTS `backend_resume` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8_bin NOT NULL,
  `position` varchar(20) COLLATE utf8_bin NOT NULL,
  `degree` varchar(20) COLLATE utf8_bin NOT NULL,
  `files` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `datetime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `backend_userinfo`
--

CREATE TABLE IF NOT EXISTS `backend_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `premissions` varchar(30) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=4 ;

--
-- 转存表中的数据 `backend_userinfo`
--

INSERT INTO `backend_userinfo` (`id`, `user_id`, `premissions`) VALUES
(1, 1, '1,2,3,4,5,6,7,'),
(2, 2, '1,2,3,5,6,'),
(3, 3, '1,2,');

-- --------------------------------------------------------

--
-- 表的结构 `chat_feedback`
--

CREATE TABLE IF NOT EXISTS `chat_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customID` varchar(128) COLLATE utf8_bin NOT NULL,
  `isDisplay` tinyint(1) NOT NULL,
  `content` varchar(256) COLLATE utf8_bin NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=6 ;

--
-- 转存表中的数据 `chat_feedback`
--

INSERT INTO `chat_feedback` (`id`, `customID`, `isDisplay`, `content`, `time`) VALUES
(1, 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', 1, '你也是  逗比', '2014-09-03 09:21:40'),
(2, 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', 1, '你 没啊', '2014-09-03 09:21:57'),
(3, 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', 1, 'dfasdfdsf', '2014-09-03 09:30:53'),
(4, 'f1d0cc21-335f-11e4-9cc7-206a8a5d2ed1', 1, '你大爷', '2014-09-03 12:32:23'),
(5, 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 1, '点点滴滴', '2014-09-05 04:05:34');

-- --------------------------------------------------------

--
-- 表的结构 `chat_message`
--

CREATE TABLE IF NOT EXISTS `chat_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `isDisplay` tinyint(1) NOT NULL,
  `content` varchar(256) COLLATE utf8_bin NOT NULL,
  `customID` varchar(128) COLLATE utf8_bin NOT NULL,
  `name` varchar(16) COLLATE utf8_bin NOT NULL,
  `phone` varchar(16) COLLATE utf8_bin NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=24 ;

--
-- 转存表中的数据 `chat_message`
--

INSERT INTO `chat_message` (`id`, `isDisplay`, `content`, `customID`, `name`, `phone`, `time`) VALUES
(1, 1, '个', 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', '范德萨', '飞洒', '2014-09-03 09:18:33'),
(2, 1, '你才是逗比', 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', '范德萨', '飞洒', '2014-09-03 09:21:49'),
(3, 1, '你大爷 啊', 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', '范德萨', '飞洒', '2014-09-03 09:22:06'),
(4, 1, '靠 你打', 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', '范德萨', '飞洒', '2014-09-03 09:22:09'),
(5, 1, '靠', 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', '范德萨', '飞洒', '2014-09-03 09:23:07'),
(6, 1, '大大的擦  ', 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', '范德萨', '飞洒', '2014-09-03 10:09:55'),
(7, 1, '打算', 'f90f8d61-334a-11e4-a65d-206a8a5d2ed1', '范德萨', '飞洒', '2014-09-03 10:10:15'),
(8, 1, 'd', 'f1d0cc21-335f-11e4-9cc7-206a8a5d2ed1', 'ddd', 'x', '2014-09-03 11:50:47'),
(9, 1, 'j', 'f1d0cc21-335f-11e4-9cc7-206a8a5d2ed1', 'ddd', 'x', '2014-09-03 11:50:50'),
(10, 1, 'j', 'f1d0cc21-335f-11e4-9cc7-206a8a5d2ed1', 'ddd', 'x', '2014-09-03 11:50:52'),
(11, 1, 'f', 'f1d0cc21-335f-11e4-9cc7-206a8a5d2ed1', 'ddd', 'x', '2014-09-03 12:13:06'),
(12, 1, 'fdsfsd', 'f1d0cc21-335f-11e4-9cc7-206a8a5d2ed1', 'ddd', 'x', '2014-09-03 12:13:09'),
(13, 1, 'ni daye', 'f1d0cc21-335f-11e4-9cc7-206a8a5d2ed1', 'ddd', 'x', '2014-09-03 12:35:12'),
(14, 1, 'fdsfdsdsaas ', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:27'),
(15, 1, 'dsfds', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:29'),
(16, 1, 'f', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:30'),
(17, 1, 'd', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:31'),
(18, 1, 's', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:31'),
(19, 1, 'sd', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:32'),
(20, 1, 'sd', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:32'),
(21, 1, 's', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:32'),
(22, 1, 'sd', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:33'),
(23, 1, 'ds', 'b8cbb08f-34b1-11e4-b57d-206a8a5d2ed1', 'ffffv ', ' dddd', '2014-09-05 04:04:33');

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_bin NOT NULL,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=17 ;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'user info', 'backend', 'userinfo'),
(8, 'nav', 'backend', 'nav'),
(9, 'news', 'backend', 'news'),
(10, 'job', 'backend', 'job'),
(11, 'resume', 'backend', 'resume'),
(12, 'comments', 'backend', 'comments'),
(13, 'message', 'chat', 'message'),
(14, 'feedback', 'chat', 'feedback'),
(15, 'advantages', 'backend', 'advantages'),
(16, 'page_keywords', 'backend', 'page_keywords');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0yarqrh7ggut64p2xnjsx9p8fc1rhr7z', 'M2RjODllZjI0MTdmYTRlMmFhMDMwYjljMDExZTI4YWY5OThiMjIzOTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==', '2014-09-24 06:15:58'),
('162t14grgxd1gumww9ak5jrhr8xu44v2', 'ZWYzYmQ2MTZlMmY5ZTVmZWUwMjI3ODFmM2ZhOTg0ZjMwMjIwMjU0Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-09-13 12:01:34'),
('55g1x3owqhg7mmtgcbutcgx4sgqetbwx', 'ZWYzYmQ2MTZlMmY5ZTVmZWUwMjI3ODFmM2ZhOTg0ZjMwMjIwMjU0Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-09-12 03:22:45'),
('881emgt0nd2968s4fxc97k3xg15vtd9b', 'NTczOTdjN2JiODk2ZGNmNzc0NzdjOTg3ZWZmMDlkOWQ5MjU5MTE0Nzp7fQ==', '2014-09-16 01:48:42'),
('nme43e11rqrrme6o7b3vil7m8elqatba', 'M2M3YzliMzg1MDI0ODNjYTE2YjRkMTUwYzUwNThhZTY5ZWE2Mzk3ZDqAAn1xAVUGY3VzdG9tcQIoY2NoYXQudmlld3MKQ3VzdG9tCnEDb31xBChVBXBob25lcQVYBgAAAOmjnua0knEGVQJpZHEHY3V1aWQKVVVJRApxCCmBcQl9cQpVA2ludHELihHRLl2KaiBdpuQRSjNhjQ/5AHNiVQRuYW1lcQxYCQAAAOiMg+W+t+iQqHENdWJzLg==', '2014-09-17 09:16:22'),
('o5mlczrd09q6row2kiavknmavxtr7atm', 'ZWYzYmQ2MTZlMmY5ZTVmZWUwMjI3ODFmM2ZhOTg0ZjMwMjIwMjU0Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-09-15 03:13:53'),
('tubmit4oaq034pjmh3cyfyh9l1jodlm3', 'MGRjZmM2MjAyZTBkNGQwMzgwYjA4YTkzMWVkNjBjY2QxMGY5YjA3YjqAAn1xAVUGY3VzdG9tcQIoY2NoYXQudmlld3MKQ3VzdG9tCnEDb31xBChVBXBob25lcQVYAQAAAHhVAmlkcQZjdXVpZApVVUlECnEHKYFxCH1xCVUDaW50cQqKEdEuXYpqIMec5BFfMyHM0PEAc2JVBG5hbWVxC1gDAAAAZGRkcQx1YnMu', '2014-09-17 11:46:30'),
('tyq5grwxk87l4ege8gvcgl5occz2ocdt', 'ZWYzYmQ2MTZlMmY5ZTVmZWUwMjI3ODFmM2ZhOTg0ZjMwMjIwMjU0Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-09-12 14:41:45'),
('vbds2up0nxuo9br4960fv148qi9sy72g', 'MTdiNWIxNWQ0ZTE3YzI0MjY2Mzc0NDIwNGZhODZhMzhjZDVkM2U1OTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQFVBmN1c3RvbShjY2hhdC52aWV3cwpDdXN0b20KcQVvfXEGKFUFcGhvbmVxB1gFAAAAIGRkZGRVAmlkcQhjdXVpZApVVUlECnEJKYFxCn1xC1UDaW50cQyKEdEuXYpqIH215BGxNI+wy7gAc2JVBG5hbWVxDVgGAAAAZmZmZnYgdWJ1Lg==', '2014-09-19 12:20:14'),
('vsw35rz4184wh8zsg0xba29g2jlmhngr', 'ZjhkZTk2ZTMzYmRmZDRhYzdkMTI2NTllZWFhMTdlYzZhYmIxN2IwMDp7Il9hdXRoX3VzZXJfaWQiOjEsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2014-09-13 06:05:43');

-- --------------------------------------------------------

--
-- 表的结构 `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) COLLATE utf8_bin NOT NULL,
  `name` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

--
-- 限制导出的表
--

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `backend_nav`
--
ALTER TABLE `backend_nav`
  ADD CONSTRAINT `pid_id_refs_id_6cd4a145` FOREIGN KEY (`pid_id`) REFERENCES `backend_nav` (`id`);

--
-- 限制表 `backend_userinfo`
--
ALTER TABLE `backend_userinfo`
  ADD CONSTRAINT `user_id_refs_id_ca7fdcbb` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
