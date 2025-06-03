from itertools import count

from odoo import models, fields, api


class EstatePropertyTypes(models.Model):
    _name = 'estate.property.types'
    _description = 'Property Types'
    _order = 'sequence, name'

    sequence = fields.Integer('Sequence')
    name = fields.Char('Property Type', required=True)
    property_ids = fields.One2many('estate.property','property_types_id', string='Property Types')
    offer_ids= fields.One2many('estate.property.offer', 'property_types_id', string='Offers')
    offer_count = fields.Integer(' Offer Count', compute='_compute_offer_count')

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)','Name must be unique')
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            offers = record.mapped('property_ids.offer_ids')
            record.offer_count = len(offers)









