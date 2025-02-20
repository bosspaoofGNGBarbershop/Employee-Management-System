class PayrollService:
    def __init__(self, esb):
        self.esb = esb

    def handle_message(self, message):
        if "employee_id" in message:
            self.process_payroll(message["employee_id"])

    def process_payroll(self, employee_id):
        # Simulate payroll processing
        print(f"Processed payroll for employee ID: {employee_id}")
