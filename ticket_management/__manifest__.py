# -*- coding: utf-8 -*-
{
    'name': "Ticket Management",
    'summary': """This module provides ticket management""",
    'version': '0.1',
    'description': """This module provides ticket management""",
    'author': "AtomX System",
    'company': "AtomX System",
    'website': "http://atomxsystem.eu",
    'category': 'Tools',
    'depends': ['base', 'contacts', 'base_kanban_stage'],
    'data': [
        'security/ir.model.access.csv',

        'data/ticket_management_stage_data.xml',
        
        'views/views.xml',
        'views/stage_views.xml',
        'views/settings_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}