'''
patient
'''
import datetime

from sqlalchemy import Integer,Float, BigInteger, String, DateTime, Text, Boolean, Column, Sequence, ForeignKey, UniqueConstraint,Enum
from sqlalchemy.orm import backref, relationship

from rptserver.database.sqlal import Base

class Patient(Base):
    '''病人'''
    __tablename__ = 'patient'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    name = Column(String(25), doc='姓名',name = '姓名')
    phone1 = Column(String(255), doc="联系电话1", name = '联系电话1')
    phone2 = Column(String(255), doc="联系电话2", name = '联系电话2')
    sex = Column(Enum("男", "女"), name = "性别")
    marital_status = Column(Enum('已婚','未婚','离异','丧偶'), name = "婚姻状况")
    age = Column(Integer, doc="初诊年龄", name = '初诊年龄')
    mz = Column(String(25), doc='民族',name = '民族')
    job = Column(String(25), doc='职业',name = '职业')
    jg = Column(String(25), doc='籍贯',name = '籍贯')
    addr = Column(String(255), doc='现地址',name = '现地址')
    fbDate = Column(DateTime, doc="发现日期", name = '发现日期')
    ryDate = Column(DateTime, doc="入院日期", name = '入院日期')
    cert_id = Column(String(255), doc='身份证号',name = '身份证号')
    birthday = Column(DateTime, doc="出生日期", name = '出生日期')
    tall = Column(Float, name = '身高')
    weight = Column(Float, name = '体重')
    bmi = Column(Float, name = 'BMI')

class PreviousHistory(Base):
    """既往病史"""
    __tablename__ = 'previous_history'
    
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    rxlxjbs = Column(Enum('无','纤维腺瘤','增生性疾病','导管内乳头状瘤','炎症性疾病','其他') , doc='乳腺良性疾病史',name = '乳腺良性疾病史')
    rxlxjbsjtqk = Column(String(255) ,name = '乳腺良性疾病史具体情况')
    grxjb = Column(String(255), doc='感染性疾病',name = '感染性疾病')
    grxjbjtqk = Column(String(255) ,name = '感染性疾病具体情况')
    xgyxrq = Column(DateTime, doc="新冠阳性日期", name = '新冠阳性日期')
    xgzyrq = Column(DateTime, doc="新冠转阴日期", name = '新冠转阴日期')
    xgzyqzfs = Column(Enum('核酸确诊','抗原确诊','其他'), name = '新冠转阴确诊方式')
    xtxjb = Column(String(255), doc='是否有系统疾病',name = '是否有系统疾病')
    xtjbjtqk = Column(String(255) ,name = '系统疾病具体情况')
    sss = Column(Enum("是", "否"), name = "是否有手术史")
    sssjtqk = Column(String(255) ,name = '手术史具体情况')
    exzl = Column(Enum("是", "否"), doc='是否有恶性肿瘤既往史',name = '是否有恶性肿瘤既往史')
    exzljtqk = Column(String(255) ,name = '恶性肿瘤既往史具体情况')

