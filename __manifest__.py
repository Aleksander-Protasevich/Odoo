# -*- coding: utf-8 -*-
{
    'name' : 'Test Task',
    'version' : '1.1',
    'summary': 'Product Manufacturer & Model',
    'sequence': 10,
    'description': """Product manufacturer and model""",
    'category': 'Sales/Sales',
    'depends' : ['product'],
    'data': [
        'views\product_manufacturer_menu.xml',
        'views\product_model_menu.xml',
        # 'views\product_template_manufacturer.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
