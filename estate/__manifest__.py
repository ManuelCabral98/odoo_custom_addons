{
    'name': 'Real Estate',
    'version': '1.0',
    'summary': 'Real Estate opportunities',
    'description': "",
    'depends': ['base'],
    'website': 'https://www.odoo.com/app/Real Estate',

    
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_user_views.xml',
        'views/estate_property_offers_views.xml',
        'views/estate_property_types_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_menus.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