class surgicalPathologicalInfo(Base):
    """手术及病理信息"""
    __tablename__ = 'surgical_pathological_info'
    
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    ssrq = Column(DateTime, doc="手术日期", name = '手术日期')
    ssfs = Column(String(100), name = '手术方式')
    sfbr = Column(Enum('是','否'), name = '是否保乳')
    sfzz = Column(Enum('是','否'), name = '是否再造')
    ywlbqsfs = Column(Enum('腋清','前哨淋巴结活检'), name = '腋窝淋巴结清扫方式')
    shdblh = Column(String(100), name = '术后大病理号')
    bzsl = Column(Integer, name = '病灶数量')
    ryzwdx = Column(String(200), name = '肉眼肿物大小')
    blxfq = Column(String(255), name = '病理学分期')
    bllx = Column(Enum('导管内癌','小叶原位癌','乳头湿疹样乳腺癌','浸润性导管癌','浸润性小叶癌','浸润性特殊癌','其他'), name = '病理类型')
    blxjtms = Column(String(1000), name = '病理具体描述')

    zzxfj = Column(Enum('I','II','III','I-II','II-III','其他'), name = '组织学分级')
    zzxfjjtqk = Column(String(100), name = '组织学分级具体情况')
    lbxgqf = Column(String(255), name = '淋巴血管侵犯与否')
    lbgbs = Column(Enum('有','无'), name = '淋巴管癌栓')
    jzznqrlbxb = Column(String(255), name = '间质内浸润淋巴细胞')
    hlfy = Column(String(255), name = '化疗反应')
    brsskjazz = Column(Enum('是','否'), name = '保乳手术标本周断端是否可见癌组织')
    brssbbzdd = Column(String(1000), name = '保乳手术标本周断端')
    brssbbbqzdd = Column(String(255), name = '保乳手术标本补切周断端')
    
    lbjqk = Column(String(255), name = '淋巴结情况')
    ywlbzs = Column(Integer, name = '腋窝淋巴结总数')
    yxywlbzs = Column(Integer, name = '阳性腋窝淋巴结数')
    er = Column(String(255), name = 'ER')
    pr = Column(String(255), name = 'PR')
    her2 = Column(Enum('阴性','1+','2+','3+','其他'), name = 'HER2')
    her2jtqk = Column(String(255), name = 'her2具体情况')
    ki67 = Column(String(255), name = 'Ki67')
    p53 = Column(String(255), name = 'P53')
    fish = Column( Enum('阴性','阳性','其他'), name = 'FISH') 
    fishjtqk = Column(String(20), name = 'FISH具体情况') 
    hfc = Column(String(255), name = 'HER2-FISH COPY数')
    hfr = Column(String(255), name = 'HER2-FISH RATIO')
    

class familyHistory(Base):
    """家族史表"""
    
    __tablename__ = 'family_history'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    wxzl = Column(Enum('是','否'), name = '是否有恶性肿瘤家族史') 
    rxa = Column(Enum('是','否'), name = '乳腺癌家族史')
    lca = Column(Enum('是','否'), name = '卵巢癌家族史')
    qtwxzl = Column(Enum('是','否'), name = '其他恶性肿瘤家族史') 
    qtwxzljtqk = Column(String(255), name = '其他恶性肿瘤家族史具体情况')
    xqs = Column(String(100), name = 'x级亲属')

class patientHistory(Base):
    """个人史表"""
    
    __tablename__ = 'patient_history'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    
    sfxy = Column(Enum('是','否'), name = '是否吸烟') 
    jtxyl = Column(String(255), name = '具体吸烟量')
    sfyj = Column(Enum('是','否'), name = '是否饮酒') 
    jtyjl = Column(String(255), name = '具体饮酒量')


