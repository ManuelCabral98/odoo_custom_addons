/** @odoo-module **/

import { Component, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { Layout } from  "@web/search/layout";
import { useService } from "@web/core/utils/hooks";
import {_t} from "@web/core/l10n/translation";
import { DashboardItem } from "./dashboard_item/dashboard_item";


export class AwesomeDashboard extends Component {
    static template = "awesome_dashboard.AwesomeDashboard";
    static components = { Layout, DashboardItem: DashboardItem };

    setup() {
        this.display = {
            controlPanel: {},
        };
        this.action = useService("action");
        this.rpc = useService("rpc");
        onWillStart(async () => {
            this.statistics = await this.rpc("/awesome_dashboard/statistics");
        })
    }
    // aqui se llama a una acción ya establecida en XML en el modulo base
    openKanbanCustomers(){
        this.action.doAction("base.action_partner_form");
    }

    // metodo para abrir crm.lead, de forma dinamica, si no existe una acción
    async openLeads() {
        await this.action.doAction({
            type: 'ir.actions.act_window',
            name: _t('Leads'),
            target: 'current',
            res_model: 'crm.lead',
            views: [
                [false, 'list'],
                [false, 'form'],
            ],
        });
    }

}

registry.category("actions").add("awesome_dashboard.dashboard", AwesomeDashboard);
