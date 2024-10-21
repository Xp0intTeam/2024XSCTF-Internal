CREATE DATABASE IF NOT EXISTS student;

USE student;

DROP TABLE IF EXISTS `class1`;
CREATE TABLE `class1` (
  `id` int NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class` int NOT NULL,
  `hobbies` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of class1
-- ----------------------------
INSERT INTO `class1` VALUES ('1', '地狱火', '1', '大哥真送吗');
INSERT INTO `class1` VALUES ('2', '坤坤', '1', '唱，跳，rap，篮球');
INSERT INTO `class1` VALUES ('3', '孙思远', '1', '长跑, 听音乐');
INSERT INTO `class1` VALUES ('4', '周雨婷', '1', '看电影, 做手工');
INSERT INTO `class1` VALUES ('5', '吴雅琪', '1', '摄影, 写作');
INSERT INTO `class1` VALUES ('6', '郑嘉欣', '1', '跳舞, 看书');
INSERT INTO `class1` VALUES ('7', '王浩天', '1', '打游戏, 健身');
INSERT INTO `class1` VALUES ('8', '陈俊杰', '1', '钓鱼, 徒步');
INSERT INTO `class1` VALUES ('9', '赵婉如', '1', '养花, 做陶艺');
INSERT INTO `class1` VALUES ('10', '黄梓轩', '1', '学习外语, 旅行');
INSERT INTO `class1` VALUES ('11', '陈静雅', '1', '水彩画, 摄影');
INSERT INTO `class1` VALUES ('12', '何蝶舞', '1', '篮球, 听音乐');
INSERT INTO `class1` VALUES ('13', '许琳琳', '1', '瑜伽, 做烘焙');
INSERT INTO `class1` VALUES ('14', '陆志强', '1', '跑步, 看书');
INSERT INTO `class1` VALUES ('15', '张子萱', '1', '画画, 写作');
INSERT INTO `class1` VALUES ('16', '林梦瑶', '1', '游泳, 看电影');
INSERT INTO `class1` VALUES ('17', '陶天宇', '1', '街舞, 健身');
INSERT INTO `class1` VALUES ('18', '梁思悦', '1', '编程, 徒步');
INSERT INTO `class1` VALUES ('19', '邓浩宇', '1', '养盆栽, 做DIY');
INSERT INTO `class1` VALUES ('20', '蒋雨欣', '1', '学法语, 烹饪');
INSERT INTO `class1` VALUES ('21', '韩婉婷', '1', '篮球, 听音乐');
INSERT INTO `class1` VALUES ('22', '许梓敏', '1', '素描, 写日记');
INSERT INTO `class1` VALUES ('23', '赵梦婷', '1', '游泳, 看纪录片');
INSERT INTO `class1` VALUES ('24', '冯雅琪', '1', '民族舞, 阅读');
INSERT INTO `class1` VALUES ('25', '程浩宇', '1', '游戏开发, 健身');
INSERT INTO `class1` VALUES ('26', '沈欣怡', '1', '养多肉, 徒步旅行');
INSERT INTO `class1` VALUES ('27', '曾志强', '1', '学习德语, 背包旅行');
INSERT INTO `class1` VALUES ('28', '雷蕾', '1', '瑜伽冥想, 做家常菜');
INSERT INTO `class1` VALUES ('29', '汪子豪', '1', '晨跑, 看书评');
INSERT INTO `class1` VALUES ('30', '陆欣', '1', '画画, 写短篇小说');
-- ----------------------------
-- Table structure for `class2`
-- ----------------------------
DROP TABLE IF EXISTS `class2`;
CREATE TABLE `class2` (
  `id` int NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class` int NOT NULL,
  `hobbies` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of class2
-- ----------------------------
INSERT INTO `class2` VALUES ('1', '李明', '2', '打篮球, 编程');
INSERT INTO `class2` VALUES ('2', '王丽', '2', '画画, 阅读');
INSERT INTO `class2` VALUES ('3', '张伟', '2', '跑步, 听音乐');
INSERT INTO `class2` VALUES ('4', '赵敏', '2', '看电影, 做手工');
INSERT INTO `class2` VALUES ('5', '刘阳', '2', '摄影, 写作');
INSERT INTO `class2` VALUES ('6', '陈晨', '2', '跳舞, 看书');
INSERT INTO `class2` VALUES ('7', '杨帆', '2', '打游戏, 健身');
INSERT INTO `class2` VALUES ('8', '周涛', '2', '钓鱼, 徒步');
INSERT INTO `class2` VALUES ('9', '吴静', '2', '养花, 做陶艺');
INSERT INTO `class2` VALUES ('10', '徐强', '2', '学习外语, 背包旅行');
INSERT INTO `class2` VALUES ('11', '孙悦', '2', '做甜点, 弹吉他');
INSERT INTO `class2` VALUES ('12', '高洁', '2', '游泳, 看电影');
INSERT INTO `class2` VALUES ('13', '林浩', '2', '打羽毛球, 编程');
INSERT INTO `class2` VALUES ('14', '郭婷', '2', '素描, 写日记');
INSERT INTO `class2` VALUES ('15', '罗斌', '2', '骑行, 摄影');
INSERT INTO `class2` VALUES ('16', '张薇', '2', '练瑜伽, 看书');
INSERT INTO `class2` VALUES ('17', '曹阳', '2', '打篮球, 健身');
INSERT INTO `class2` VALUES ('18', '何静', '2', '做手工, 养宠物');
INSERT INTO `class2` VALUES ('19', '谢飞', '2', '学习编程, 打游戏');
INSERT INTO `class2` VALUES ('20', '韩雪', '2', '画画, 写小说');
INSERT INTO `class2` VALUES ('21', '程鹏', '2', '长跑, 听音乐');
INSERT INTO `class2` VALUES ('22', '许晴', '2', '看电影, 做甜点');
INSERT INTO `class2` VALUES ('23', '马强', '2', '学习法语, 旅行');
INSERT INTO `class2` VALUES ('24', '朱莉', '2', '打网球, 看书');
INSERT INTO `class2` VALUES ('25', '王磊', '2', '健身, 钓鱼');
INSERT INTO `class2` VALUES ('26', '李娜', '2', '做陶艺, 养多肉');
INSERT INTO `class2` VALUES ('27', '赵雷', '2', '学习德语, 背包旅行');
INSERT INTO `class2` VALUES ('28', '刘芳', '2', '瑜伽冥想, 做家常菜');
INSERT INTO `class2` VALUES ('29', '陈波', '2', '跑步, 看书评');
INSERT INTO `class2` VALUES ('30', '周洁', '2', '画画, 写散文');
INSERT INTO `class2` VALUES ('31', '吴鹏', '2', '打篮球, 健身操');
INSERT INTO `class2` VALUES ('32', '郑丽', '2', '做手工, 养花');
INSERT INTO `class2` VALUES ('33', '王浩', '2', '学习编程, 打游戏机');
INSERT INTO `class2` VALUES ('34', '张敏', '2', '画画, 写短篇小说');

-- ----------------------------
-- Table structure for `class3`
-- ----------------------------
DROP TABLE IF EXISTS `class3`;
CREATE TABLE `class3` (
  `id` int NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class` int NOT NULL,
  `hobbies` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of class3
-- ----------------------------
INSERT INTO `class3` VALUES ('1', '赵天宇', '3', '打篮球, 编程');
INSERT INTO `class3` VALUES ('2', '陈思琪', '3', '画画, 阅读书籍');
INSERT INTO `class3` VALUES ('3', '刘浩然', '3', '跑步, 听音乐');
INSERT INTO `class3` VALUES ('4', '李欣怡', '3', '看电影, 做手工');
INSERT INTO `class3` VALUES ('5', '王梓轩', '3', '摄影, 写短篇小说');
INSERT INTO `class3` VALUES ('6', '张梓涵', '3', '跳舞, 看书');
INSERT INTO `class3` VALUES ('7', '黄俊杰', '3', '打游戏, 健身');
INSERT INTO `class3` VALUES ('8', '林晓峰', '3', '钓鱼, 徒步旅行');
INSERT INTO `class3` VALUES ('9', '郭雨欣', '3', '养花, 做陶艺');
INSERT INTO `class3` VALUES ('10', '何志强', '3', '学习外语, 背包旅行');
INSERT INTO `class3` VALUES ('11', '孙雅琪', '3', '做甜点, 弹吉他');
INSERT INTO `class3` VALUES ('12', '周慧敏', '3', '游泳, 看话剧');
INSERT INTO `class3` VALUES ('13', '吴浩宇', '3', '打羽毛球, 学习编程');
INSERT INTO `class3` VALUES ('14', '郑欣怡', '3', '素描, 写日记');
INSERT INTO `class3` VALUES ('15', '徐子轩', '3', '骑行, 摄影');
INSERT INTO `class3` VALUES ('16', '朱梓萱', '3', '练瑜伽, 看书');
INSERT INTO `class3` VALUES ('17', '马天宇', '3', '打篮球, 健身');
INSERT INTO `class3` VALUES ('18', '陈静雅', '3', '做手工, 养宠物');
INSERT INTO `class3` VALUES ('19', '高思远', '3', '学习编程, 打游戏');
INSERT INTO `class3` VALUES ('20', '罗梓萱', '3', '画画, 写散文');
INSERT INTO `class3` VALUES ('21', '谢浩然', '3', '长跑, 听音乐');
INSERT INTO `class3` VALUES ('22', '李梓轩', '3', '看电影, 做甜点');
INSERT INTO `class3` VALUES ('23', '韩天宇', '3', '学习法语, 旅行');
INSERT INTO `class3` VALUES ('24', '王梓涵', '3', '打网球, 看书');
INSERT INTO `class3` VALUES ('25', '张浩然', '3', '健身, 钓鱼');
INSERT INTO `class3` VALUES ('26', '刘思琪', '3', '做陶艺, 养多肉');
INSERT INTO `class3` VALUES ('27', '陈梓轩', '3', '学习德语, 背包旅行');
INSERT INTO `class3` VALUES ('28', '周梓萱', '3', '瑜伽冥想, 做家常菜');
INSERT INTO `class3` VALUES ('29', '黄慧敏', '3', '跑步, 看书评');
INSERT INTO `class3` VALUES ('30', '林俊杰', '3', '画画, 写小说');
INSERT INTO `class3` VALUES ('31', '赵梓萱', '3', '打篮球, 健身操');
INSERT INTO `class3` VALUES ('32', '陈雅琪', '3', '做手工, 养花');
INSERT INTO `class3` VALUES ('33', '王浩宇', '3', '学习编程, 打游戏机');
INSERT INTO `class3` VALUES ('34', '李慧敏', '3', '画画, 写诗歌');