class clinicalFeature(Base):
    """临床特征表"""
    
    __tablename__ = 'clinical_feature'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    fxwz = Column(Enum('自查','体检','其他'), name = '发现方式') 
    zkwz = Column(Enum('右乳','左乳','双乳'), name = '肿瘤位置') 
    lcsfzz = Column(Enum('肿块','乳头溢液','其他首发症状'), name = '有无临床首发症状')
    sfzzjtms = Column(String(255), name = '首发症状具体描述') 
    hcrt = Column(Enum('正常','凹陷','半固定','固定','湿疹样','乳头皴裂','乳头缺如','其他'), name = '患侧乳头')
    hcrtjtms = Column(String(255), name = '患侧乳头症状具体描述') 
    hcpf = Column(Enum('正常','水肿','卫星结节','破溃','桔皮样变','炎样红肿','静脉曲张','其他'), name = '患侧皮肤')
    hcpfjtms = Column(String(255), name = '患侧皮肤症状具体描述') 
    rtyy = Column(Enum('自发','非自发'), name = '乳头溢液')
    yydg = Column(Enum('左侧','右侧','单个','多个'), name = '溢液导管')
    yyxz = Column(Enum('陈旧血性','新鲜血性','淡黄','乳汁样','水样','脓性','其他'), name = '溢液性质')
    yyxzjtms = Column(String(255), name = '溢液性质具体描述') 
    yxjclx = Column(Enum('b超','钼靶','核磁'), name = '影像检查类型')
    yxjch = Column(String(255), name = '影像检查号')
    sqzldx = Column(String(100), name = '术前影像肿瘤大小') 
    sqtfq = Column(String(100), name = '术前T分期') 
    sqyxlbjwz = Column(Enum('腋下Ⅰ水平','腋下Ⅱ水平','腋窝Ⅲ水平','锁骨下','锁骨上','乳内淋巴结'), name = '术前影像腋下淋巴结位置') 
    sqyxlbjdx = Column(String(255), name = '术前影像腋下淋巴结大小') 
    sqnfq = Column(String(100), name = '术前N分期') 
    yczy = Column(Enum('是','否'), name = '远处转移与否')
    zybw = Column(Enum('肝','肺','骨','脑','其他'), name = '转移部位') 
    jtzybw = Column(String(255), name = '具体转移部位')
    tnm = Column(String(100), name = '临床TNM分期') 
    zlbzqzfs = Column(Enum('术前开放活检','术中开放活检','穿刺粗针吸','穿刺细针吸'), name = '肿瘤病灶确诊方式')  
    lbjqzfs = Column(Enum('无','粗针吸','细针吸','术前淋巴结活检'), name = '淋巴结确诊方式') 
    qzblh = Column(String(100), name = '确诊病理信息')  
    sfxmyzh = Column(Enum('是','否'), name = '是否行免疫组化')
    
    er = Column(String(100), name = '肿瘤病灶穿刺ER') 
    pr = Column(String(100), name = '肿瘤病灶穿刺PR') 
    her2 = Column( Enum('阴性','1+','2+','3+','其他'), name = '肿瘤病灶穿刺Her2') 
    her2jtqk = Column(String(20), name = '肿瘤病灶穿刺Her2具体情况') 
    ki67 = Column(String(100), name = '肿瘤病灶穿刺Ki67') 
    p53 = Column(String(100), name = '肿瘤病灶穿刺P53') 
    fish = Column( Enum('阴性','阳性','其他'), name = '肿瘤病灶FISH') 
    fishjtqk = Column(String(20), name = '肿瘤病灶FISH具体情况') 
    fcopy = Column(String(100), name = '肿瘤病灶FISH copy数') 
    fratio = Column(String(100), name = '肿瘤病灶FISH ratio') 
    
    ywlbjer = Column(String(100), name = '腋窝淋巴结穿刺ER') 
    ywlbjpr = Column(String(100), name = '腋窝淋巴结穿刺PR') 
    ywlbjher2 = Column(Enum('阴性','1+','2+','3+','其他'), name = '腋窝淋巴结穿刺Her2')
    ywlbjher2jtqk = Column(String(20), name = '腋窝淋巴结穿刺Her2具体情况')
    ywlbjki67 = Column(String(100), name = '腋窝淋巴结穿刺Ki67') 
    ywlbjp53 = Column(String(100), name = '腋窝淋巴结穿刺P53') 
    ywlbjfish = Column( Enum('阴性','阳性','其他'), name = '腋窝淋巴结FISH') 
    ywlbjfishjtqk = Column(String(20), name = '腋窝淋巴结FISH具体情况') 
    ywlbjfcopy = Column(String(100), name = '腋窝淋巴结FISH copy数')
    ywlbjfratio =  Column(String(100), name = '腋窝淋巴结FISH ratio') 

    jblbjer = Column(String(100), name = '颈部淋巴结穿刺ER') 
    jblbjpr = Column(String(100), name = '颈部淋巴结穿刺PR') 
    jblbjher2 = Column(Enum('阴性','1+','2+','3+','其他'), name = '颈部淋巴结穿刺Her2')
    jblbjher2jtqk = Column(String(20), name = '颈部淋巴结穿刺Her2具体情况')
    jblbjki67 = Column(String(100), name = '颈部淋巴结穿刺Ki67') 
    jblbjp53 = Column(String(100), name = '颈部淋巴结穿刺P53') 
    jblbjfish = Column( Enum('阴性','阳性','其他'), name = '颈部淋巴结FISH') 
    jblbjfishjtqk = Column(String(20), name = '颈部淋巴结FISH具体情况') 
    jblbjfcopy = Column(String(100), name = '颈部淋巴结FISHcopy数')
    jblbjfratio =  Column(String(100), name = '颈部淋巴结FISHratio') 
    
    yczyqzbw = Column(String(100), name = '远处转移确诊部位') 
    yczyer = Column(String(100), name = '远处转移灶ER') 
    yczypr = Column(String(100), name = '远处转移灶PR') 
    yczyher2 = Column(Enum('阴性','1+','2+','3+','其他'), name = '远处转移灶Her2')
    yczyher2jtqk = Column(String(20), name = '远处转移灶Her2具体情况')
    yczyki67 = Column(String(100), name = '远处转移灶Ki67') 
    yczyp53 = Column(String(100), name = '远处转移灶P53') 
    yczyfish = Column( Enum('阴性','阳性','其他'), name = '远处转移灶FISH') 
    yczyfishjtqk = Column(String(20), name = '远处转移灶FISH具体情况') 
    yczyfcopy = Column(String(100), name = '远处转移灶FISH copy数')
    yczyfratio =  Column(String(100), name = '远处转移灶FISH ratio') 
    
    xfzzl = Column(Enum('是','否'), name = '术前是否行新辅助治疗')
    xfzzlkssj = Column(DateTime, doc="新辅助治疗开始时间", name = '新辅助治疗开始时间')
    xfzzlfa = Column(String(1000), name = '新辅助治疗方案及周期') 
    xfzlc = Column(Enum('是','否'), name = '新辅助治疗期间是否使用卵巢功能抑制剂')
    xfzlcyw = Column(String(255), name = '新辅助治疗卵巢功能抑制剂具体药物名称') 
    xfzzlpg = Column(String(1000), name = '新辅助治疗过程评估') 
    xfzzlpj = Column(Enum('CR','PR','SD','PD'), name = '新辅助治疗疗效评价') 
    
    jjzl = Column(Enum('是','否'), name = '术前是否行解救治疗')
    sqzlkssj = Column(DateTime, doc="术前解救治疗开始时间", name = '术前解救治疗开始时间')
    sqzlfa = Column(String(1000), name = '术前解救治疗方案及周期') 
    jjlc = Column(Enum('是','否'), name = '术前解救治疗期间是否使用卵巢功能抑制剂')
    jjlcyw = Column(String(255), name = '术前解救治疗卵巢功能抑制剂具体药物名称') 
    sqzlpg = Column(String(1000), name = '术前解救治疗过程评估') 
    sqzlpj = Column(Enum('CR','PR','SD','PD'), name = '术前解救治疗疗效评价') 
    
