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
            #'partner': sale.partner_id.name  ,
            'partner': 'hola',
            'items': []
        }

        for l in sale.order_line:
            tax_ids = []
            #GROUP seccion
            #ORDER_LINE producto
            #OPTIONAL producto
            #ACTIVITY actividad
            #KITS kits

            type = 'GROUP' if l.display_type else 'ORDER_LINE'


            for tx in l.tax_id:
                tax_ids.append({
                                "id": str(tx.id),
                                "name":  str(tx.display_name),
                                "value":  tx.amount
                            })




            dx['items'].append(

                {
                    "id": l.id ,
                    "parentId": str(l.parent_section_id.id) if l.parent_section_i else None ,
                    #"selected": false,
                    "consecutive": str(l.sequence) ,
                    "data": {
                        "id": l.id ,
                        "type": type,
                        "description":  l.name,
                        "name": l.product_id.display_name if l.product_id else l.name,
                        "brand": "",
                        "unitOfMeasurement": 0,
                        "taxes": tax_ids,
                        "amount": l.product_uom_qty ,
                        "listPrice": l.price_unit,
                        "discountPercentage": 0,
                        "gainPercentage": 0,
                        "cost": 0,
                        "stock": 0 ,
                    }

                }

            )



        return json.dumps(dx['items'])


