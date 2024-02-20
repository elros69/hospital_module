# -*- coding: utf-8 -*-
{
    'name': "HospitalModule",

    'summary': "Modulo creado la gestion de un hospital",

    'description': """
        Este modulo y sus funciones estan diseñados para poder getionar los datos de los pacientes y los
        doctores a su cargo.
    """,

    'author': "Abraham Campoy Garcia",
    'website': "https://github.com/elros69",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administracion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