class patientMenstruationHistory(Base):
    """月经史表"""
    __tablename__ = 'patient_menstruation_history'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    
    ccage = Column(String(20), name = '初潮年龄')
    yjzq = Column(String(20), name = '月经周期')
    jq = Column(String(20), name = '经期')
    sfjj = Column(Enum('是','否'), name = '是否绝经')
    jjfs = Column(Enum('自然','人工','其他'), name = '绝经方式') 
    jtjjfs = Column(String(50), name = '具体绝经方式')
    mqyj = Column(DateTime, doc="末次月经", name = '末次月经')
    jjage = Column(String(20), name = '绝经年龄')


class patientMarryHistory(Base):
    """婚育史表"""
    __tablename__ = 'patient_marry_history'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    
    sy = Column(Enum('是','否'), name = '生育')
    qzssyzt = Column(Enum('无','哺乳期','妊娠期'), name = '确诊时生育状态')
    ccage = Column(String(20), name = '初产年龄')
    mtage = Column(String(20), name = '末胎年龄')
    hycs = Column(String(20), name = '怀孕次数')
    zyc = Column(String(20), name = '足月产') 
    lczcs = Column(String(100), name = '流产或早产史') 
    fzsy = Column(Enum('是','否'), name = '是否辅助生育')
    fzsyfs = Column(String(100), name = '辅助生育方式') 
    sfmrwy = Column(Enum('是','否'), name = '是否母乳喂养')
    mrcb = Column(Enum('左','右','双'), name = '哺乳侧别')
    mrsc = Column(String(10), name = '哺乳时长')
    

class patientFollow(Base):
    """病人跟踪记录表"""
    __tablename__ = 'patient_follow'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    
    dfs = Column(String(255), name = 'DFS') 
    os = Column(String(255), name = 'OS') 
    mcfcsj = Column(DateTime, doc="末次复查时间（截止查病历时/电话随诊）", name = '末次复查时间（截止查病历时/电话随诊）')
    syqk = Column(String(255), name = '治疗后生育情况') 
    syfaz = Column(Enum('无','对侧乳腺','非同侧胸壁','区域淋巴结','其他原发癌'), name = '双原发癌症') 
    syfazjtxq = Column(String(255), name = '双原发癌症具体详情')
    zhsfsj = Column(DateTime, doc="双原发癌症首次发生时间", name = '双原发癌症首次发生时间')
    sfbz = Column(String(255), name = '随访备注') 
    swyf = Column(Enum('是','否'), name = '死亡与否')
    swsj = Column(DateTime, doc="死亡时间", name = '死亡时间')
    sy = Column(Enum('肿瘤','非肿瘤','其他'), name = '死因') 
    jtsy = Column(String(255), name = '具体死因') 
    

