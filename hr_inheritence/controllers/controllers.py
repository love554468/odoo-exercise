# -*- coding: utf-8 -*-
# from odoo import http


# class HrInheritence(http.Controller):
#     @http.route('/hr_inheritence/hr_inheritence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_inheritence/hr_inheritence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_inheritence.listing', {
#             'root': '/hr_inheritence/hr_inheritence',
#             'objects': http.request.env['hr_inheritence.hr_inheritence'].search([]),
#         })

#     @http.route('/hr_inheritence/hr_inheritence/objects/<model("hr_inheritence.hr_inheritence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_inheritence.object', {
#             'object': obj
#         })
