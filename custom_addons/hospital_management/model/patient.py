from odoo import api, fields, models
from datetime import date



class Hospitalpatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"
    name = fields.Char(string='Name',tracking=True)
    date_of_birth = fields.Date(string="Date of Birth",help="Enter date of birth")
    age = fields.Integer(string='Age',compute='_compute_age',tracking=True,store=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender',tracking=True,help="Enter date of birth")
    active = fields.Boolean(string="Active",default=True)
    ref= fields.Char(string='Reference')
    appointment_id=fields.One2many('hospital.appointment','patient_id',string='appointment')
    tag_ids=fields.Many2many('patient.tag',string='Tags')
    image=fields.Image(string="Image")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age= today.year - rec.date_of_birth.year
            else:
                rec.age=0