class postoperativeTreatment(Base):
    """术后治疗表"""
    __tablename__ = 'postoperative_treatment'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    
    shhl = Column(Enum('是','否',''), name = '术后化疗')
    hlkssj = Column(DateTime, doc="术后化疗开始时间", name = '术后化疗开始时间')
    shhlfam = Column(String(1000), name = '术后化疗方案')
    hllc = Column(Enum('是','否',''), name = '术后化疗期间是否使用卵巢功能抑制剂')
    hllcyw = Column(String(255), name = '术后化疗卵巢功能抑制剂具体药物名称') 
    shhlxq = Column(String(255), name = '术后化疗详情') 
    shnfmzl = Column(Enum('是','否',''), name = '术后内分泌治疗')
    nfmzlkssj = Column(DateTime, doc="术后内分泌治疗开始时间", name = '术后内分泌治疗开始时间')
    nfmzlym = Column(String(255), name = '术后内分泌治疗药物') 
    nfmzlfzy = Column(String(255), name = '内分泌治疗副作用') 
    shbxzl = Column(Enum('是','否',''), name = '是否术后靶向治疗')
    bxzlkssj = Column(DateTime, doc="术后靶向治疗开始时间", name = '术后靶向治疗开始时间')
    bxzlym = Column(String(255), name = '术后靶向治疗具体药物')
    shfl = Column(Enum('是','否',''), name = '术后放疗')
    flkssj = Column(DateTime, doc="术后放疗开始时间", name = '术后放疗开始时间')
    flbz = Column(String(255), name = '术后放疗备注') 
    shmyzl = Column(Enum('是','否',''), name = '术后免疫治疗') 
    myzlsj = Column(DateTime, doc="术后免疫治疗开始时间", name = '术后免疫治疗开始时间')
    myzlbz = Column(String(255), name = '术后免疫治疗备注')



class relapseInformation(Base):
    """复发信息表"""
    
    __tablename__ = 'relapse_information'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    djcff = Column(Integer, name = '第几次复发')
    ffbw = Column(Enum('胸壁复发','保乳术后复发','同侧腋窝及锁上淋巴结复发','其他'), name = '复发部位') 
    jtffbw = Column(String(255), name = '具体复发部位') 
    ffrq = Column(DateTime, doc="复发日期", name = '复发日期')
    ffqzsd = Column(Enum('无','粗针吸穿刺','细针吸穿刺','开放活检'), name = '复发确诊手段') 
    ffbzblxx = Column(String(255), name = '复发病灶病理信息') 
    ffbzymzh = Column(String(255), name = '复发病灶免疫组化') 
    ffhzl = Column(String(1000), name = '复发后治疗') 
    ffxgpj = Column(Enum('CR','PR','SD','PD',''), name = '复发后治疗效果评价') 

class gene21Detection(Base):
    """gene21_detection"""
    
    __tablename__ = 'gene21_detection'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    sfjx21jyjc = Column( Enum('是','否'), name = '是否进行21基因检测') 
    jcsj = Column(DateTime, doc="检测时间", name = '检测时间')
    yjbh = Column(String(20), name = '研究编号') 
    jcry = Column(String(20), name = '检测人员') 
    bbwz = Column(String(50), name = '标本位置')
    bz = Column(String(100), name = '备注') 
    jtxq = Column(String(1000) , name = '具体详情')

class gene70Detection(Base):
    """gene70_detection"""
    
    __tablename__ = 'gene70_detection'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    sfjx70jyjc = Column( Enum('是','否'), name = '是否进行70基因检测') 
    jcsj = Column(DateTime, doc="检测时间", name = '检测时间')
    yjbh = Column(String(20), name = '研究编号') 
    jcry = Column(String(20), name = '检测人员') 
    bbwz = Column(String(50), name = '标本位置')
    bz = Column(String(100), name = '备注') 
    jtxq = Column(String(1000) , name = '具体详情')

