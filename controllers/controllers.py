# -*- coding: utf-8 -*-
# from odoo import http


# class HosspitalModule(http.Controller):
#     @http.route('/hosspital_module/hosspital_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hosspital_module/hosspital_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hosspital_module.listing', {
#             'root': '/hosspital_module/hosspital_module',
#             'objects': http.request.env['hosspital_module.hosspital_module'].search([]),
#         })

#     @http.route('/hosspital_module/hosspital_module/objects/<model("hosspital_module.hosspital_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hosspital_module.object', {
#             'object': obj
#         })

