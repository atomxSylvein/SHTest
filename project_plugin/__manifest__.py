# -*- coding: utf-8 -*-
{
    'name': "Project Plugin",

    'summary': """Add stages to projects""",

    'description': """This module adds 3 stages to the Project module""",

    'author': "AtomX System",

    'website': "http://atomxsystem.eu",

    'category': 'Tools',

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        #'views/kanban_view.xml',
        #'views/form_view.xml',
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
}