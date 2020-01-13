# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddDateCrm(models.Model):
	_inherit = "crm.lead"

	date_now = fields.Datetime(string="Fecha de lead")
	partner_address_mobile = fields.Char('Partner Contact Mobile', related='partner_id.mobile', readonly=True)
	