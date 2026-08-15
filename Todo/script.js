// Select DOM elements
const taskInput = document.getElementById('task-input');
const addTaskBtn = document.getElementById('add-task-btn');
const taskList = document.getElementById('task-list');
const totalTasksEl = document.getElementById('total-tasks');
const activeTasksEl = document.getElementById('active-tasks');
const completedTasksEl = document.getElementById('completed-tasks');
const clearCompletedBtn = document.getElementById('clear-completed');
const emptyStateEl = document.getElementById('empty-state');

let tasks = [];

// Load tasks from localStorage
document.addEventListener('DOMContentLoaded', loadTasks);

// Add task
addTaskBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});

// Clear completed tasks
clearCompletedBtn.addEventListener('click', clearCompleted);

function loadTasks() {
    tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    renderTasks();
    updateStatistics();
}

function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText === '') return;
    const newTask = { text: taskText, completed: false };
    tasks.push(newTask);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    renderTasks();
    taskInput.value = '';
}

function renderTasks() {
    taskList.innerHTML = '';
    tasks.forEach((task, index) => {
        const taskEl = document.createElement('div');
        taskEl.className = 'task';
        taskEl.innerHTML = `
            <input type='checkbox' ${task.completed ? 'checked' : ''} onchange='toggleTask(${index})'>
            <span class='task-text ${task.completed ? "completed" : ""}'>${task.text}</span>
            <button class='edit' onclick='editTask(${index})'>Edit</button>
            <button class='delete' onclick='deleteTask(${index})'>Delete</button>
        `;
        taskList.appendChild(taskEl);
    });
    emptyStateEl.style.display = tasks.length === 0 ? 'block' : 'none';
}

function toggleTask(index) {
    tasks[index].completed = !tasks[index].completed;
    localStorage.setItem('tasks', JSON.stringify(tasks));
    renderTasks();
    updateStatistics();
}

function deleteTask(index) {
    tasks.splice(index, 1);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    renderTasks();
    updateStatistics();
}

function editTask(index) {
    const newText = prompt('Edit task:', tasks[index].text);
    if (newText) {
        tasks[index].text = newText;
        localStorage.setItem('tasks', JSON.stringify(tasks));
        renderTasks();
    }
}

function clearCompleted() {
    tasks = tasks.filter(task => !task.completed);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    renderTasks();
    updateStatistics();
}

function updateStatistics() {
    totalTasksEl.textContent = tasks.length;
    activeTasksEl.textContent = tasks.filter(task => !task.completed).length;
    completedTasksEl.textContent = tasks.filter(task => task.completed).length;
}