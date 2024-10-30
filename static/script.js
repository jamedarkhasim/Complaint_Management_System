document.addEventListener("DOMContentLoaded", loadComplaints);

function loadComplaints() {
    fetch('/api/complaints')
        .then(response => response.json())
        .then(complaints => {
            const complaintList = document.getElementById("complaintList");
            complaintList.innerHTML = '';
            complaints.forEach(complaint => {
                const complaintDiv = document.createElement('div');
                complaintDiv.className = 'complaint-item';
                complaintDiv.innerHTML = `
                    <strong>ID:</strong> ${complaint.ID} <br>
                    <strong>Name:</strong> ${complaint.FirstName} ${complaint.LastName} <br>
                    <strong>Address:</strong> ${complaint.Address} <br>
                    <strong>Gender:</strong> ${complaint.Gender} <br>
                    <strong>Comment:</strong> ${complaint.Comment} <br>
                    <button onclick="deleteComplaint(${complaint.ID})">Delete</button>
                `;
                complaintList.appendChild(complaintDiv);
            });
        });
}

function submitComplaint() {
    const data = {
        first_name: document.getElementById("firstName").value,
        last_name: document.getElementById("lastName").value,
        address: document.getElementById("address").value,
        gender: document.getElementById("gender").value,
        comment: document.getElementById("comment").value
    };

    fetch('/api/complaints', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(message => {
        alert(message.message);
        loadComplaints();  
        clearForm();
    });
}

function deleteComplaint(id) {
    fetch(`/api/complaints/${id}`, { method: 'DELETE' })
        .then(response => response.json())
        .then(message => {
            alert(message.message);
            loadComplaints();  
        });
}

function clearForm() {
    document.getElementById("firstName").value = "";
    document.getElementById("lastName").value = "";
    document.getElementById("address").value = "";
    document.getElementById("gender").value = "Male";
    document.getElementById("comment").value = "";
}
