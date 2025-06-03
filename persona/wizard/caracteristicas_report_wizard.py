from odoo import fields, models

class CaracteristicasReportWizard(models.TransientModel):
    _name = 'caracteristicas.report.wizard'
    _description = 'Wizard for the creation of PDF reports'

    weight_start = fields.Float(string='Weight Start', default=0)
    weight_end = fields.Float(string='Weight End', default=0)

    def action_search_weights(self):
        form_data = self.read()[0]

        weights = self.env['caracteristicas'].search_read([
            ('weight','>=', form_data['weight_start']),
            ('weight','<=', form_data['weight_end']),
        ])

        data = {
            'form_data': form_data,
            'weights': weights,
        }

        return self.env.ref('persona.action_caracteristicas_wizard').report_action(self, data=data)


