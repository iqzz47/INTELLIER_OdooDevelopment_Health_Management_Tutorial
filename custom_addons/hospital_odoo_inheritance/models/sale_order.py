from odoo import api, fields, models

class PatientTag(models.Model):
    _inherit = "sale.order.line"


    confirmed_user_id= fields.Many2one('res.users',string="Confirmed user")

    def test_function(self):
        return