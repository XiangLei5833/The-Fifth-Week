"""定义 API 对应的 URL"""

from flask import Blueprint
from rmon.views.index import IndexView
<<<<<<< HEAD
from rmon.views.server import ServerList, ServerDetail

api = Blueprint('api', __name__)
api.add_url_rule('/', view_func=IndexView.as_view('index'))

api.add_url_rule('/servers/', view_func=ServerList.as_view('server_list'))
api.add_url_rule('/servers/<int:object_id>', 
        view_func=ServerDetail.as_view('server_detail'))
=======

api = Blueprint('api', __name__)
api.add_url_rule('/', view_func=IndexView.as_view('index'))
>>>>>>> origin/master
