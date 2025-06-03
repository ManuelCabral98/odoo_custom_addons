{
    'name': 'Persona',
    'version': '1.0',
    'summary': 'Modulo para crear una Persona',
    'description': "",
    'depends': ['base','contacts'],
    'website': 'https://www.odoo.com/app/Persona',
    'data':[
        'security/ir.model.access.csv',
        'report/caracteristicas_report_action.xml',
        'report/caracteristicas_report_document.xml',
        'wizard/caracteristicas_report_wizard_document.xml',
        'wizard/caracteristicas_report_wizard_views.xml',
        'views/persona_views.xml',
        'views/caracteristicas_views.xml',
        'views/persona_menus.xml',
        'views/persona_user_views.xml',
        'views/caracteristicas_menu.xml',


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
