# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloSge(http.Controller):
#     @http.route('/modulo_sge/modulo_sge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_sge/modulo_sge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_sge.listing', {
#             'root': '/modulo_sge/modulo_sge',
#             'objects': http.request.env['modulo_sge.modulo_sge'].search([]),
#         })

#     @http.route('/modulo_sge/modulo_sge/objects/<model("modulo_sge.modulo_sge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_sge.object', {
#             'object': obj
#         })
