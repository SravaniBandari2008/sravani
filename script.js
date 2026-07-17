document.querySelectorAll('.navbar a').forEach(link =>{
  link.addEventListener('click',function (e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    document.querySelector(targetId).scrollIntoView({ behavior: 'smooth'});
  });
}); 

// ---------- 2. Student Profile ----------
const createProfileBtn = document.getElementById('createProfileBtn');
const profileDisplay = document.getElementById('profileDisplay');

function createProfile() {
    // read values out of the form
    const name = document.getElementById('studentName').value;
    const roll = document.getElementById('rollNumber').value;
    const branch = document.getElementById('branch').value;
    const year = document.getElementById('year').value;
    const goal = document.getElementById('careerGoal').value;

    // basic validation before we touch the DOM
    if (!name || !roll) {
        alert('Please enter at least your name and roll number');
        return;
    }

    // build and inject a summary card, reusing the .task-card style
    profileDisplay.innerHTML = `
        <div class="task-card">
            <div>
                <h4>${name} (${roll})</h4>
                <p>${branch} - Year ${year}</p>
                <p>Goal: ${goal}</p>
            </div>
        </div>
    `;

    document.getElementById('profileForm').reset();
}

createProfileBtn.addEventListener('click', createProfile);


// ---------- 3. Task Manager ----------
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');

function addTask() {
    const title = document.getElementById('taskTitle').value;
    const date = document.getElementById('taskDueDate').value;

    if (!title || !date) {
        alert('Please enter task title and due date');
        return;
    }

    // createElement + innerHTML: build the card in memory, then attach it
    const taskCard = document.createElement('div');
    taskCard.className = 'task-card';
    taskCard.innerHTML = `
        <div>
            <h4>${title}</h4>
            <p>Due Date: ${date}</p>
        </div>
        <span class="status-badge status-pending">Pending</span>
    `;

    // clicking the badge toggles Pending <-> Completed
    const badge = taskCard.querySelector('.status-badge');
    badge.addEventListener('click', () => toggleTaskStatus(badge));

    taskList.appendChild(taskCard);

    // clear the inputs for the next entry
    document.getElementById('taskTitle').value = '';
    document.getElementById('taskDueDate').value = '';
}

function toggleTaskStatus(badge) {
    if (badge.classList.contains('status-pending')) {
        badge.classList.remove('status-pending');
        badge.classList.add('status-completed');
        badge.textContent = 'Completed';
    } else {
        badge.classList.remove('status-completed');
        badge.classList.add('status-pending');
        badge.textContent = 'Pending';
    }
}

addTaskBtn.addEventListener('click', addTask);


// ---------- 4. Coding Practice Tracker ----------
const addProblemBtn = document.getElementById('addProblemBtn');
const problemTableBody = document.getElementById('problemTableBody');

function addProblem() {
    const title = document.getElementById('problemTitle').value;
    const platform = document.getElementById('platformInput').value;
    const difficulty = document.getElementById('difficultySelect').value;
    const status = document.getElementById('statusSelect').value;

    if (!title || !platform) {
        alert('Please enter problem title and platform');
        return;
    }

    // a table needs a <tr> full of <td>, not a <div>
    const row = document.createElement('tr');
    row.innerHTML = `
        <td>${title}</td>
        <td>${platform}</td>
        <td>${difficulty}</td>
        <td>${status}</td>
    `;

    problemTableBody.appendChild(row);

    document.getElementById('problemTitle').value = '';
    document.getElementById('platformInput').value = '';
}

addProblemBtn.addEventListener('click', addProblem);