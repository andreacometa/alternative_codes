# -*- encoding: utf-8 -*-
##############################################################################
#
#    Personalizzazione realizzata da Francesco OpenCode Apruzzese (f.apruzzese@andreacometa.it)
#    Compatible with OpenERP release 6.1.X
#    Copyright (C) 2010 Andrea Cometa. All Rights Reserved.
#    Email: info@andreacometa.it, f.apruzzese@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##############################################################################

{
    'name': "alternative_code",
    'version': '0.1',
    'category': 'Product',
    'description': """
    ITA: Permette di associare ai prodotti, codici alternativi
    ENG: Now you can insert more codes for each product""",
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "depends" : ['product'],
    "init_xml" : [],
    "update_xml" : [
        'product/product_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        ],
    "demo_xml" : [],
    "active": False,
    "installable": True,
    "images" : ['images/image.png'],
}
