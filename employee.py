# Employee Agent
class EmployeeAgent:
    def handle_query(self, query):
        if "complaint" in query.lower() or "serious" in query.lower():
            return "ESCALATE"
        else:
            return "Your query has been solved by Employee Agent"


# Employee Attendance Agent
class EmployeeAttendanceAgent:
    def __init__(self):
        self.attendance_record = {}

    def update_attendance(self, employee_name, percentage):
        self.attendance_record[employee_name] = percentage

    def check_attendance(self, employee_name):
        percentage = self.attendance_record.get(employee_name, 100)

        if percentage < 50:
            return "ESCALATE"
        elif 50 <= percentage < 70:
            return "WARNING: Attendance below 70%"
        else:
            return "Attendance is Satisfied"


# HR Coordinator Agent
class HRCoordinatorAgent:
    def handle_issue(self, issue):
        print("\n[HR Coordinator Activated]")
        print("Issue Received:", issue)

        if issue == "Low Attendance Critical":
            print("HR Coordinator escalating to Admin...")
            return "ESCALATE_ADMIN"

        elif issue == "Employee Query Escalation":
            print("HR Coordinator reviewing complex query...")
            return "ESCALATE_ADMIN"

        else:
            print("HR Coordinator solved this issue.")
            return "RESOLVED"


# Admin Agent
class AdminAgent:
    def intervene(self, issue):
        print("\n[Human Admin Intervention Required]")
        print("Admin resolving issue:", issue)
        print("Admin has taken necessary action\n")


# Main Function
def main():
    print("=========================================")
    print("===== Smart Office Multi Agent System =====")
    print("=========================================")

    # Create Agents
    employee_agent = EmployeeAgent()
    attendance_agent = EmployeeAttendanceAgent()
    coordinator = HRCoordinatorAgent()
    admin = AdminAgent()

    # Employee Query Handling
    print("\n--- Employee Query Section ---")
    query = input("Enter Employee Query: ")

    response = employee_agent.handle_query(query)

    if response == "ESCALATE":
        coord_response = coordinator.handle_issue("Employee Query Escalation")

        if coord_response == "ESCALATE_ADMIN":
            admin.intervene("Complex Employee Query")

    else:
        print("Employee Agent Response:", response)

    # Attendance Monitoring
    print("\n--- Employee Attendance Section ---")
    name = input("Enter Employee Name: ")
    percentage = float(input("Enter Attendance Percentage: "))

    attendance_agent.update_attendance(name, percentage)
    attendance_status = attendance_agent.check_attendance(name)

    if attendance_status == "ESCALATE":
        coord_response = coordinator.handle_issue("Low Attendance Critical")

        if coord_response == "ESCALATE_ADMIN":
            admin.intervene("Critical Low Attendance Case")

    else:
        print("Attendance Agent:", attendance_status)


# Run Main
if __name__ == "__main__":
    main()