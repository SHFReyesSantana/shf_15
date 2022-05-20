from odoo import http
from odoo.http import request
import logging
import pprint
_logger = logging.getLogger(__name__)
from urllib.parse import urlparse


class WebHooks(http.Controller):
    @http.route(['/preview_sale_angular/<model("sale.order"):instance>'], type='http', auth="user",
                methods=['POST','GET'], website=True, csrf=True)
    def index(self,instance,**post):
        #request.make_response('',None,{'hi':'hola'})
        data = {
            'data': {
                'token': str(request.session.session_token) ,
                'id_sale':  instance.id
            }

        }

        return http.request.render('shf_sale_angular.sale_index_angular',data)
        #data = http.request.jsonrequest
        #_logger.info('creacion del producto %s', pprint.pformat(data))
        #http.request.env['woo.synchro'].sudo().hook(data,instance,'products')



