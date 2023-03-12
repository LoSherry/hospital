import os
import werkzeug
from flask import current_app
from flask_restplus import Namespace, Resource, fields, reqparse

from rptserver.services.patient import PatientService

_NS = Namespace('upload', description='上传文件')
_PatientService = PatientService()

@_NS.route('/patient')
class PatientUploadFile(Resource):
    """患者信息"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_patient(localpath)
        return data
    

@_NS.route('/patientHistory')
class PatientUploadFile(Resource):
    """个人史"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_patient_history(localpath)
        return data

@_NS.route('/familyHistory')
class PatientUploadFile(Resource):
    """家族史表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_family_history(localpath)
        return data

@_NS.route('/postoperativeTreatment')
class PatientUploadFile(Resource):
    """术后治疗"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_postoperative_treatment(localpath)
        return data

@_NS.route('/marryHistory')
class PatientUploadFile(Resource):
    """婚育史"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_patient_marry_history(localpath)
        return data

@_NS.route('/menstruation')
class PatientUploadFile(Resource):
    """月经表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_menstruation_history(localpath)
        return data

@_NS.route('/clinical')
class PatientUploadFile(Resource):
    """临床特征表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_clinical_feature(localpath)
        return data

@_NS.route('/recorder')
class PatientUploadFile(Resource):
    """记录人员信息表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_recorder_info(localpath)
        return data

@_NS.route('/recorder')
class PatientUploadFile(Resource):
    """记录人员信息表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_recorder_info(localpath)
        return data

@_NS.route('/gene21')
class PatientUploadFile(Resource):
    """21基因信息表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_gene21(localpath)
        return data

@_NS.route('/gene70')
class PatientUploadFile(Resource):
    """70基因信息表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_gene70(localpath)
        return data


@_NS.route('/genebrca')
class PatientUploadFile(Resource):
    """BRCA基因信息表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_genebrca(localpath)
        return data

@_NS.route('/patientFollow')
class PatientUploadFile(Resource):
    """病人跟踪记录表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_patient_follow(localpath)
        return data

@_NS.route('/peripheralBlood')
class PatientUploadFile(Resource):
    """外周血标本采样表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_peripheral_blood(localpath)
        return data

@_NS.route('/recurrent')
class PatientUploadFile(Resource):
    """远处转移信息表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_recurrent(localpath)
        return data

@_NS.route('/previousHistory')
class PatientUploadFile(Resource):
    """既往史表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_previous_history(localpath)
        return data

@_NS.route('/relapse')
class PatientUploadFile(Resource):
    """复发信息表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_relapse_info(localpath)
        return data

@_NS.route('/specimens')
class PatientUploadFile(Resource):
    """复发转移灶标本采样表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_specimens(localpath)
        return data

@_NS.route('/pathological')
class PatientUploadFile(Resource):
    """手术及病理信息表"""
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('list_file', type=werkzeug.datastructures.FileStorage,
                             location='files', help="批量导入文件", required=True)

    post_model = _NS.model('patientupLoadPostModel', {
        'message': fields.String(required=True, description='消息'),
        "status": fields.Integer(required=True, description="请求状态"),
        "valid_num": fields.Integer(required=True, description='有效数据数量')
    })
    
    @_NS.expect(post_parser)
    @_NS.marshal_with(post_model)
    def post(self):
        """批量上传"""
        args = self.post_parser.parse_args()
        list_file = args['list_file']
        localpath = os.path.join("rptserver\\resources", list_file.filename)
        list_file.save(localpath)
        data = _PatientService.batch_add_pathological(localpath)
        return data