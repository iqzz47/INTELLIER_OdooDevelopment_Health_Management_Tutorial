# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalOdooInheritance(http.Controller):
#     @http.route('/hospital_odoo_inheritance/hospital_odoo_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_odoo_inheritance/hospital_odoo_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_odoo_inheritance.listing', {
#             'root': '/hospital_odoo_inheritance/hospital_odoo_inheritance',
#             'objects': http.request.env['hospital_odoo_inheritance.hospital_odoo_inheritance'].search([]),
#         })

#     @http.route('/hospital_odoo_inheritance/hospital_odoo_inheritance/objects/<model("hospital_odoo_inheritance.hospital_odoo_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_odoo_inheritance.object', {
#             'object': obj
#         })
