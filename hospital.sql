/*
 Navicat Premium Data Transfer

 Source Server         : 666
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : 110

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 12/03/2023 13:17:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for clinical_feature
-- ----------------------------
DROP TABLE IF EXISTS `clinical_feature`;
CREATE TABLE `clinical_feature`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `发现方式` enum('自查','体检','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤位置` enum('右乳','左乳','双乳','') CHARACTER SET utf8mb4 COLLATE utf8mb4_german2_ci NULL DEFAULT NULL,
  `有无临床首发症状` enum('肿块','乳头溢液','其他首发症状','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `首发症状具体描述` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `患侧乳头` enum('正常','凹陷','半固定','固定','湿疹样','乳头皴裂','乳头缺如','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `患侧乳头症状具体描述` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `患侧皮肤` enum('正常','水肿','卫星结节','破溃','桔皮样变','炎样红肿','静脉曲张','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `患侧皮肤症状具体描述` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `乳头溢液` enum('自发','非自发','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `溢液导管` enum('左侧','右侧','单个','多个','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `溢液性质` enum('陈旧血性','新鲜血性','淡黄','乳汁样','水样','脓性','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `溢液性质具体描述` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `影像检查类型` enum('b超','钼靶','核磁','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `影像检查号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前影像肿瘤大小` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前T分期` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前影像腋下淋巴结位置` enum('腋下Ⅰ水平','腋下Ⅱ水平','腋窝Ⅲ水平','锁骨下','锁骨上','乳内淋巴结','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前影像腋下淋巴结大小` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前N分期` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移与否` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `转移部位` set('肝','肺','骨','脑','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `具体转移部位` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `临床TNM分期` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶确诊方式` enum('术前开放活检','术中开放活检','穿刺粗针吸','穿刺细针吸','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `淋巴结确诊方式` enum('无','粗针吸','细针吸','术前淋巴结活检','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `确诊病理信息` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否行免疫组化` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶穿刺ER` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶穿刺PR` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶穿刺Her2` enum('阴性','1+','2+','3+','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶穿刺Her2具体情况` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶穿刺Ki67` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶穿刺P53` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶FISH` enum('阴性','阳性','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶FISH具体情况` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶FISH copy数` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `肿瘤病灶FISH ratio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结穿刺ER` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结穿刺PR` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结穿刺Her2` enum('阴性','1+','2+','3+','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结穿刺Her2具体情况` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结穿刺Ki67` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结穿刺P53` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结FISH` enum('阴性','阳性','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结FISH具体情况` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结FISH copy数` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结FISH ratio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结穿刺ER` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结穿刺PR` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结穿刺Her2` enum('阴性','1+','2+','3+','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结穿刺Her2具体情况` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结穿刺Ki67` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结穿刺P53` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结FISH` enum('阴性','阳性','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结FISH具体情况` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结FISHcopy数` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `颈部淋巴结FISHratio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移确诊部位` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶ER` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶PR` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶Her2` enum('阴性','1+','2+','3+','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶Her2具体情况` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶Ki67` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶P53` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶FISH` enum('阴性','阳性','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶FISH具体情况` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶FISH copy数` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移灶FISH ratio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前是否行新辅助治疗` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `新辅助治疗开始时间` date NULL DEFAULT NULL,
  `新辅助治疗方案及周期` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `新辅助治疗期间是否使用卵巢功能抑制剂` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `新辅助治疗卵巢功能抑制剂具体药物名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `新辅助治疗过程评估` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `新辅助治疗疗效评价` enum('CR','PR','SD','PD','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前是否行解救治疗` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前解救治疗开始时间` date NULL DEFAULT NULL,
  `术前解救治疗方案及周期` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前解救治疗期间是否使用卵巢功能抑制剂` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前解救治疗卵巢功能抑制剂具体药物名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前解救治疗过程评估` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术前解救治疗疗效评价` enum('CR','PR','SD','PD','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6002 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '临床特征表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for family_history
-- ----------------------------
DROP TABLE IF EXISTS `family_history`;
CREATE TABLE `family_history`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `是否有恶性肿瘤家族史` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `乳腺癌家族史` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `卵巢癌家族史` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `其他恶性肿瘤家族史` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `x级亲属` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '家族史表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for gene21_detection
-- ----------------------------
DROP TABLE IF EXISTS `gene21_detection`;
CREATE TABLE `gene21_detection`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `是否进行21基因检测` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `检测时间` date NULL DEFAULT NULL,
  `研究编号` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `检测人员` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本位置` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `备注` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `具体详情` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '21基因信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for gene70_detection
-- ----------------------------
DROP TABLE IF EXISTS `gene70_detection`;
CREATE TABLE `gene70_detection`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `是否进行70基因检测` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `检测时间` date NULL DEFAULT NULL,
  `研究编号` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `检测人员` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本位置` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `备注` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `具体详情` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '70基因信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for genebrca_detection
-- ----------------------------
DROP TABLE IF EXISTS `genebrca_detection`;
CREATE TABLE `genebrca_detection`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `是否进行BRCA基因检测` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `检测时间` date NULL DEFAULT NULL,
  `研究编号` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `检测人员` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本位置` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `备注` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `具体详情` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = 'brca基因信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for patient
-- ----------------------------
DROP TABLE IF EXISTS `patient`;
CREATE TABLE `patient`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `姓名` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `初诊年龄` int NULL DEFAULT NULL,
  `性别` enum('男','女','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `婚姻状况` enum('已婚','未婚','离异','丧偶','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `民族` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `职业` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `籍贯` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `现地址` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `入院日期` datetime NULL DEFAULT NULL,
  `发现日期` date NULL DEFAULT NULL,
  `联系电话1` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `联系电话2` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `身份证号` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `出生日期` date NULL DEFAULT NULL,
  `体重` float NULL DEFAULT NULL,
  `身高` float NULL DEFAULT NULL,
  `BMI` float NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1006 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '患者基本信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for patient_follow
-- ----------------------------
DROP TABLE IF EXISTS `patient_follow`;
CREATE TABLE `patient_follow`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `DFS` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `死亡与否` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `死亡时间` datetime NULL DEFAULT NULL,
  `死因` enum('肿瘤','非肿瘤','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `具体死因` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `OS` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `末次复查时间（截止查病历时/电话随诊）` date NULL DEFAULT NULL,
  `治疗后生育情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `双原发癌症` enum('无','对侧乳腺','非同侧胸壁','区域淋巴结','其他原发癌','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `双原发癌症具体详情` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `双原发癌症首次发生时间` datetime NULL DEFAULT NULL,
  `随访备注` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '病人跟踪记录表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for patient_history
-- ----------------------------
DROP TABLE IF EXISTS `patient_history`;
CREATE TABLE `patient_history`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `是否吸烟` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `具体吸烟量` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否饮酒` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `具体饮酒量` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '个人史表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for patient_marry_history
-- ----------------------------
DROP TABLE IF EXISTS `patient_marry_history`;
CREATE TABLE `patient_marry_history`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `生育` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `确诊时生育状态` enum('无','哺乳期','妊娠期','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `初产年龄` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `末胎年龄` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `怀孕次数` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `足月产` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `流产或早产史` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否辅助生育` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `辅助生育方式` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否母乳喂养` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `哺乳侧别` enum('左','右','双','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `哺乳时长` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6246 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '婚育史表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for patient_menstruation_history
-- ----------------------------
DROP TABLE IF EXISTS `patient_menstruation_history`;
CREATE TABLE `patient_menstruation_history`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `初潮年龄` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `月经周期` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `经期` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否绝经` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `绝经方式` enum('自然','人工','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `具体绝经方式` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `末次月经` date NULL DEFAULT NULL,
  `绝经年龄` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '月经表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for peripheral_blood_sample_sampling
-- ----------------------------
DROP TABLE IF EXISTS `peripheral_blood_sample_sampling`;
CREATE TABLE `peripheral_blood_sample_sampling`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `标本类型` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `采血时间点` datetime NULL DEFAULT NULL,
  `采集人` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `采集备注` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `采集用途` enum('常规收集','课题','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本编码` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本量` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本盒编码` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本存放位置` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否取用` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `取用日期` date NULL DEFAULT NULL,
  `取用人` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `取用用途` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `取用备注` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '外周血标本采样表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for postoperative_treatment
-- ----------------------------
DROP TABLE IF EXISTS `postoperative_treatment`;
CREATE TABLE `postoperative_treatment`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `术后化疗` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后化疗开始时间` date NULL DEFAULT NULL,
  `术后化疗方案` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后化疗详情` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后化疗期间是否使用卵巢功能抑制剂` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后化疗卵巢功能抑制剂具体药物名称` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后内分泌治疗` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后内分泌治疗开始时间` date NULL DEFAULT NULL,
  `术后内分泌治疗药物` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `内分泌治疗副作用` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否术后靶向治疗` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后靶向治疗开始时间` date NULL DEFAULT NULL,
  `术后靶向治疗具体药物` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后放疗` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后放疗开始时间` datetime NULL DEFAULT NULL,
  `术后放疗备注` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后免疫治疗` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后免疫治疗开始时间` date NULL DEFAULT NULL,
  `术后免疫治疗备注` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '术后治疗表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for previous_history
-- ----------------------------
DROP TABLE IF EXISTS `previous_history`;
CREATE TABLE `previous_history`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `乳腺良性疾病史` enum('无','纤维腺瘤','增生性疾病','导管内乳头状瘤','炎症性疾病','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `乳腺良性疾病史具体情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `感染性疾病` set('无','肝炎','梅毒','艾滋','新冠','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `感染性疾病具体情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `新冠阳性日期` date NULL DEFAULT NULL,
  `新冠转阴日期` date NULL DEFAULT NULL,
  `新冠转阴确诊方式` enum('核酸确诊','抗原确诊','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否有系统疾病` set('无','高血压','心脏病','糖尿病','青光眼','哮喘','甲状腺疾病','脑血管疾病','精神疾病','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `系统疾病具体情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否有手术史` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `手术史具体情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否有恶性肿瘤既往史` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `恶性肿瘤既往史具体情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '既往史表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for recorder_information
-- ----------------------------
DROP TABLE IF EXISTS `recorder_information`;
CREATE TABLE `recorder_information`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `首次录入人` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `首次录入时间` datetime NULL DEFAULT NULL,
  `末次随访人` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `末次随访时间` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '记录人员信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for recurrent_distant_metastasis
-- ----------------------------
DROP TABLE IF EXISTS `recurrent_distant_metastasis`;
CREATE TABLE `recurrent_distant_metastasis`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `第几次转移` int NULL DEFAULT NULL,
  `远处转移部位` set('对侧乳腺','非同侧胸壁','区域淋巴结','骨','肺','肝','脑','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT '',
  `远处转移日期` datetime NULL DEFAULT NULL,
  `远处转移确诊手段` enum('无','粗针吸穿刺','细针吸穿刺','开放活检','手术','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移病理信息` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移免疫组化` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移治疗` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `远处转移治疗效果评价` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '远处转移信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for relapse_information
-- ----------------------------
DROP TABLE IF EXISTS `relapse_information`;
CREATE TABLE `relapse_information`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `第几次复发` int NULL DEFAULT NULL,
  `复发部位` enum('胸壁复发','保乳术后复发','同侧腋窝及锁上淋巴结复发','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `具体复发部位` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `复发日期` date NULL DEFAULT NULL,
  `复发确诊手段` enum('无','粗针吸穿刺','细针吸穿刺','开放活检','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `复发病灶病理信息` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `复发病灶免疫组化` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `复发后治疗` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `复发后治疗效果评价` enum('CR','PR','SD','PD','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '复发信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for sampling_recurrence_metastasis_specimens
-- ----------------------------
DROP TABLE IF EXISTS `sampling_recurrence_metastasis_specimens`;
CREATE TABLE `sampling_recurrence_metastasis_specimens`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `关联病灶` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `采样日期` date NULL DEFAULT NULL,
  `用途标识` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `其他用途` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `采集人` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本类型` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本性质` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本编码` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本量` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本盒编码` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `标本存放位置` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否取用` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `取用日期` date NULL DEFAULT NULL,
  `取用人` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `取用用途` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `取用备注` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '复发转移灶标本采样表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for surgical_pathological_info
-- ----------------------------
DROP TABLE IF EXISTS `surgical_pathological_info`;
CREATE TABLE `surgical_pathological_info`  (
  `编号` int NOT NULL AUTO_INCREMENT,
  `滨海住院号` int NULL DEFAULT NULL,
  `河西住院号` int NULL DEFAULT NULL,
  `手术日期` date NULL DEFAULT NULL,
  `手术方式` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否保乳` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `是否再造` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结清扫方式` enum('腋清','前哨淋巴结活检','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `术后大病理号` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `病灶数量` int NULL DEFAULT NULL,
  `肉眼肿物大小` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `病理学分期` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `病理类型` enum('导管内癌','小叶原位癌','乳头湿疹样乳腺癌','浸润性导管癌','浸润性小叶癌','浸润性特殊癌','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `病理具体描述` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `组织学分级` enum('I','II','III','I-II','II-III','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `组织学分级具体情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `淋巴血管侵犯与否` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `淋巴管癌栓` enum('有','无','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `间质内浸润淋巴细胞` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `化疗反应` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `保乳手术标本周断端是否可见癌组织` enum('是','否','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `保乳手术标本周断端` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `保乳手术标本补切周断端` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `淋巴结情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `腋窝淋巴结总数` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `阳性腋窝淋巴结数` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `ER` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `PR` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `HER2` enum('阴性','1+','2+','3+','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `HER2具体情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `Ki67` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `P53` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `FISH` enum('阴性','阳性','其他','') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `FISH具体情况` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `HER2-FISH COPY数` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `HER2-FISH RATIO` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2001 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci COMMENT = '手术病理信息表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `admin` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `password` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `status` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `admin`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
