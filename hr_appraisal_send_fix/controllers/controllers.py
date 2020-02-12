# -*- coding: utf-8 -*-
from odoo import http

# class HrAppraisalSendFix(http.Controller):
#     @http.route('/hr_appraisal_send_fix/hr_appraisal_send_fix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_appraisal_send_fix/hr_appraisal_send_fix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_appraisal_send_fix.listing', {
#             'root': '/hr_appraisal_send_fix/hr_appraisal_send_fix',
#             'objects': http.request.env['hr_appraisal_send_fix.hr_appraisal_send_fix'].search([]),
#         })

#     @http.route('/hr_appraisal_send_fix/hr_appraisal_send_fix/objects/<model("hr_appraisal_send_fix.hr_appraisal_send_fix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_appraisal_send_fix.object', {
#             'object': obj
#         })