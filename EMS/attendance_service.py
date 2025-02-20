class AttendanceService:
    def __init__(self, esb):
        self.esb = esb
        self.attendance_records = []

    def handle_message(self, message):
        if "employee_id" in message and "status" in message:
            self.record_attendance(message["employee_id"], message["status"])

    def record_attendance(self, employee_id, status):
        self.attendance_records.append({"employee_id": employee_id, "status": status})
        print(f"Recorded attendance for employee ID: {employee_id} with status: {status}")
