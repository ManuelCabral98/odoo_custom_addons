/** @odoo-module **/

import { Component} from "@odoo/owl";

export class DashboardItem extends Component{
    static template = "awesome_dashboard.DashboardItem";
    static props = {
        slots: {type: Object, shape: {default: Object}},
        size: { type: Number, optional: true, default: 1}
    };
}
