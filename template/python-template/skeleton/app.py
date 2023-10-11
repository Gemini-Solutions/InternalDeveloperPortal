from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate an employee database
employees = [
    {"id": 1, "name": "John Doe", "position": "Software Developer"},
    {"id": 2, "name": "Jane Smith", "position": "Designer"},
]

# Create - Add a new employee
@app.route('/employees', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    new_employee["id"] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

# Read - Get all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({'employees': employees})

# Read - Get a specific employee by ID
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify({'employee': employee})

# Update - Update an existing employee
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    updated_employee = request.get_json()
    employee.update(updated_employee)
    return jsonify({'employee': employee})

# Delete - Delete an employee by ID
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = next((employee for employee in employees if employee['id'] == employee_id), None)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    employees.remove(employee)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
