'''
    Rotas e endereços da aplicação
    \n/
    \n/download
    \n/consultar
'''

from wheezy.routing import url
from wheezy.web.handlers import file_handler

from views import MainHandler
from views import ConsultarHandler
from views import DownloadHandler

ROTAS = [
    url('', MainHandler, name='default'),
    url('download', DownloadHandler, name='download'),
    url('consultar', ConsultarHandler, name='consultar'),
    url('static/{path:any}', file_handler(
        root='src/static/'), name='static'),
]
