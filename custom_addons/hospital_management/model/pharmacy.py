from odoo import api, fields, models

class AppointmentPharamacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmcay Lines"

    product_id=fields.Many2one('product.product')
    qty=fields.Integer(string="Quality")
    price_unit=fields.Float(string='Price')
    appointment_id=fields.Many2one('hospital.appointment',string="Appointment")


