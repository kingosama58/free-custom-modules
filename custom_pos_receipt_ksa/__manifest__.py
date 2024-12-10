# -*- coding: utf-8 -*-
################################################################################
#
#    AccountTechs
#
#    Copyright (C) 2024-TODAY AccountTechs (<https://wa.me/966553493285>).
#    Author: Your Name (<osamahalnihmi@gmail.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
################################################################################

{
    'name': 'KSA Custom POS Receipt',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Customize POS receipts for KSA compliance.',
    'description': """
        This module provides a customized POS receipt template tailored for KSA compliance, 
        including VAT and other required details.
    """,
    'author': 'AccountTechs',
    'website': 'https://wa.me/966553493285',
    'depends': ['base', 'point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'custom_pos_receipt_ksa/static/src/**/*',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'sequence': 1,
    # 'price': 30,
    # 'currency': 'USD',
    'installable': True,
    'application': False,
    'auto_install': False,
}
