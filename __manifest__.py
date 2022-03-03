# -*- coding: utf-8 -*-
{
    'name': "opencinema",

    'summary': """
        Almacena datos de peículas.
        """,

    'description': """
       Este módulo permite almacenar datos de las películas que van pasando por cartelera. Permite guardar el título, la descripción y el año de estreno.
    """,

    'author': "Sergio Fraga",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'application': 'true',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/opencinema.xml',
        'views/templates.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
