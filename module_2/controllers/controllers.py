# -*- coding: utf-8 -*-
from odoo import http

# class Module2(http.Controller):
#     @http.route('/module_2/module_2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_2/module_2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_2.listing', {
#             'root': '/module_2/module_2',
#             'objects': http.request.env['module_2.module_2'].search([]),
#         })

#     @http.route('/module_2/module_2/objects/<model("module_2.module_2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_2.object', {
#             'object': obj
#         })