# -*- coding: utf-8 -*-
# Part of Xavik Solutions. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2024-2025 Xavik Solutions, Xavier Orlov (<https://xavik.solutions>).

{
    'name': 'WooCommerce Odoo Connector [FREE]',
    'summary': 'Free bi-directional synchronization of products, orders, and stock between Odoo and WooCommerce.',
    'description': """
WooCommerce Odoo Connector (Community Edition)
==============================================
This module provides a seamless integration between your WooCommerce online store and Odoo 17, centralizing your business management in a single platform.

**Message to the Odoo Community:**
We believe in the power of open-source collaboration. This module is our contribution to help small businesses and developers grow their ecosystem without initial barriers. Enjoy, share, and improve it!

Key Features:
-------------
* **Product Synchronization:** Effortlessly import and export products, categories, and variants.
* **Inventory Management:** Real-time automatic stock level updates from Odoo to WooCommerce.
* **Order Automation:** Web orders are automatically created as Quotations or Sales Orders in Odoo.
* **Customer Sync:** Synchronization of customer billing and shipping information.
* **Multi-Instance Support:** Capability to connect multiple WooCommerce stores to a single Odoo database.

Streamline your operations and eliminate data duplication with this robust technical solution.
    """,
    'author': 'Xavik Solutions, Xavier Orlov',
    'website': 'https://xavik.solutions',
    'category': 'Technical',
    'version': '17.0.1.0.0',
    'depends': ['base', 'web', 'sale_management', 'stock'],
    'external_dependencies': {
        'python': ['woocommerce'],
    },
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}