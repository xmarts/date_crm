# -*- coding: utf-8 -*-
from odoo import http

# class AddDateCrm(http.Controller):
#     @http.route('/add_date_crm/add_date_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_date_crm/add_date_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_date_crm.listing', {
#             'root': '/add_date_crm/add_date_crm',
#             'objects': http.request.env['add_date_crm.add_date_crm'].search([]),
#         })

#     @http.route('/add_date_crm/add_date_crm/objects/<model("add_date_crm.add_date_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_date_crm.object', {
#             'object': obj
#         })