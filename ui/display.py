from models.student import Student
from services.attendance_tracker import AttendanceTracker


def print_header():
    print("\n" + "=" * 60)
    print(" SMART ATTENDANCE & PERFORMANCE TRACKER ")
    print("=" * 60)


def print_menu():
    print("""
1. Add Student
2. Mark Attendance
3. Enter Marks
4. View Student Report
5. Display All Students
6. View Analytics
7. Exit
""")


def display_student(student: Student):
    print(f"""
Roll No    : {student.roll_no}
Name       : {student.name}
Semester   : {student.semester}
Attendance : {student.get_attendance_percentage()}%
Status     : {student.get_attendance_warning()}
Marks      : {student.marks or "N/A"}
Performance: {student.get_performance_remark()}
""")


def display_all_students(tracker: AttendanceTracker):
    for s in tracker.get_all_students():
        print(f"{s.roll_no:<8} {s.name:<20} {s.get_attendance_percentage():<6}% {s.marks}")
