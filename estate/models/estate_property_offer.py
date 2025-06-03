from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import UserError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"
    _order = 'price desc'
    price = fields.Float(string="Price")
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused")
        ],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer("Validity (Days)", default=7, store=True)
    date_deadline = fields.Date("Deadline",
                                compute="_compute_date_deadline",
                                inverse="_inverse_validity",
                                default=fields.Date.add(fields.Date.today(),days = 7),
                                store=True
                                )

    property_types_id = fields.Many2one(related="property_id.property_types_id", store=True, string="Property Type")

    _sql_constraints = [
        ("check_price",'CHECK(price>=0)','Price must be positive')
    ]

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date.date() + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

    def _inverse_validity(self):
        for record in self:
            if record.create_date and record.validity:
                aux = record.date_deadline - record.create_date.date()
                record.validity = aux.days

    def _verification_status(self):
        for record in self:
            accepted = self.search([('status','=','accepted'), ('property_id', '=', record.property_id.id)])
            if accepted:
                return True
        return False


    def accept_offer_button(self):
        verification = self._verification_status()
        for record in self:
            if verification:
                raise UserError("You cannot accept more than one offer")
            else:
                if record.property_id.status == "cancelled":
                    record.status = 'refused'
                    raise UserError("Cannot accept offer because property is cancelled")
                else:
                    record.status = 'accepted'

                    record.property_id.selling_price = record.price
                    record.property_id.buyer_id = self.env.user

    def refuse_offer_button(self):
        for record in self:
            record.status = 'refused'
            record.property_id.selling_price = 0.0
            record.property_id.buyer_id = False

    @api.model
    def create(self, vals):
        offers = super().create(vals)
        for offer in offers:
            if offer.price < offer.property_id.best_offer:
                raise UserError("Price must be greater than offer price")
            else:
                if offer.property_id.status == 'new':
                    offer.property_id.status = 'offer received'
                return offers















