from odoo import models, fields, api
from odoo.exceptions import UserError


class InheritedEstateProperty(models.Model):
    _inherit = "estate.property"


    def sold_button(self):
        for record in self:
            if record.buyer_id:
                invoice_vals = {
                    'partner_id':record.buyer_id.id,
                    'move_type':'out_invoice',
                    'invoice_line_ids':[
                        (0,0.,{
                            'name':'Commission',
                            'quantity':1,
                            'price_unit':record.selling_price * 0.06,
                        }),
                        (0,0,{
                            'name':'Administrative fees',
                            'quantity':1,
                            'price_unit':100.0,
                        })
                    ]
                }
                self.env['account.move'].create(invoice_vals)



        return super().sold_button()

