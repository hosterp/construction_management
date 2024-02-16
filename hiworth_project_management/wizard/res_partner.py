# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) BrowseInfo (http://browseinfo.in)
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
import datetime
from lxml import etree
import math
import pytz
import threading
import urlparse

from openerp.osv import osv
from openerp.osv import fields
from datetime import datetime, timedelta
from openerp.tools.translate import _
from openerp import SUPERUSER_ID
import openerp.addons.decimal_precision as dp
from openerp import http
from openerp.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT


class res_partner(osv.osv):
    _inherit = "res.partner"



    def _cron_birthday_reminder(self, cr, uid, context=None):

        su_id =self.pool.get('res.partner').browse(cr, uid, SUPERUSER_ID)
        partner_ids = self.search(cr, uid, (), context=None)
        for partner in self.browse(cr, uid, partner_ids, context=None):
            if partner.dob != False:
                bdate =datetime.strptime(partner.dob,'%Y-%m-%d').date()
                today =datetime.now().date()
                if bdate != today:
                    if bdate.month == today.month:
                        if bdate.day == today.day:
                            if partner:
                                template_id = self.pool.get('ir.model.data').get_object_reference(cr, uid,
                                                                      'hiworth_project_management',
                                                                      'email_template_edi_birthday_reminder')[1]
                                email_template_obj = self.pool.get('email.template')
                                if template_id:
                                    values = email_template_obj.generate_email(cr, uid,template_id, partner.id, context=context)
                                    values['email_from'] = su_id.email
                                    values['email_to'] = partner.email
                                    values['res_id'] = False
                                    mail_mail_obj = self.pool.get('mail.mail')
                                    msg_id = mail_mail_obj.create(cr, SUPERUSER_ID,values)
                                    if msg_id:
                                        mail_mail_obj.send(cr, SUPERUSER_ID,[msg_id])

        return True


    def _cron_anniversary_reminder(self, cr, uid, context=None):

        su_id =self.pool.get('res.partner').browse(cr, uid, SUPERUSER_ID)
        partner_ids = self.search(cr, uid, (), context=None)
        for partner in self.browse(cr, uid, partner_ids, context=None):
            if partner.wdng_day != False:
                anniversary =datetime.strptime(partner.wdng_day,'%Y-%m-%d').date()
                today =datetime.now().date()
                if anniversary != today:
                    if anniversary.month == today.month:
                        if anniversary.day == today.day:
                            if partner:
                                template_id = self.pool.get('ir.model.data').get_object_reference(cr, uid,
                                                                      'hiworth_project_management',
                                                                      'email_template_edi_anniversary_reminder')[1]
                                email_template_obj = self.pool.get('email.template')
                                if template_id:
                                    values = email_template_obj.generate_email(cr, uid,template_id, partner.id, context=context)
                                    values['email_from'] = su_id.email
                                    values['email_to'] = partner.email
                                    values['res_id'] = False
                                    mail_mail_obj = self.pool.get('mail.mail')
                                    msg_id = mail_mail_obj.create(cr, SUPERUSER_ID,values)
                                    if msg_id:
                                        mail_mail_obj.send(cr, SUPERUSER_ID,[msg_id])

        return True


    


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
