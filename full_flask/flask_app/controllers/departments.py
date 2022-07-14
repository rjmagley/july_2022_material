from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.employee import Employee
from flask_app.models.department import Department

@app.route('/departments')
def all_departments():

    departments = Department.get_all_departments()

    return render_template("departments.html", departments = departments)

@app.route('/departments/<int:department_id>')
def single_department(department_id):

    data = {
        'id': department_id
    }

    department = Department.get_department_by_id(data)

    employees_not_in_department = Employee.get_employees_not_in_department(data)

    return render_template("single_department.html", department = department, employees_not_in_department = employees_not_in_department)

@app.route('/departments/<int:department_id>/transfer_employee', methods=['POST'])
def transfer_employee(department_id):

    data = {
        'department_id': department_id,
        'employee_id': request.form['employee_id']
    }

    Employee.transfer_employee(data)

    return redirect(f'/departments/{department_id}')