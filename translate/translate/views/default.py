from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

# from ..models import MyModel
from ..models import Users

# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         query = request.dbsession.query(Mymodel)
#         one = query.filter(Mymodel.name == 'one').first()
#     except DBAPIError:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'translate'}


@view_config(route_name='chameleon', renderer='../templates/sample.pt')
def chameleon_view(request):
    try:
        # query = request.dbsession.query(Users)
        # one = query.filter(Users.name == 'one').first()
        query = request.dbsession.query(Users).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    # return {'one': one, 'project': 'translate'}
    return {'query': query}

db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_translate_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
