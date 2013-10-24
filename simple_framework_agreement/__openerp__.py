# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2013 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{'name': 'Simple Framework Agreement',
 'version': '0.1',
 'author': 'Camptocamp',
 'maintainer': 'Camptocamp',
 'category': 'Purchase Management',
 'complexity': 'normal',
 'depends': ['stock', 'purchase'],
 'description': """Simple implementation of Long Term Agreement
(or Framework Agreement) on price with supplier.


An agreement is set on a product or via a menu in the product configuration.
An agreement is defined by a product, a date range , a supplier, a price, a lead time
and agreed quantity.

There can be only one agreement for the same supplier product at the same time, even
if we may have different prices depending on lead time/qty.

If an agreement is running its price will be automatically used in PO.
A warning will be raised in case of exhaustion of override of agreement price.
""",
 'website': 'http://www.camptocamp.com',
 'data': ['data.xml',
          'security/multicompany.xml',
          'view/product_view.xml',
          'view/framework_agreement_view.xml',
          'view/purchase_view.xml'],
 'demo': [],
 'test': [],
 'installable': True,
 'auto_install': False,
 'license': 'AGPL-3',
 'application': False,
 }
