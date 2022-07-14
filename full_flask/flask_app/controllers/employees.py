from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.employee import Employee
from flask_app.models.department import Department

@app.route('/')
def index():

    employees = Employee.get_all_employees()
    departments = Department.get_all_departments()

    return render_template('employees.html', employees = employees, departments = departments)

@app.route('/employees/create', methods=['POST'])
def create_employee():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'salary': request.form['salary'],
        'department_id': request.form['department_id']
    }

    if request.form['middle_name'] == '':
        data['middle_name'] = None
    else:
        data['middle_name'] = request.form['middle_name']

    Employee.create_employee(data)

    return redirect('/')

@app.route('/employees/<int:employee_id>/delete')
def delete_employee(employee_id):

    data = {
        'id': employee_id
    }

    Employee.delete_employee(data)

    return redirect('/')

@app.route('/employees/<int:employee_id>/edit')
def edit_employee(employee_id):

    data = {
        'id': employee_id
    }

    employee = Employee.get_employee_by_id(data)
    departments = Department.get_all_departments()

    return render_template('edit_employee.html', departments = departments, employee = employee)

@app.route('/employees/<int:employee_id>/update', methods=['POST'])
def update_employee(employee_id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'salary': request.form['salary'],
        'department_id': request.form['department_id'],
        'id': employee_id
    }

    if request.form['middle_name'] == '':
        data['middle_name'] = None
    else:
        data['middle_name'] = request.form['middle_name']

    Employee.update_employee(data)

    return redirect('/')