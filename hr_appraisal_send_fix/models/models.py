# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrAppraisal(models.Model):
    _inherit = "hr.appraisal"

    def _send_mail(self, recipient, company_id, header_text, subject, body):
        """ 
            Overridden from hr_appraisal, added .send() and nothing more
        """

        msg = self.env['mail.message'].sudo().new(dict(body=body))

        notif_layout = self.env.ref('mail.mail_notification_light')
        notif_values = {'model_description': header_text, 'company': company_id}
        body_html = notif_layout.render(dict(message=msg, **notif_values), engine='ir.qweb', minimal_qcontext=True)
        body_html = self.env['mail.thread']._replace_local_links(body_html)
        email = self.env.user.work_email or self.env.user.email

        if not email:
            raise ValidationError(_("You must configure your mail address."))

        mail_values = {
            'email_from': formataddr((self.env.user.name, email)),
            'email_to': formataddr((recipient.name, recipient.work_email)),
            'subject': subject
            }
        self.env['mail.mail'].create(dict(body_html=body_html, state='outgoing', **mail_values)).send()