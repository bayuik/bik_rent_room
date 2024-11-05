{
    'name': "BIK | Rent Room",
    'summary': """

    """,
    'description': """


    """,
    'author': "Bayu Indra Kusuma",
    'website': "https://bayuik.dev",
    'category': 'BIK Module',
    'application': True,
    'version': '0.1',
    'depends': ['base'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/room_master_views.xml',
        'views/room_reservation_views.xml',
        'views/menuitems.xml',
    ]
}
