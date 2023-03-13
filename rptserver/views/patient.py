from flask_restplus import Namespace, Resource, fields, reqparse

from rptserver.services.patient import PatientService

_NS = Namespace('patient', description='病人信息')
_PatientService = PatientService()

@_NS.route('/info')
class PatientInfo(Resource):
    """patient"""
    
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('id', help="病人编号", type=int, required=True, default=None)
    
    
    @_NS.expect(get_parser)
    def get(self):
        args = self.get_parser.parse_args()
        data =  _PatientService.get_all_patient_info_by_id(**args)
        return data

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('name', help="姓名", type=str, required=True, default=None)
    post_parser.add_argument('phone1', help="联系电话1", type=str, required=True, default=None)
    post_parser.add_argument('phone2', help="联系电话2", type=str, required=True, default=None)
    post_parser.add_argument('sex', help="性别", type=str, required=True, choices=('男', '女'))
    post_parser.add_argument('marital_status', help="婚姻状况", type=str, required=True, choices=('已婚','未婚','离异','丧偶'))
    post_parser.add_argument('age', help="初诊年龄", type=int, default=None)
    post_parser.add_argument('mz', help="民族", type=str, required=False)
    post_parser.add_argument('job', help="职业", type=str, required=False)
    post_parser.add_argument('jg', help="籍贯", type=str, required=False)
    post_parser.add_argument('addr', help="现地址", type=str, required=False)
    post_parser.add_argument('fbDate', help="发现日期", type=str, required=False)
    post_parser.add_argument('ryDate', help="入院日期", type=str, required=False)
    post_parser.add_argument('cert_id', help="身份证号", type=str, required=True)
    post_parser.add_argument('birthday', help="出生日期", type=str, required=False)
    post_parser.add_argument('tall', help="身高", type=float, required=False)
    post_parser.add_argument('weight', help="体重", type=float, required=False)
    post_parser.add_argument('bmi', help="BMI", type=float, required=False)

    post_model = _NS.model('UsersPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 新增病人信息 '
        args = self.post_parser.parse_args()
        data = _PatientService.add_patient(**args)
        return data

@_NS.route('/bhzyinfo')
class PatientInfo2(Resource):
    """通过滨海住院号获取级别信息"""
   
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=True, default=None) 
    
    @_NS.expect(get_parser)
    def get(self):
        args = self.get_parser.parse_args()
        data =  _PatientService.get_all_patient_info_by_bhzyid(**args)
        return data

@_NS.route('/hxzyinfo')
class PatientInfo3(Resource):
    """通过河西住院号获取级别信息"""
   
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('hxzyid', help="河西住院号", type=int, required=True, default=None) 
    
    @_NS.expect(get_parser)
    def get(self):
        args = self.get_parser.parse_args()
        data =  _PatientService.get_all_patient_info_by_hxzyid(**args)
        return data

