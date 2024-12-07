
async function markTaskComplete(taskId) {
    const response = await fetch('/mark_task_complete', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({task_id: taskId})
    });
    const result = await response.json();
}

async function addTask(event) {
    event.preventDefault(); // prevent submission from reloading the page

    const formData = new formData(event.target);
    const taskData = Object.fromEntries(formData.entries()); // convert form data to object

    try {
        const response = await fetch('./add_task', {
            method: 'POST',
            headers: {
                'Content-Type:': 'application/json',
            },
            body: JSON.stringify(taskData)
        });

        const result = await response.json();
        alert(result.message) // show success message
        getTasks(); // refresh task list
    }
    catch(error) {
        console.error('Error adding task: ', error);
    }
}

async function getTasks() {
    try {
        const response = await fetch('./get_tasks');
        const tasks = await response.json();

        const taskList = document.getElementById('task-list');
        taskList.innerHTML = "";

        taskList.forEach( task => {
            const taskDiv = document.createElement('div')
            taskDiv.setAttribute('height', '200px')
            taskDiv.setAttribute('width', '200px')
            taskDiv.setAttribute('border', '1px solid black')
            taskDiv.textContent += "\nTask ID: " + task.task_id
            taskDiv.textContent += "\nTask Name: " + task.task_name
            taskDiv.textContent += "\nDue Date: " + task.due_date
            if (task.complete == true) {
                taskDiv.textContent += "\nIs Complete: " + "Task Complete"
            }
            else {
                taskDiv.textContent += "\nIs Complete: " + "Task Not Completed"
            }
            taskList.appendChild(taskDiv)
        })

    }
    catch (error) {
        console.error("Error fetching tasks: ", error)
    }
}

document.addEventListener("DOMContentLoaded", () => {
    
    const taskForm = document.getElementById('task-form')
    taskForm.addEventListener('submit', addTask)
    getTasks()
})
