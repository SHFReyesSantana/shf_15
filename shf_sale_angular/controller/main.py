from odoo import http
from odoo.http import request
import logging
import pprint
_logger = logging.getLogger(__name__)
from urllib.parse import urlparse
import json


class WebHooks(http.Controller):
    @http.route(['/preview_sale_angular/<model("sale.order"):instance>'], type='http', auth="user",
                methods=['POST','GET'], website=True, csrf=True)
    def index(self,instance,**post):
        #request.make_response('',None,{'hi':'hola'})
        data = {
            'data': {
                'token': str(request.session.session_token) ,
                'id_sale':  instance.id ,
                'url': http.request.env['ir.config_parameter'].search([('key','=','web.base.url')]).value ,
                'tag_read' : 'read_sale_angular/'+str(instance.id) ,
                'tag_write' :  'write_sale_angular/'+str(instance.id) ,

            }

        }

        return http.request.render('shf_sale_angular.sale_index_angular',data)

    @http.route(['/read_sale_angular/<model("sale.order"):sale>'], type='http', auth="public", methods=['GET'], website=True, csrf=False)
    def index2(self, sale ,**kw):

        dx = {
            'id_sale': sale.id ,
            'name': sale.name ,
            'partner': sale.partner_id.name  ,
            'items': []
        }

        for l in sale.order_line:


            dx['items'].append(

                {
                    "id": l.id ,
                    "parentId": l.parent_section_id.id ,
                    #"selected": false,
                    "consecutive": str(l.sequence) ,
                    "data": {
                        "id": l.id ,
                        "type": "GROUP",
                        "description": "",
                        "name": "",
                        "brand": "",
                        "unitOfMeasurement": 0,
                        "taxes": [
                            {
                                "id": "1",
                                "name": "",
                                "value": 0
                            }
                        ],
                        "amount": 0,
                        "listPrice": 0,
                        "discountPercentage": 0,
                        "gainPercentage": 0,
                        "cost": 0,
                        "stock": 0 ,
                    }
                }
            )

        return json.dumps(dx)