@_NS.route("/prehistory")
class PreviousHistory(Resource):
    """既往病史"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('rxlxjbs', help="乳腺良性疾病史", type=str, required=True, choices=('无','纤维腺瘤','增生性疾病','导管内乳头状瘤','炎症性疾病','其他'))
    post_parser.add_argument('rxlxjbsjtqk', help="乳腺良性疾病史具体情况", type=str, required=False)
    post_parser.add_argument('grxjb', help="感染性疾病", type=str, required=True)
    post_parser.add_argument('grxjbjtqk', help="感染性疾病具体情况", type=str, required=False)
    post_parser.add_argument('xgyxrq', help="新冠阳性日期", type=str, required=False)
    post_parser.add_argument('xgzyrq', help="新冠转阴日期", type=str, required=False)
    post_parser.add_argument('xtxjb', help="是否有系统疾病", type=str, required=True)
    post_parser.add_argument('sss', help="是否有手术史", type=str, required=True, choices=("是", "否"))
    post_parser.add_argument('sssjtqk', help="手术史具体情况", type=str, required=False)
    post_parser.add_argument('exzl', help="是否有恶性肿瘤既往史", type=str, required=True, choices=("是", "否"))
    post_parser.add_argument('exzljtqk', help="恶性肿瘤既往史具体情况", type=str, required=False)

    post_model = _NS.model('PreviousHistoryPostModel', {
        "status": fields.Integer(required=True, description="请求状态"),
        'message': fields.String(required=True, description='消息')
        
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 新增既往病史'
        args = self.post_parser.parse_args()
        data = _PatientService.add_previous_history(**args)
        return data

@_NS.route("/surgical")
class SurgicalInfo(Resource):
    """手术及病理信息"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('ssrq', help="手术日期", type=str, required=False)
    post_parser.add_argument('ssfs', help="手术方式", type=str, required=False)
    post_parser.add_argument('sfbr', help="是否保乳", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('sfzz', help="是否再造", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('ywlbqsfs', help="腋窝淋巴结清扫方式", type=str, required=True, choices=('腋清','前哨淋巴结活检'))
    post_parser.add_argument('shdblh', help="术后大病理号", type=str, required=False)
    post_parser.add_argument('bzsl', help="病灶数量", type=int, required=False, default=None)
    post_parser.add_argument('ryzwdx', help="肉眼肿物大小", type=str, required=False)
    post_parser.add_argument('blxfq', help="病理学分期", type=str, required=False)
    post_parser.add_argument('bllx', help="病理类型", type=str, required=True, choices=('导管内癌','小叶原位癌','乳头湿疹样乳腺癌','浸润性导管癌','浸润性小叶癌','浸润性特殊癌','其他'))
    post_parser.add_argument('blxjtms', help="病理具体描述", type=str, required=False)
    post_parser.add_argument('zzxfj', help="组织学分级", type=str, required=True, choices=('I','II','III','I-II','II-III','其他'))
    post_parser.add_argument('zzxfjjtqk', help="组织学分级具体情况", type=str, required=False)
    post_parser.add_argument('lbxgqf', help="淋巴血管侵犯与否", type=str, required=False)
    post_parser.add_argument('lbgbs', help="淋巴管癌栓", type=str, required=True, choices=('有','无'))
    post_parser.add_argument('jzznqrlbxb', help="间质内浸润淋巴细胞", type=str, required=False)
    post_parser.add_argument('hlfy', help="化疗反应", type=str, required=False)
    post_parser.add_argument('brsskjazz', help="保乳手术标本周断端是否可见癌组织", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('brssbbzdd', help="保乳手术标本周断端", type=str, required=False)
    post_parser.add_argument('brssbbbqzdd', help="保乳手术标本补切周断端", type=str, required=False)

    post_parser.add_argument('lbjqk', help="淋巴结情况", type=str, required=False)
    post_parser.add_argument('ywlbzs', help="腋窝淋巴结总数", type=int, required=False)
    post_parser.add_argument('yxywlbzs', help="阳性腋窝淋巴结数", type=int, required=False)

    post_parser.add_argument('er', help="ER", type=str, required=False)
    post_parser.add_argument('pr', help="PR", type=str, required=False)

    post_parser.add_argument('her2', help="HER2", type=str, required=True, choices=('阴性','1+','2+','3+','其他'))
    post_parser.add_argument('her2jtqk', help="her2具体情况", type=str, required=False)
    post_parser.add_argument('ki67', help="Ki67", type=str, required=False)
    post_parser.add_argument('p53', help="P53", type=str, required=False)
    post_parser.add_argument('fish', help="FISH", type=str, required=True, choices=('阴性','阳性','其他'))
    post_parser.add_argument('fishjtqk', help="FISH具体情况", type=str, required=False)
    post_parser.add_argument('hfc', help="HER2-FISH COPY数", type=str, required=False)
    post_parser.add_argument('hfr', help="HER2-FISH RATIO", type=str, required=False)
    post_model = _NS.model('SurgicalInfoPostModel', {
        'message': fields.String(required=True, description='消息'),
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 新增手术及病理信息'
        args = self.post_parser.parse_args()
        data = _PatientService.add_surgical_pathological_info(**args)
        return data

@_NS.route("/familyhistory")
class familyHistory(Resource):
    """家族史表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('wxzl', help="是否有恶性肿瘤家族史", type=str, required=True,choices=('是','否'))
    post_parser.add_argument('rxa', help="乳腺癌家族史", type=str, required=False,choices=('是','否'))
    post_parser.add_argument('lca', help="卵巢癌家族史", type=str, required=False,choices=('是','否'))
    post_parser.add_argument('qtwxzl', help="其他恶性肿瘤家族史", type=str, required=True ,choices=('是','否'))
    post_parser.add_argument('qtwxzljtqk', help="其他恶性肿瘤家族史具体情况", type=str, required=False)
    post_parser.add_argument('xqs', help="x级亲属", type=str, required=False)

    post_model = _NS.model('familyHistoryPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 新增家族史表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_family_history(**args)
        return data

@_NS.route("/pathistory")
class patientHistory(Resource):
    """个人史表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('sfxy', help="是否吸烟", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('jtxyl', help="具体吸烟量", type=str, required=False)
    post_parser.add_argument('sfyj', help="是否饮酒", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('jtyjl', help="具体饮酒量", type=str, required=False)


    post_model = _NS.model('patientHistoryPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        '新增个人史表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_patient_history(**args)
        return data

@_NS.route("clinicalFeature")
class clinicalFeature(Resource):
    """临床特征表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('fxwz', help="发现方式", type=str, required=True, choices=('自查','体检','其他'))
    post_parser.add_argument('zkwz', help="肿瘤位置", type=str, required=True, choices=('右乳','左乳','双乳'))
    post_parser.add_argument('lcsfzz', help="有无临床首发症状", type=str, required=True, choices=('肿块','乳头溢液','其他首发症状'))
    post_parser.add_argument('sfzzjtms', help="首发症状具体描述", type=str, required=False)
    post_parser.add_argument('hcrt', help="患侧乳头", type=str, required=True, choices=('正常','凹陷','半固定','固定','湿疹样','乳头皴裂','乳头缺如','其他'))
    post_parser.add_argument('hcrtjtms', help="患侧乳头症状具体描述", type=str, required=False)
    post_parser.add_argument('hcpf', help="患侧皮肤", type=str, required=True, choices=('正常','水肿','卫星结节','破溃','桔皮样变','炎样红肿','静脉曲张','其他'))
    post_parser.add_argument('hcpfjtms', help="患侧皮肤症状具体描述", type=str, required=False)
    post_parser.add_argument('rtyy', help="乳头溢液", type=str, required=True, choices=('自发','非自发'))
    post_parser.add_argument('yydg', help="溢液导管", type=str, required=True, choices=('左侧','右侧','单个','多个'))
    post_parser.add_argument('yyxz', help="溢液性质", type=str, required=True, choices=('陈旧血性','新鲜血性','淡黄','乳汁样','水样','脓性','其他'))
    post_parser.add_argument('yyxzjtms', help="溢液性质具体描述", type=str, required=False)
    
    post_parser.add_argument('yxjclx', help="影像检查类型", type=str, required=True, choices=('b超','钼靶','核磁'))
    post_parser.add_argument('yxjch', help="影像检查号", type=str, required=True)
    post_parser.add_argument('sqzldx', help="术前影像肿瘤大小", type=str, required=False)
    post_parser.add_argument('sqtfq', help="术前T分期", type=str, required=False)
    post_parser.add_argument('sqyxlbjwz', help="术前影像腋下淋巴结位置", type=str, required=True, choices=('腋下Ⅰ水平','腋下Ⅱ水平','腋窝Ⅲ水平','锁骨下','锁骨上','乳内淋巴结'))
    post_parser.add_argument('sqyxlbjdx', help="术前影像腋下淋巴结大小", type=str, required=False)
    post_parser.add_argument('sqnfq', help="术前N分期", type=str, required=False)
    post_parser.add_argument('yczy', help="远处转移与否", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('zybw', help="转移部位", type=str, required=True, choices=('肝','肺','骨','脑','其他'))
    post_parser.add_argument('jtzybw', help="具体转移部位", type=str, required=False)
    post_parser.add_argument('tnm', help="临床TNM分期", type=str, required=False)
    post_parser.add_argument('zlbzqzfs', help="肿瘤病灶确诊方式", type=str, required=True, choices=('术前开放活检','术中开放活检','穿刺粗针吸','穿刺细针吸'))
    post_parser.add_argument('lbjqzfs', help="确诊方式", type=str, required=True, choices=('无','粗针吸','细针吸','术前淋巴结活检'))
    post_parser.add_argument('qzblh', help="确诊病理信息", type=str, required=False)
    post_parser.add_argument('sfxmyzh', help="是否行免疫组化", type=str, required=True, choices=('是','否'))
    
    post_parser.add_argument('er', help="肿瘤病灶穿刺ER", type=str, required=False)
    post_parser.add_argument('pr', help="肿瘤病灶穿刺PR", type=str, required=False)
    post_parser.add_argument('her2', help="肿瘤病灶穿刺Her2", type=str, required=True, choices=('阴性','1+','2+','3+','其他'))
    post_parser.add_argument('her2jtqk', help="肿瘤病灶穿刺Her2具体情况", type=str, required=False)
    post_parser.add_argument('ki67', help="肿瘤病灶穿刺Ki67", type=str, required=False)
    post_parser.add_argument('p53', help="肿瘤病灶穿刺P53", type=str, required=False)
    post_parser.add_argument('fish', help="肿瘤病灶FISH", type=str, required=True, choices=('阴性','阳性','其他'))
    post_parser.add_argument('fishjtqk', help="肿瘤病灶FISH具体情况", type=str, required=False)
    post_parser.add_argument('fcopy', help="肿瘤病灶FISH copy数", type=str, required=False)
    post_parser.add_argument('fratio', help="肿瘤病灶FISH ratio", type=str, required=False)

    post_parser.add_argument('ywlbjer', help="腋窝淋巴结穿刺ER", type=str, required=False)
    post_parser.add_argument('ywlbjpr', help="腋窝淋巴结穿刺PR", type=str, required=False)
    post_parser.add_argument('ywlbjher2', help="腋窝淋巴结穿刺Her2", type=str, required=True, choices=('阴性','1+','2+','3+','其他'))
    post_parser.add_argument('ywlbjher2jtqk', help="腋窝淋巴结穿刺Her2具体情况", type=str, required=False)
    post_parser.add_argument('ywlbjki67', help="腋窝淋巴结穿刺Ki67", type=str, required=False)
    post_parser.add_argument('ywlbjp53', help="腋窝淋巴结穿刺P53", type=str, required=False)
    post_parser.add_argument('ywlbjfish', help="腋窝淋巴结FISH", type=str, required=True, choices=('阴性','阳性','其他'))
    post_parser.add_argument('ywlbjfishjtqk', help="腋窝淋巴结FISH具体情况", type=str, required=False)
    post_parser.add_argument('ywlbjfcopy', help="腋窝淋巴结FISH copy数", type=str, required=False)
    post_parser.add_argument('ywlbjfratio', help="腋窝淋巴结FISH ratio", type=str, required=False)
    
    post_parser.add_argument('jblbjer', help="颈部淋巴结穿刺ER", type=str, required=False)
    post_parser.add_argument('jblbjpr', help="颈部淋巴结穿刺PR", type=str, required=False)
    post_parser.add_argument('jblbjher2', help="颈部淋巴结穿刺Her2", type=str, required=True, choices=('阴性','1+','2+','3+','其他'))
    post_parser.add_argument('jblbjher2jtqk', help="颈部淋巴结穿刺Her2具体情况", type=str, required=False)
    post_parser.add_argument('jblbjki67', help="颈部淋巴结穿刺Ki67", type=str, required=False)
    post_parser.add_argument('jblbjp53', help="颈部淋巴结穿刺P53", type=str, required=False)
    post_parser.add_argument('jblbjfish', help="颈部淋巴结FISH", type=str, required=True, choices=('阴性','阳性','其他'))
    post_parser.add_argument('jblbjfishjtqk', help="颈部淋巴结FISH具体情况", type=str, required=False)
    post_parser.add_argument('jblbjfcopy', help="颈部淋巴结FISHcopy数", type=str, required=False)
    post_parser.add_argument('jblbjfratio', help="颈部淋巴结FISHratio", type=str, required=False)

    post_parser.add_argument('yczyqzbw', help="远处转移确诊部位", type=str, required=False)
    post_parser.add_argument('yczyer', help="远处转移灶ER", type=str, required=False)
    post_parser.add_argument('yczypr', help="远处转移灶PR", type=str, required=False)
    post_parser.add_argument('yczyher2', help="远处转移灶Her2", type=str, required=True, choices=('阴性','1+','2+','3+','其他'))
    post_parser.add_argument('yczyher2jtqk', help="远处转移灶Her2具体情况", type=str, required=False)
    post_parser.add_argument('yczyki67', help="远处转移灶Ki67", type=str, required=False)
    post_parser.add_argument('yczyp53', help="远处转移灶P53", type=str, required=False)
    post_parser.add_argument('yczyfish', help="远处转移灶FISH", type=str, required=True, choices=('阴性','阳性','其他'))
    post_parser.add_argument('yczyfishjtqk', help="远处转移灶FISH具体情况", type=str, required=False)
    post_parser.add_argument('yczyfcopy', help="远处转移灶FISH copy数", type=str, required=False)
    post_parser.add_argument('yczyfratio', help="远处转移灶FISH ratio", type=str, required=False)

    post_parser.add_argument('xfzzl', help="术前是否行新辅助治疗", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('xfzzlkssj', help="新辅助治疗开始时间", type=str, required=False)
    post_parser.add_argument('xfzzlfa', help="新辅助治疗方案及周期", type=str, required=False)
    post_parser.add_argument('xfzlc', help="新辅助治疗期间是否使用卵巢功能抑制剂", type=str, required=False,choices=('是','否'))
    post_parser.add_argument('xfzlcyw', help="新辅助治疗卵巢功能抑制剂具体药物名称", type=str, required=False)
    post_parser.add_argument('xfzzlpg', help="新辅助治疗过程评估", type=str, required=False)
    post_parser.add_argument('xfzzlpj', help="新辅助治疗疗效评价", type=str, required=True, choices=('CR','PR','SD','PD'))

    post_parser.add_argument('jjzl', help="术前是否行解救治疗", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('sqzlkssj', help="术前解救治疗开始时间", type=str, required=False)
    post_parser.add_argument('sqzlfa', help="术前解救治疗方案及周期", type=str, required=False)
    post_parser.add_argument('jjlc', help="术前解救治疗期间是否使用卵巢功能抑制剂", type=str, required=False,choices=('是','否'))
    post_parser.add_argument('jjlcyw', help="术前解救治疗卵巢功能抑制剂具体药物名称", type=str, required=False)
    post_parser.add_argument('sqzlpg', help="术前解救治疗过程评估", type=str, required=False)
    post_parser.add_argument('sqzlpj', help="术前解救治疗疗效评价", type=str, required=True, choices=('CR','PR','SD','PD'))

    post_model = _NS.model('clinicalFeaturePostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 临床特征表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_clinical_feature(**args)
        return data

@_NS.route("/pmhistory")
class patientHistory(Resource):
    """月经史表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('ccage', help="初潮年龄", type=str, required=False, default=None)
    post_parser.add_argument('yjzq', help="月经周期", type=str, required=False, default=None)  
    post_parser.add_argument('jq', help="经期", type=str, required=False, default=None)  

    post_parser.add_argument('sfjj', help="是否绝经", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('jjfs', help="绝经方式", type=str, required=True, choices=('自然','人工','其他'))
    post_parser.add_argument('jtjjfs', help="具体绝经方式", type=str, required=False)
    post_parser.add_argument('mqyj', help="末次月经", type=str, required=False)
    post_parser.add_argument('jjage', help="绝经年龄", type=str, required=False, default=None)


    post_model = _NS.model('patientMenstruationHistoryPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 月经史表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_patient_menstruation_history(**args)
        return data

@_NS.route("/marryhistory")
class patientMarryHistory(Resource):
    """婚育史表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('sy', help="生育", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('qzssyzt', help="确诊时生育状态", type=str, required=True, choices=('无','哺乳期','妊娠期'))

    post_parser.add_argument('ccage', help="初产年龄", type=str, required=False, default=None)
    post_parser.add_argument('mtage', help="末胎年龄", type=str, required=False, default=None)
    post_parser.add_argument('hycs', help="怀孕次数", type=str, required=False, default=None)
    post_parser.add_argument('zyc', help="足月产", type=str, required=False)
    post_parser.add_argument('lczcs', help="流产或早产史", type=str, required=True)
    post_parser.add_argument('fzsy', help="是否辅助生育", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('fzsyfs', help="辅助生育方式", type=str, required=False)
    post_parser.add_argument('sfmrwy', help="是否母乳喂养", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('mrcb', help="哺乳侧别", type=str, required=False, choices=('左','右','双'))
    post_parser.add_argument('mrsc', help="哺乳时长", type=str, required=False)


    post_model = _NS.model('patientMarryHistoryPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 婚育史表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_patient_marry_history(**args)
        return data

@_NS.route("/patfollow")
class patientFollow(Resource):
    """病人跟踪记录表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('dfs', help="DFS", type=str, required=False)
    post_parser.add_argument('os', help="OS", type=str, required=False)
    post_parser.add_argument('mcfcsj', help="末次复查时间（截止查病历时/电话随诊）", type=str, required=False)
    post_parser.add_argument('syqk', help="治疗后生育情况", type=str, required=False)
    post_parser.add_argument('syfaz', help="双原发癌症", type=str, required=True, choices=('无','对侧乳腺','非同侧胸壁','区域淋巴结','其他原发癌'))
    post_parser.add_argument('syfazjtxq', help="双原发癌症具体详情", type=str, required=False)
    post_parser.add_argument('zhsfsj', help="双原发癌症首次发生时间", type=str, required=False)
    post_parser.add_argument('sfbz', help="随访备注", type=str, required=False)
    post_parser.add_argument('swyf', help="死亡与否", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('swsj', help="死亡时间", type=str, required=False)
    post_parser.add_argument('sy', help="死因", type=str, required=False, choices=('肿瘤','非肿瘤','其他'))
    post_parser.add_argument('jtsy', help="具体死因", type=str, required=False)

    post_model = _NS.model('patientFollowPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 病人跟踪记录表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_patient_follow(**args)
        return data

@_NS.route("/postoper")
class postoperativeTreatment(Resource):
    """术后治疗表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('shhl', help="术后化疗", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('hlkssj', help="术后化疗开始时间", type=str, required=False)
    post_parser.add_argument('shhlfam', help="术后化疗方案", type=str, required=False)
    post_parser.add_argument('hllc', help="术前解救治疗期间是否使用卵巢功能抑制剂", type=str, required=False,choices=('是','否'))
    post_parser.add_argument('hllcyw', help="术前解救治疗卵巢功能抑制剂具体药物名称", type=str, required=False)
    post_parser.add_argument('shhlxq', help="术后化疗详情", type=str, required=False)
    post_parser.add_argument('shnfmzl', help="术后内分泌治疗", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('nfmzlkssj', help="术后内分泌治疗开始时间", type=str, required=False)
    post_parser.add_argument('nfmzlym', help="术后内分泌治疗药物", type=str, required=False)
    post_parser.add_argument('nfmzlfzy', help="内分泌治疗副作用", type=str, required=False)
    post_parser.add_argument('shbxzl', help="是否术后靶向治疗", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('bxzlkssj', help="术后靶向治疗开始时间", type=str, required=False)
    post_parser.add_argument('bxzlym', help="术后靶向治疗具体药物", type=str, required=False)
    post_parser.add_argument('shfl', help="术后放疗", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('flkssj', help="术后放疗开始时间", type=str, required=False)
    post_parser.add_argument('flbz', help="术后放疗备注", type=str, required=False)
    post_parser.add_argument('shmyzl', help="术后免疫治疗", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('hlsj', help="术后免疫治疗开始时间", type=str, required=False)
    post_parser.add_argument('myzlbz', help="术后免疫治疗备注", type=str, required=False)


    post_model = _NS.model('postoperativeTreatmentPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 术后治疗表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_postoperative_treatment(**args)
        return data

@_NS.route("/relapse")
class relapseInformation(Resource):
    """复发信息表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('djcff', help="第几次复发", type=int, required=True, default=None)
    post_parser.add_argument('ffbw', help="复发部位", type=str, required=True, choices=('胸壁复发','保乳术后复发','同侧腋窝及锁上淋巴结复发','其他'))
    post_parser.add_argument('jtffbw', help="具体复发部位", type=str, required=False)
    post_parser.add_argument('ffrq', help="复发日期", type=str, required=False)
    post_parser.add_argument('ffqzsd', help="复发确诊手段", type=str, required=True, choices=('无','粗针吸穿刺','细针吸穿刺','开放活检'))

    post_parser.add_argument('ffbzblxx', help="复发病灶病理信息", type=str, required=False)
    post_parser.add_argument('ffbzymzh', help="复发病灶免疫组化", type=str, required=False)
    post_parser.add_argument('ffhzl', help="复发后治疗", type=str, required=False)
    post_parser.add_argument('ffxgpj', help="复发后治疗效果评价", type=str, required=True, choices=('CR','PR','SD','PD',''))
    

    post_model = _NS.model('relapseInformationPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        ' 复发信息表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_relapse_information(**args)
        return data

@_NS.route("/gene21detect")
class gene21Detection(Resource):
    """21基因信息表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('sfjx21jyjc', help="是否进行21基因检测", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('jcsj', help="检测时间", type=str, required=False)
    post_parser.add_argument('yjbh', help="研究编号", type=str, required=False)

    post_parser.add_argument('jcry', help="检测人员", type=str, required=False)
    post_parser.add_argument('bbwz', help="标本位置", type=str, required=False)
    post_parser.add_argument('bz', help="备注", type=str, required=False)
    post_parser.add_argument('jtxq', help="具体详情", type=str, required=True)
    

    post_model = _NS.model('gene21DetectionPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        '21基因信息表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_gene21_detection(**args)
        return data 

@_NS.route("/gene70detect")
class gene70Detection(Resource):
    """70基因信息表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('sfjx70jyjc', help="是否进行70基因检测", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('jcsj', help="检测时间", type=str, required=False)
    post_parser.add_argument('yjbh', help="研究编号", type=str, required=False)

    post_parser.add_argument('jcry', help="检测人员", type=str, required=False)
    post_parser.add_argument('bbwz', help="标本位置", type=str, required=False)
    post_parser.add_argument('bz', help="备注", type=str, required=False)
    post_parser.add_argument('jtxq', help="具体详情", type=str, required=True)
    

    post_model = _NS.model('gene70DetectionPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        '70基因信息表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_gene70_detection(**args)
        return data 
    
@_NS.route("/genebrcadetect")
class genebrcaDetection(Resource):
    """brca基因信息表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('sfjxbrcajyjc', help="是否进行BRCA基因检测", type=str, required=True, choices=('是','否'))
    post_parser.add_argument('jcsj', help="检测时间", type=str, required=False)
    post_parser.add_argument('yjbh', help="研究编号", type=str, required=False)

    post_parser.add_argument('jcry', help="检测人员", type=str, required=False)
    post_parser.add_argument('bbwz', help="标本位置", type=str, required=False)
    post_parser.add_argument('bz', help="备注", type=str, required=False)
    post_parser.add_argument('jtxq', help="具体详情", type=str, required=True)
    

    post_model = _NS.model('genebrcaDetectionPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        'brca基因信息表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_genebrca_detection(**args)
        return data 

@_NS.route("/blood")
class BloodSampleSampling(Resource):
    """外周血标本采样表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('bblx', help="标本类型", type=str, required=True)
    post_parser.add_argument('cxsjd', help="采血时间点", type=str, required=False)
    post_parser.add_argument('cjr', help="采集人", type=str, required=False)
    post_parser.add_argument('cjbz', help="采集备注", type=str, required=False)
    post_parser.add_argument('cjyt', help="采集用途", type=str, required=False,choices=('常规收集','课题'))

    post_parser.add_argument('ybid', help="标本编码", type=str, required=False)
    post_parser.add_argument('ybnum', help="标本量", type=str, required=False)
    post_parser.add_argument('ybhbh', help="标本盒编码", type=str, required=False)
    post_parser.add_argument('ybcfwz', help="标本存放位置", type=str, required=False)
    post_parser.add_argument('sfqy', help="是否取用", type=str, required=False,choices=('是','否'))
    post_parser.add_argument('qyrq', help="取用日期", type=str, required=False)
    post_parser.add_argument('qyr', help="取用人", type=str, required=False)
    post_parser.add_argument('qyyt', help="取用用途", type=str, required=False)
    post_parser.add_argument('qybz', help="取用备注", type=str, required=False)


    post_model = _NS.model('bloodSampleSamplingPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        '外周血标本采样表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_peripheral_blood_sample_sampling(**args)
        return data 

@_NS.route("/recorder")
class recorderInformation(Resource):
    """记录人员信息表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('sclrr', help="首次录入人", type=str, required=True)
    post_parser.add_argument('sclrsj', help="首次录入时间", type=str, required=False)
    post_parser.add_argument('mcsfr', help="末次随访人", type=str, required=False)
    post_parser.add_argument('mcsfsj', help="末次随访时间", type=str, required=False)
    
    post_model = _NS.model('recorderInformationPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        '记录人员信息表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_recorder_information(**args)
        return data 

@_NS.route("/recurrent")
class recurrentDistantMetastasis(Resource):
    """远处转移信息表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('djczy', help="第几次转移", type=int, required=True)
    post_parser.add_argument('yzzybw', help="远处转移部位", type=str, required=False)
    post_parser.add_argument('yczyrq', help="远处转移日期", type=str, required=False)
    post_parser.add_argument('yczyzl', help="远处转移确诊手段", type=str, required=False)
    post_parser.add_argument('yzzyblxx', help="远处转移病理信息", type=str, required=False)
    post_parser.add_argument('yzzymyzh', help="远处转移免疫组化", type=str, required=False)
    post_parser.add_argument('yczyzl', help="远处转移治疗", type=str, required=False)
    post_parser.add_argument('yczyzlxgpj', help="远处转移治疗效果评价", type=str, required=False)
    post_model = _NS.model('recurrentDistantMetastasisPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        '远处转移信息表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_recurrent_distant_metastasis(**args)
        return data 

@_NS.route("/specimens")
class samplingRecurrenceMetastasisSpecimens(Resource):
    """复发转移灶标本采样表"""

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('bhzyid', help="滨海住院号", type=int, required=False, default=None)
    post_parser.add_argument('hxzyid', help="河西住院号", type=int, required=False, default=None)
    post_parser.add_argument('glbz', help="关联病灶", type=str, required=False)
    post_parser.add_argument('cyrq', help="采样日期", type=str, required=False)
    post_parser.add_argument('ytbz', help="用途标识", type=str, required=False)
    post_parser.add_argument('qtyt', help="其他用途", type=str, required=False)

    post_parser.add_argument('cjr', help="采集人", type=str, required=False)
    post_parser.add_argument('bblx', help="标本类型", type=str, required=False)
    post_parser.add_argument('bbxz', help="标本性质", type=str, required=False)
    post_parser.add_argument('ybid', help="标本编码", type=str, required=False)
    post_parser.add_argument('ybnum', help="标本量", type=str, required=False)
    post_parser.add_argument('ybhbh', help="标本盒编码", type=str, required=False)
    post_parser.add_argument('ybcfwz', help="标本存放位置", type=str, required=False)
    post_parser.add_argument('sfqy', help="是否取用", type=str, required=False,choices=('是','否'))
    post_parser.add_argument('qyrq', help="取用日期", type=str, required=False)
    post_parser.add_argument('qyr', help="取用人", type=str, required=False)
    post_parser.add_argument('qyyt', help="取用用途", type=str, required=False)
    post_parser.add_argument('qybz', help="取用备注", type=str, required=False)

    post_model = _NS.model('RecurrenceMetastasisSpecimensPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态")
    })

    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        '复发转移灶标本采样表'
        args = self.post_parser.parse_args()
        data = _PatientService.add_sampling_recurrence_metastasis_specimens(**args)
        return data