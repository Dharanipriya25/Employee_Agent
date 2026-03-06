# Student Agent
class StudentAgent:
    def handle_query(self, query):
        if "complaint" in query.lower() or "serious" in query.lower():
            return "ESCALATE"
        else:
            return "Your query has been solved by Student Agent"

# Attendance Agent
class AttendanceAgent:
    def __init__(self):
        self.attendance_record = {}

    def update_attendance(self, student_name, percentage):
        self.attendance_record[student_name] = percentage

    def check_attendance(self, student_name):
        percentage = self.attendance_record.get(student_name, 100)
        if percentage < 60:
            return "ESCALATE"
        elif 60 <= percentage < 75:
            return "WARNING: Attendance below 75%"
        else:
            return "Attendance is Satisfied"

# Coordinate Agent
class CoordinateAgent:
    def handle_issue(self, issue):
        print("\n[Coordinate Agent Activated]")
        print("Issue Received:", issue)
        if issue == "Low Attendance Critical":
            print("Coordinator escalating to admin...")
            return "ESCALATE_ADMIN"
        elif issue == "Student Query Escalation":
            print("Coordinator reviewing complex query...")
            return "ESCALATE_ADMIN"
        else:
            print("Coordinator solved this issue.")
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
    print("===== Smart Campus Multi Agent System =====")
    print("=========================================")

    # Create Agents
    student_agent = StudentAgent()
    attendance_agent = AttendanceAgent()
    coordinator = CoordinateAgent()
    admin = AdminAgent()

    # Student Query Handling
    print("\n--- Student Query Section ---")
    query = input("Enter Student Query: ")
    response = student_agent.handle_query(query)

    if response == "ESCALATE":
        coord_response = coordinator.handle_issue("Student Query Escalation")
        if coord_response == "ESCALATE_ADMIN":
            admin.intervene("Complex Student Query")
    else:
        print("Student Agent Response:", response)

    # Attendance Monitoring
    print("\n--- Attendance Monitoring Section ---")
    name = input("Enter Student Name: ")
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
