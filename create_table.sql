SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for train
-- ----------------------------
DROP TABLE IF EXISTS `train`;
CREATE TABLE `train` (
  `id` int(11) NOT NULL COMMENT '渔船id',
  `x` double DEFAULT NULL,
  `y` double DEFAULT NULL,
  `speed` float DEFAULT NULL,
  `direction` varchar(255) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;