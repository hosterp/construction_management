# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
	'name': 'BOQ',
	'version': '0.2',
	'author': 'OpenERP SA',
	'website': 'https://www.odoo.com',
	'category': 'Tools',
	'installable': True,
	'auto_install': False,
	'data': [
	
			#security			 
			 'security/ir.model.access.csv',

			#views
			 'views/boq_view.xml',
			 'views/re_view.xml',
			 'views/cs_view.xml', 
			 'views/property_details_view.xml', 
			 'views/ir_sequence.xml',


			#report
			 'report/report.xml',
			 'report/comparative_statement_report_template.xml',
			 'report/revised_estimate_report_template.xml',
			 'report/first_bill_report_template.xml',

			#wizard
			'wizard/first_bill_excel_report.xml', 
			'wizard/revised_estimate_excel_report.xml', 
			'wizard/comparative_statement_excel.xml', 


	],
	'demo': [ 
	],
	'depends': ['base','hiworth_construction','account','report_xlsx', 'web_kanban_gauge', 'web_kanban_sparkline'],
	'description': """

"""
}
