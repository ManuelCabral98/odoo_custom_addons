# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api
from odoo.exceptions import UserError

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'
    _order = 'id desc'

    name = fields.Char('Property Name', required=True)
    description = fields.Text('Property Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date(
        'Date Availability',
        default=fields.Date.add(fields.Date.today(), months=3),
        copy=False
    )
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    best_offer = fields.Float('Best Offer', compute="_compute_best_price" ,readonly=True, copy=False, store=True)
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades_area = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area (sqm)')
    active = fields.Boolean('Active', default=True)
    garden_orientation = fields.Selection([
            ('north','North'),
            ('south','South'),
            ('east','East'),
            ('west','West'),
            ],
            string='Garden Orientation',
            default = '',
    )
    status = fields.Selection([
        ('new','New'),
        ('offer received','Offer Received'),
        ('offer accepted','Offer Accepted'),
        ('sold','Sold'),
        ('cancelled','Cancelled'),
        ],
        string='Status',
        default='new',
        required=True,
        copy=False
    )
    property_types_id = fields.Many2one("estate.property.types", string="Property Type")
    buyer_id = fields.Many2one("res.users", string="Client", copy=False)
    salesman_id = fields.Many2one("res.users", string="Salesman")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area = fields.Integer(compute="_compute_total_area", string="Total Area (sqm)", store=True)



    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price>=0)','Expected Price must be greater than 0'),
        ('check_selling_price', 'CHECK(selling_price>=0)','Selling Price must be positive')
    ]

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_offer = max(record.offer_ids.mapped('price'))
            else:
                record.best_offer = 0.0

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = ''

    def sold_button(self):
        for record in self:
            if record.status != 'cancelled':
                record.status = 'sold'
            else:
                raise UserError("The property has already been cancelled!")

    def cancel_button(self):
        for record in self:
            if record.status != 'sold':
                record.status = 'cancelled'
            else:
                raise UserError("The property has already been sold!")

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < record.expected_price * 0.9 and record.offer_ids.status != 'refused':
                raise UserError("The selling price must be at least 90% of the expected price")

    @api.ondelete(at_uninstall=False)
    def _delete(self):
        for record in self:
            if record.status not in ('new', 'cancelled'):
                raise UserError("Only new or cancelled offers are allowed to delete!!!")



