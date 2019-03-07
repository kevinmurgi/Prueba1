# -*- coding: utf-8 -*-
{
    'name': "Veterinaria",

    'summary': """
        Módulo que gestiona una clinica veterinaria.""",

    'description': """
        Módulo creado por Kevin Martínez Leiva para la asignatura de Sistemas de Gestión Empresarial impartida por Gabriel Callejón.
    """,

    'author': "Kevin Martinez Leiva",
    'website': "www.iesmurgi.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
		'templates.xml',
		'data/defaultdata.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
