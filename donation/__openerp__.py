# -*- encoding: utf-8 -*-
##############################################################################
#
#    Donation module for Odoo
#    Copyright (C) 2014-2015 Barroux Abbey (www.barroux.org)
#    Copyright (C) 2014-2015 Akretion France (www.akretion.com)
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


{
    'name': 'Donation',
    'version': '8.0.0.1.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Manage donations',
    'author': 'Barroux Abbey, Akretion, Odoo Community Association (OCA)',
    'website': 'http://www.barroux.org',
    'depends': ['account_accountant'],
    'data': [
        'security/donation_security.xml',
        'donation_view.xml',
        'account_view.xml',
        'product_view.xml',
        'donation_campaign_view.xml',
        'users_view.xml',
        'security/ir.model.access.csv',
        'partner_view.xml',
        'report/donation_report_view.xml',
        'wizard/donation_validate_view.xml',
        ],
    'demo': ['donation_demo.xml'],
    'test': ['test/validate.yml'],
}
