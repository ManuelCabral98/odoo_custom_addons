/** @odoo-module **/

import { Component,useState,onMounted,useRef } from "@odoo/owl";
import { TodoItem } from "./todo_item";



export class TodoList extends Component{
    static template = "awesome_owl.TodoList";
    static components = {TodoItem};

    inputRef = useRef("input");

    setup(){
        this.todos = useState([]);
        this.nextID = 1;
        onMounted(() => {
            this.inputRef.el.focus();
        })
    }

    addTodo(ev){
        if (ev.keyCode === 13 && ev.target.value !== "") {
            this.todos.push({
                id: this.nextID++,
                description: ev.target.value,
                isCompleted: false
            });
            ev.target.value = "";
        }
    }

    toggleTodo(todoId){
        const todo = this.todos.find((todo) => todo.id === todoId);
        if(todo){
            todo.isCompleted = !todo.isCompleted;
        }
    }

    removeTodo(todoId){
        const index = this.todos.findIndex((elem) => elem.id === todoId);
        if (index >= 0){
            this.todos.splice(index, 1);
        }
    }
}