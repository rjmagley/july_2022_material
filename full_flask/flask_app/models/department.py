from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.employee import Employee

class Department():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.employees = []

    @classmethod
    def get_all_departments(cls):

        query = "SELECT * FROM departments LEFT JOIN employees ON departments.id = employees.department_id;"

        results = connectToMySQL('july_2022_employees').query_db(query)

        departments = []

        departments.append(Department(results[0]))

        for row in results:
            # check to see if this department exists or not
            if row['id'] != departments[-1].id:
                # if department is not in list, create a new one
                departments.append(Department(row))
            if row['employees.id'] != None:
                employee_data = {
                    'id': row['employees.id'],
                    'first_name': row['first_name'],
                    'middle_name': row['middle_name'],
                    'last_name': row['last_name'],
                    'salary': row['salary'],
                    'created_at': row['employees.created_at'],
                    'updated_at': row['employees.updated_at'],
                    'department_id': row['department_id']
                }
                new_employee = Employee(employee_data)
                departments[-1].employees.append(new_employee)
            

        return departments

    @classmethod
    def get_department_by_id(cls, data):

        query = "SELECT * FROM departments LEFT JOIN employees ON departments.id = employees.department_id WHERE departments.id = %(id)s;"

        results = connectToMySQL('july_2022_employees').query_db(query, data)

        department = Department(results[0])

        for row in results:
            if row['employees.id'] != None:
                employee_data = {
                    'id': row['employees.id'],
                    'first_name': row['first_name'],
                    'middle_name': row['middle_name'],
                    'last_name': row['last_name'],
                    'salary': row['salary'],
                    'created_at': row['employees.created_at'],
                    'updated_at': row['employees.updated_at'],
                    'department_id': row['department_id']
                }
                new_employee = Employee(employee_data)
                department.employees.append(new_employee)

        return department