class genebrcaDetection(Base):
    """genebrca_detection"""
    
    __tablename__ = 'genebrca_detection'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    sfjxbrcajyjc = Column( Enum('是','否'), name = '是否进行BRCA基因检测') 
    jcsj = Column(DateTime, doc="检测时间", name = '检测时间')
    yjbh = Column(String(20), name = '研究编号') 
    jcry = Column(String(20), name = '检测人员') 
    bbwz = Column(String(50), name = '标本位置')
    bz = Column(String(100), name = '备注') 
    jtxq = Column(String(1000) , name = '具体详情')

class peripheralBloodSampleSampling(Base):
    """peripheral_blood_sample_sampling"""
    
    __tablename__ = 'peripheral_blood_sample_sampling'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    bblx = Column(String(200), name = '标本类型') 
    cxsjd = Column(DateTime, doc="采血时间点", name = '采血时间点')
    cjr = Column(String(20), name = '采集人')
    cjbz = Column(String(100), name = '采集备注') 
    cjyt = Column( Enum('常规收集','课题'), name = '采集用途') 
    ybid = Column(String(255),  name = '标本编码')
    ybnum = Column(String(255),  name = '标本量')
    ybhbh = Column(String(255), doc='标本盒编码',name = '标本盒编码')
    ybcfwz = Column(String(255), doc='标本存放位置',name = '标本存放位置')
    sfqy = Column( Enum('是','否'), name = '是否取用') 
    qyrq = Column(DateTime, doc="取用日期", name = '取用日期')
    qyr = Column(String(20), doc='取用人',name = '取用人')
    qyyt = Column(String(255), doc='取用用途',name = '取用用途')
    qybz = Column(String(255), doc='取用备注',name = '取用备注')


class recorderInformation(Base):
    """recorder_information"""
    
    __tablename__ = 'recorder_information'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    sclrr = Column(String(255), name = '首次录入人') 
    sclrsj = Column(DateTime, doc="首次录入时间", name = '首次录入时间')
    mcsfr = Column(String(255), name = '末次随访人') 
    mcsfsj = Column(DateTime, doc="末次随访时间", name = '末次随访时间')

class recurrentDistantMetastasis(Base):
    """recurrent_distant_metastasis"""
    
    __tablename__ = 'recurrent_distant_metastasis'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    djczy = Column(Integer, name = '第几次转移')
    yzzybw = Column(String(255), name = '远处转移部位') 
    yczyrq = Column(DateTime, doc="远处转移日期", name = '远处转移日期')
    yczyqzsd = Column( Enum('无','粗针吸穿刺','细针吸穿刺','开放活检','手术'), name = '远处转移确诊手段') 
    yzzyblxx = Column(String(255), name = '远处转移病理信息') 
    yzzymyzh = Column(String(255), name = '远处转移免疫组化') 
    yczyzl = Column(String(200), name = '远处转移治疗') 
    yczyzlxgpj = Column(String(500), name = '远处转移治疗效果评价') 


class samplingRecurrenceMetastasisSpecimens(Base):
    """sampling_recurrence_metastasis_specimens"""
    
    __tablename__ = 'sampling_recurrence_metastasis_specimens'
    id = Column(BigInteger,  primary_key=True, name = '编号')
    bhzyid = Column(Integer, name = '滨海住院号')
    hxzyid = Column(Integer, name = '河西住院号')
    glbz = Column(String(200), name = '关联病灶') 
    cyrq = Column(DateTime, doc="采样日期", name = '采样日期')
    ytbz = Column(String(20), name = '用途标识')
    qtyt = Column(String(20), name = '其他用途')
    cjr = Column(String(20), name = '采集人')
    bblx = Column(String(100), name = '标本类型')
    bbxz = Column(String(255), name = '标本性质')
    ybid = Column(String(255),  name = '标本编码')
    ybnum = Column(String(255),  name = '标本量')
    ybhbh = Column(String(255), doc='标本盒编码',name = '标本盒编码')
    ybcfwz = Column(String(255), doc='标本存放位置',name = '标本存放位置')
    sfqy = Column( Enum('是','否'), name = '是否取用') 
    qyrq = Column(DateTime, doc="取用日期", name = '取用日期')
    qyr = Column(String(20), doc='取用人',name = '取用人')
    qyyt = Column(String(255), doc='取用用途',name = '取用用途')
    qybz = Column(String(255), doc='取用备注',name = '取用备注')
    