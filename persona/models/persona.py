from odoo import models, fields


class Persona(models.Model):
    _name='persona'
    _description = 'Modelo para la creacion de una Persona'

    name = fields.Char('Nombre', required=True)
    age = fields.Integer('Age', required=True)
    father = fields.Many2one('res.users', string='Father')
    note = fields.Char('Note', required=True)
    active = fields.Boolean('Active', default=True)
    address = fields.Text('Address')
    gender = fields.Selection([
        ('m', 'Masculino'),
        ('f', 'Femenino'),
    ])
    birthdate = fields.Date('Birthdate')