import json
import hashlib
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.exc import DBAPIError

from ..models.mymodel import(
    Users,
    Login,
    Language,
)

@view_config(route_name='login',request_method='GET', renderer='../templates/login.pt')
def translate_get(request):
    """ログイン画面"""
    try:
        result = request.dbsession.query(Login)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'query':''}

@view_config(route_name='login', request_method='POST', renderer='json')
def translate_post(request):
    login_model = request.dbsession.query(Login).filter(Login.email==request.params['email']).first()
    pass_hash = hashlib.sha1(login_model.password.encode('utf-8')).hexdigest()
    if login_model.password == request.params['password']:
        """pass_hashに変える"""
        print('success')
        return Response(json.dumps({'query':'register'}))
    else:
        print('エラー')

@view_config(route_name='register', request_method='GET', renderer='../templates/register.pt')
def register_view(request):
    return {}

@view_config(route_name='register', request_method='POST', renderer='../templates/register.pt')
def register_post(request):
    return {}

