# -*- coding: utf-8 -*-
{
    'name': "Sale Plugin",

    'summary': """Mofifies fields in sales""",

    'description': """This module modifies the sale document""",

    'author': "AtomX System",

    'website': "http://atomxsystem.eu",

    'category': 'Tools',

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'views/quotation_view.xml',
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
}