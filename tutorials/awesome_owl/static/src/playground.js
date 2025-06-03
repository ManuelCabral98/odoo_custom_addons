/** @odoo-module **/

import { Component, markup, useState } from "@odoo/owl";
import { Counter } from "./counter/counter";
import { DashboardItem } from "./dashboardItem/card"
import { TodoList } from "./todo_list/todo_list";


export class Playground extends Component {
    static template = "awesome_owl.Playground"
    static components = { Counter, Card: DashboardItem, TodoList }

    setup(){
        // this.str1 = "<div class='text-primary'>Text</div>"
        // this.str2 = markup("<div class='text-primary'>Some other text</div>")
        this.sum = useState({value: 2});
    }

    incrementSum(){
        this.sum.value++;
    }
}
