/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : mosesdb

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2017-02-28 21:27:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for d2heros
-- ----------------------------
DROP TABLE IF EXISTS `d2heros`;
CREATE TABLE `d2heros` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `localized_name` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for d2leagues
-- ----------------------------
DROP TABLE IF EXISTS `d2leagues`;
CREATE TABLE `d2leagues` (
  `league_name` varchar(60) DEFAULT NULL,
  `league_id` int(60) NOT NULL,
  `tournament_url` varchar(255) DEFAULT NULL,
  `itemdef` varchar(60) DEFAULT NULL,
  `description` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`league_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for matchrecord
-- ----------------------------
DROP TABLE IF EXISTS `matchrecord`;
CREATE TABLE `matchrecord` (
  `id` int(32) DEFAULT NULL,
  `hero` varchar(64) DEFAULT NULL,
  `fetchTime` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `matchTime` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `kda` varchar(11) DEFAULT NULL,
  `matchResult` varchar(11) DEFAULT NULL,
  `gameUser` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
