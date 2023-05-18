const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");

let todos = [];

function submitAddTodo(event) {
  event.preventDefault();
  const content = document.getElementById("content");
  const newTodo = content.value;
  todos.push(newTodo);
  window.localStorage.setItem("todo", JSON.stringify(todos));
  content.value = "";
  paintTodo();
}

function paintTodo() {
  todoList.innerHTML = "";
  todos.forEach((todo, index) => {
    const listItem = document.createElement("li");
    listItem.textContent = todo;
    listItem.id = "todo-" + index;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", deleteTodo);
    listItem.appendChild(deleteButton);

    todoList.appendChild(listItem);
  });
}

function deleteTodo(event) {
  const deleteButton = event.target;
  const listItem = deleteButton.parentNode;
  const todoId = listItem.id.split("-")[1];
  todos.splice(todoId, 1);
  window.localStorage.setItem("todo", JSON.stringify(todos));
  listItem.remove();
}

todoForm.addEventListener("submit", submitAddTodo);

const storedTodos = JSON.parse(window.localStorage.getItem("todo"));
if (Array.isArray(storedTodos)) {
  todos = storedTodos;
  paintTodo();
}
