from odoo import api, fields, models



class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"

    patient_id=fields.Many2one('hospital.patient',string="Patient")
    appointment_time=fields.Datetime(string="Appointment Time",default=fields.Datetime.now)
    booking_date=fields.Date(string="Booking Date", default=fields.Date.context_today)
    gender = fields.Selection(related='patient_id.gender')
    ref=fields.Char(string='Reference')
    prescription=fields.Html(string="Prescription")
    priority=fields.Selection([('0','Normal'),('1','Low'),('2','High'),('3','Very High')],string="priority")
    state=fields.Selection([('draft','Draft'),('in_consultation','In_consultation'),('done','Done'),('cancel','Canceled_task')] ,string="Status",default="draft",required="True")
    doctor_id=fields.Many2one('res.users',string="Doctor")
    pharmacy_lines_ids=fields.One2many('appointment.pharmacy.lines','appointment_id',string='Pharmacy Lines')
    hide_sales_price=fields.Boolean(string="Hide Sales Price")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
          print(self.patient_id)
          self.ref=self.patient_id.ref


    def action_test(self):
        print("Button Clicked!!!")
        return {
            'effect':{
                'fadeout':'slow',
                 'message':'Click Succesful',
                 'type':'rainbow_man'
            }
        }


    def action_in_consultation(self):
        for rec in self:
            rec.state='in_consultation'


    def action_in_markasdone(self):
        for rec in self:
            rec.state='done'

    def action_in_delete(self):
        #for rec in self:
        #rec.state='cancel'
        action=self.env.ref('hospital_management.action_cancel_appointment').read()[0]
        return action

    def action_restore(self):
        for rec in self:
            rec.state='draft'