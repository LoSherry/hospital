from flask_restplus import Namespace, Resource, fields, reqparse

from rptserver.services.sample import SampleService

_NS = Namespace('sample', description='样本信息')
_Service = SampleService()

@_NS.route('/use')
class SampleUseInfo(Resource):
    
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('qyid', help="取用编号", type=str, required=True)
    get_model = _NS.model("SampleUseGetModel", {
        'qyid' : fields.Integer(description='取用编号'),
        'ybid': fields.Integer(description='标本编码'),
        'qyrq' : fields.DateTime(description='取用日期'),
        'qyr' : fields.String(description="取用人"),
        'yt' : fields.String(description='用途'),
        'bz' : fields.String(description="备注"),
    })
    
    
    @_NS.expect(get_parser)
    @_NS.marshal_with(get_model)
    def get(self):
        args = self.get_parser.parse_args()
        data =  _Service.qry_sample_use_by_id(**args)
        return data


@_NS.route('/store')
class SampleStoreInfo(Resource):
    """SampleStore"""
    
    
    get_parser = reqparse.RequestParser()
    get_parser.add_argument('cfid', help="存放编号", type=str, required=True)
    get_model = _NS.model("SampleStoreGetModel", {
        'cfid' : fields.Integer(description='存放编号'),
        'ybid': fields.Integer(description='标本编码'),
        'ybnum' : fields.Integer(description='样本量'),
        'ybhbh' : fields.String(description="样本盒编号"),
        'ybcfwz' : fields.String(description='样本存放位置'),
    })
    
    
    @_NS.expect(get_parser)
    @_NS.marshal_with(get_model)
    def get(self):
        args = self.get_parser.parse_args()
        data =  _Service.qry_sample_store_by_id(**args)
        return data