class ESB:
    def __init__(self):
        self.services = {}

    def register_service(self, name, service):
        self.services[name] = service

    def send_message(self, service_name, message):
        if service_name in self.services:
            self.services[service_name].handle_message(message)
        else:
            print(f"Service {service_name} not found.")

# Example of how to run the ESB
if __name__ == "__main__":
    esb = ESB()
    
    from employee_service import EmployeeService
    from payroll_service import PayrollService
    from attendance_service import AttendanceService
    from auth_service import AuthService
    
    esb.register_service("employee", EmployeeService(esb))
    esb.register_service("payroll", PayrollService(esb))
    esb.register_service("attendance", AttendanceService(esb))
    esb.register_service("auth", AuthService(esb))
    
    esb.send_message("auth", {"username": "john_doe", "password": "password123"})
    esb.send_message("employee", {"action": "list"})
    esb.send_message("payroll", {"employee_id": 1})
    esb.send_message("attendance", {"employee_id": 1, "status": "present"})
