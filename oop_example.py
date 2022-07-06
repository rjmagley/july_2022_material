class Department():

    def __init__(self, name, location):
        # one sec brb
        self.name = name
        self.location = location
        self.employees = []

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def get_department_summary(self):
        # returns string containing information about the department
        department_info = f"{self.name} - office: {self.location}\n"
        department_info += f"Total employees: {len(self.employees)}\n"
        department_info += f"Yearly salary for all employees: {self.get_yearly_salary()}\n"
        for employee in self.employees:
            department_info += f"{employee.full_name}\n"
        return department_info

    def get_yearly_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary

        return total_salary

    def departmental_salary_increase(self, percentage):
        # percentage is a float
        # i.e. 5% = .05
        for employee in self.employees:
            employee.set_salary(employee.salary * (1 + percentage))

class Employee():

    # methods
    # __init__ methods - acts as constructor
    def __init__(self, first_name, last_name, salary, department, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary
        self.department = department
        self.department.add_employee(self)

    # alternatively:
    # def __init__(self, fname, lname, sal):
    #     self.first_name = fname
    #     self.last_name = lname
    #     self.salary = sal

    def set_salary(self, new_salary):
        if type(new_salary) == float:
            new_salary = int(new_salary)
            # minimum salary is 40000, maximum is 200000
        elif type(new_salary) != int:
            return None
            
        if new_salary >= 40000 and new_salary <= 200000:
            self.salary = new_salary

    @property
    def full_name(self):
        if self.middle_name != None:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name[0]}. {self.last_name} ({self.salary})"

    def __repr__(self):
        return f"{self.first_name[0]} {self.last_name} {id(self)}"


department_a = Department("Engineering", "204B")

employee_a = Employee('Adam', 'Smith', 80000, department_a)
employee_b = Employee('Bradley', 'Jones', 64000, department_a)
employee_c = Employee('Christine', 'Smith', 94000, department_a, middle_name = 'Alexis')

department_b = Department("Sales", "601A")

Employee('Davis', 'Alexander', 76000, department_b)
Employee('Elexis', 'Jones', 49000, department_b)
Employee('Francis', 'Adamsson', 71000, department_b)

print(department_a.get_department_summary())

print(department_b.get_department_summary())

department_b.departmental_salary_increase(.03)

print(department_b.get_department_summary())



