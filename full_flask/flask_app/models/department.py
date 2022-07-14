from flask_app.config.mysqlconnection import connectToMySQL

class Department():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_departments(cls):

        query = "SELECT * FROM departments;"

        results = connectToMySQL('july_2022_employees').query_db(query)

        departments = []

        for row in results:
            departments.append(Department(row))

        return departments

