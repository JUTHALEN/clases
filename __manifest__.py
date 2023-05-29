# -*- coding: utf-8 -*-
{
    'name': "clases",

    'summary': "Clases particulares",

    'description': "Gestión de clases particulares.",

    'author': "Judith Alende Martínez",
    'website': "https://ead.murciaeduca.es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Academia',
    'version': '1.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
