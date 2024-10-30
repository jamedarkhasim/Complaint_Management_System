from flask import Flask, request, jsonify, render_template
from configdb import ConnectionDatabase

app = Flask(__name__)
db = ConnectionDatabase()

@app.route('/')
def home():
    return render_template('index.html')  # Serves the frontend HTML

# API to view all complaints
@app.route('/api/complaints', methods=['GET'])
def get_complaints():
    complaints = db.List()  # Fetches all complaints from database
    return jsonify([dict(row) for row in complaints])

# API to add a new complaint
@app.route('/api/complaints', methods=['POST'])
def add_complaint():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    address = data.get('address')
    gender = data.get('gender')
    comment = data.get('comment')
    db.AddText(first_name, last_name, address, gender, comment)  # Insert complaint
    return jsonify({"message": "Complaint added successfully"}), 201

# API to delete a complaint by ID
@app.route('/api/complaints/<int:complaint_id>', methods=['DELETE'])
def delete_complaint(complaint_id):
    db.DeleteComplaint(complaint_id)  # Delete by ID
    return jsonify({"message": f"Complaint with ID {complaint_id} deleted."})

if __name__ == "__main__":
    app.run(debug=True)
