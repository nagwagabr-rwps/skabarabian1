# -*- coding: utf-8 -*-
# from odoo import http


# class SkabCustmodule(http.Controller):
#     @http.route('/skab_custmodule/skab_custmodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/skab_custmodule/skab_custmodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('skab_custmodule.listing', {
#             'root': '/skab_custmodule/skab_custmodule',
#             'objects': http.request.env['skab_custmodule.skab_custmodule'].search([]),
#         })

#     @http.route('/skab_custmodule/skab_custmodule/objects/<model("skab_custmodule.skab_custmodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('skab_custmodule.object', {
#             'object': obj
#         })

