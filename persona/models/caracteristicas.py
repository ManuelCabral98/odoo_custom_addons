from odoo import models, fields, api
from odoo.exceptions import UserError

class Caracteristicas(models.Model):
    _name = 'caracteristicas'
    _description = 'Modelo para las caracteristicas'

    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.context.get('active_id'))
    birthdate = fields.Date('Birthdate', required=True)
    age = fields.Integer('Age', compute='_compute_age')
    height = fields.Float('Height', required=True)
    weight = fields.Float('Weight', required=True)
    bmi = fields.Float('BMI', readonly=False, store=True)

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                born = record.birthdate
                today = fields.Date.today()
                record.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            else:
                record.age = 0

    @api.onchange('height', 'weight')
    def _onchange_bmi(self):
        for record in self:
            if record.height > 0.0 and record.weight > 0.0:
                record.bmi = round(record.weight / (record.height ** 2), 2)
            else:
                record.bmi = 0.0