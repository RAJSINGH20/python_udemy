// Select elements
const taskInput = document.getElementById('task');
const addTaskBtn = document.getElementById('add-task');
const taskList = document.getElementById('task-list');
const totalTasks = document.getElementById('total-tasks');
const activeTasks = document.getElementById('active-tasks');
const completedTasks = document.getElementById('completed-tasks');
const clearCompletedBtn = document.getElementById('clear-completed');
const filters = document.querySelectorAll('.filter');
const emptyState = document.querySelector('.empty-state');

let tasks = [];

// Load tasks from localStorage on page load
window.onload = function() {
    loadTasks();
};

// Add task
addTaskBtn.addEventListener('click', addTask);
taskInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});

// Clear Completed button
clearCompletedBtn.addEventListener('click', clearCompletedTasks);

// Add filters
filters.forEach(filter => {
    filter.addEventListener('click', filterTasks);
});

function addTask() {
    const taskText = taskInput.value.trim();
    if (!taskText) return;

    const task = {
        id: Date.now(),
        text: taskText,
        completed: false
    };
    tasks.push(task);
    taskInput.value = '';
    saveTasks();
    renderTasks();
}

function renderTasks() {
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const taskDiv = document.createElement('div');
        taskDiv.className = 'task' + (task.completed ? ' completed' : '');
        taskDiv.setAttribute('data-id', task.id);

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = task.completed;
        checkbox.addEventListener('change', () => toggleComplete(task.id));

        const taskText = document.createElement('span');
        taskText.textContent = task.text;

        const editBtn = document.createElement('button');
        editBtn.textContent = 'Edit';
        editBtn.addEventListener('click', () => editTask(task.id));

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.addEventListener('click', () => deleteTask(task.id));

        taskDiv.appendChild(checkbox);
        taskDiv.appendChild(taskText);
        taskDiv.appendChild(editBtn);
        taskDiv.appendChild(deleteBtn);
        taskList.appendChild(taskDiv);
    });
    updateStatistics();
    emptyState.style.display = tasks.length === 0 ? 'block' : 'none';
}

function toggleComplete(id) {
    const task = tasks.find(task => task.id === id);
    task.completed = !task.completed;
    saveTasks();
    renderTasks();
}

function deleteTask(id) {
    tasks = tasks.filter(task => task.id !== id);
    saveTasks();
    renderTasks();
}

function editTask(id) {
    const task = tasks.find(task => task.id === id);
    const newText = prompt('Edit task:', task.text);
    if (newText) {
        task.text = newText;
        saveTasks();
        renderTasks();
    }
}

function clearCompletedTasks() {
    tasks = tasks.filter(task => !task.completed);
    saveTasks();
    renderTasks();
}

function filterTasks(e) {
    const filter = e.currentTarget.dataset.filter;
    if (filter === 'all') {
        renderTasks();
    } else {
        const filteredTasks = tasks.filter(task => (filter === 'active' ? !task.completed : task.completed));
        taskList.innerHTML = '';
        filteredTasks.forEach(task => {
            const taskDiv = document.createElement('div');
            taskDiv.className = 'task' + (task.completed ? ' completed' : '');
            taskDiv.setAttribute('data-id', task.id);
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.checked = task.completed;
            checkbox.addEventListener('change', () => toggleComplete(task.id));
            
            const taskText = document.createElement('span');
            taskText.textContent = task.text;
            
            const editBtn = document.createElement('button');
            editBtn.textContent = 'Edit';
            editBtn.addEventListener('click', () => editTask(task.id));
            
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = 'Delete';
            deleteBtn.addEventListener('click', () => deleteTask(task.id));
            
            taskDiv.appendChild(checkbox);
            taskDiv.appendChild(taskText);
            taskDiv.appendChild(editBtn);
            taskDiv.appendChild(deleteBtn);
            taskList.appendChild(taskDiv);
        });
        emptyState.style.display = filteredTasks.length === 0 ? 'block' : 'none';
    }
}

function updateStatistics() {
    totalTasks.textContent = tasks.length;
    activeTasks.textContent = tasks.filter(task => !task.completed).length;
    completedTasks.textContent = tasks.filter(task => task.completed).length;
}

function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function loadTasks() {
    const savedTasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks = savedTasks;
    renderTasks();
}