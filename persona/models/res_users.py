from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    caracteristicas_ids = fields.One2many('caracteristicas', 'user_id', string='Caracteristicas')


