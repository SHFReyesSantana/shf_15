# -*- encoding: utf-8 -*-
{
    'name': 'Sale with Angular Design',
    'category': 'uncategorize',
    'author': 'ITGRUPO',
    'depends': ['sale_management'],
    'version': '1.0',
    'description':"""
     Descripcion
    """,
    'auto_install': False,
    'demo': [],
    'data': [
        #'security/security.xml',
        'views/sale_order.xml',
        'views/template_index.xml',
        ],
    'assets':{
        'web.assets_backend':[
            'shf_sale_angular/static/src/js/section_field.js',
            'shf_sale_angular/static/src/scss/section.scss',
        ],
    },
    'installable': True
}