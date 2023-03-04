"""通用信息获取
"""
import logging
import traceback

from flask import g
from flask_jwt_extended import create_access_token, create_refresh_token

from rptserver.model.user import User
from ..tools.utils import to_md5
from ..tools.error import ParamsError, NoDataError

class UserService(object):
    
    def login(self, admin, password):
        """ 登录
        :param code: 用户名
        :param password: 用户密码
        """
        user = g.db_session.query(User).filter(User.admin == admin, User.password == to_md5(password)).first()
        
        if not user:
            raise ParamsError('用户名或密码错误, 请重试!')

        elif user.status != '正常':
            g.message = '运行@注销用户尝试登录@用户名:%s尝试登录系统,但用户状态非正常. 已拒绝' % code
            raise ParamsError('用户已被注销')

        else:
            g.message = '运行@登录系统@用户[%s]成功登录系统' % user.name

            data = {
                'admin': user.admin,
                'name': user.name,
                'status': user.status,
                'expire' : 60
            }

            # 创建token
            data['token'] = create_access_token(identity=data)
            
        g.user = data
        return data

    def add_user(self, admin, name , status, password):
        """新增用户

        Args:
            admin (str): 用户登陆账号
            name (str): 用户姓名
            status (str): 用户状态
            password (str): 密码
            
        """
        rst = {
            'message':"添加失败",
            "success" : False
        }
        try:
            if g.db_session.query(User).filter(User.admin == admin).first():
                raise ParamsError('新增失败，该用户已存在')
            user = User(name=name, admin=admin, status=status, password=to_md5(password))
            g.db_session.add(user)
            g.db_session.flush()
            g.db_session.commit()
            rst['id'] = user.id
            rst['status'] = 1
        except Exception as e:
            rst['message'] = "添加出错，错误原因【%s】"%e
            rst['status'] = 0
            logging.error(traceback.format_exc())
        finally:
            return rst
    
    def update_user(self,id, admin = None, name=None, status=None,password=None):
        """修改用户

        Args:
            id (int) :用户代码
            admin (str): 用户名
            name (str, optional): 用户名称. Defaults to None.
            status (str, optional): 用户状态. Defaults to None.
            password (str) : 用户密码
        """
        rst = {
            'id': id,
            "status" : 0
        }
        try:
            user = g.db_session.query(User).filter(User.id == id)
            if user.first() is None:
                raise ParamsError("更新失败，用户不存在或已删除")
            if admin is not None:
                user.update({'admin': admin})
            if name is not None:
                user.update({'name': name})
            if status is not None:
                user.update({'status': status})
            if password is not None:
                user.update({'password': to_md5(password)})
            # 修改角色
            g.db_session.commit()
            rst['message'], rst['status']= "更新成功", 1
        except Exception as e:
            g.db_session.rollback()
            logging.error(traceback.format_exc())
            rst['message'] = '更新失败，失败原因[%s]'%e
        finally:
            return rst