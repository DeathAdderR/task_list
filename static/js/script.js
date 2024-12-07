
async function markTaskComplete(event) {
    event.preventDefault()
    // console.log(event)
    const taskId = event.target.task_id.value;

    if (!taskId) {
        alert("Prove a valid task ID")
        return;
    }

    const response = await fetch('/mark_task_complete', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({task_id: taskId})// pass task_id in the body
    })

    const result = await response.json();
    alert(result.message);
    await getTasks();
}

async function addTask(event) {
    event.preventDefault(); // prevent submission from reloading the page

    const formData = new FormData(event.target);
    const taskData = Object.fromEntries(formData.entries()); // convert form data to object

    try {
        const response = await fetch('/add_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
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
        const response = await fetch('/get_tasks');
        const tasks = await response.json();

        const taskList = document.getElementById('task-list');
        taskList.innerHTML = "";

        if (tasks.length === 0) {
            console.log("task list is empty")
            return
        }

        tasks.forEach( task => {
            const taskDiv = document.createElement('div')
            taskDiv.setAttribute('height', '200px')
            taskDiv.setAttribute('width', '200px')
            taskDiv.setAttribute('border', '1px solid black')
            taskDiv.textContent += "\nTask ID: " + task[0]
            taskDiv.textContent += "\nTask Name: " + task[1]
            taskDiv.textContent += "\nDue Date: " + task[2]
            if (task[3] == 1) {
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
    const markCompleteForm = document.getElementById("mark-complete")
    taskForm.addEventListener('submit', addTask)
    markCompleteForm.addEventListener('submit', markTaskComplete)
    getTasks()
})
