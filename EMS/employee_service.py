class EmployeeService:
    def __init__(self, esb):
        self.esb = esb
        self.employees = []

    def handle_message(self, message):
        if message["action"] == "list":
            self.list_employees()
        elif message["action"] == "add":
            self.add_employee(message["data"])

    def list_employees(self):
        print("Employee List:", self.employees)

    def add_employee(self, employee_data):
        self.employees.append(employee_data)
        print(f"Added Employee: {employee_data}")
