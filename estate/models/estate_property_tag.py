from odoo import models, fields

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"
    _order = 'name'

    name = fields.Char("Name")
    color = fields.Integer("Color")

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)','Name must be unique')
    ]