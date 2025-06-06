/** @odoo-module **/

import { Component } from "@odoo/owl";

export class TodoItem extends Component{
    static template = "awesome_owl.TodoItem";
    static props = {
        todo: {
            type: Object,
            shape: {id: Number, description: String, isCompleted: Boolean}
        },
        toggleState: {
            type: Function
        },
        removeTodo: {
            type: Function
        }
    };

    onChange() {
        this.props.toggleState(this.props.todo.id);
    }

    onDelete(elemId){
        this.props.removeTodo(this.props.todo.id);
    }
}