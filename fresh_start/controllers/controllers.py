# -*- coding: utf-8 -*-
# from odoo import http


# class NorahSupermarket(http.Controller):
#     @http.route('/fresh_start/fresh_start', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fresh_start/fresh_start/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fresh_start.listing', {
#             'root': '/fresh_start/fresh_start',
#             'objects': http.request.env['fresh_start.fresh_start'].search([]),
#         })

#     @http.route('/fresh_start/fresh_start/objects/<model("fresh_start.fresh_start"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fresh_start.object', {
#             'object': obj
#         })
