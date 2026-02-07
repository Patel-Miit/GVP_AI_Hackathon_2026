from services.attendance_tracker import AttendanceTracker
from ui.display import (
    print_header,
    print_menu,
    display_student,
    display_all_students
)

def main():
    tracker = AttendanceTracker()
    print_header()

    while True:
        print_menu()
        choice = input("Choice: ").strip()

        # 1️⃣ Add Student
        if choice == "1":
            r = input("Roll No: ").strip()
            n = input("Name: ").strip()
            s = int(input("Semester (1-8): "))
            success, msg = tracker.add_student(r, n, s)
            print(msg)

        # 2️⃣ Mark Attendance
        elif choice == "2":
            r = input("Roll No: ").strip()
            total = int(input("Total Lectures: "))
            attended = int(input("Lectures Attended: "))
            success, msg = tracker.mark_attendance(r, total, attended)
            print(msg)

        # 3️⃣ Enter Marks
        elif choice == "3":
            r = input("Roll No: ").strip()
            marks = float(input("Marks (0-100): "))
            success, msg = tracker.enter_marks(r, marks)
            print(msg)

        # 4️⃣ View Student Report
        elif choice == "4":
            r = input("Roll No: ").strip()
            student = tracker.get_student(r)
            if student:
                display_student(student)
            else:
                print("Student not found!")

        # 5️⃣ Display All Students
        elif choice == "5":
            display_all_students(tracker)

        # 6️⃣ View Analytics
        elif choice == "6":
            analytics = tracker.get_analytics()
            print("\n===== SYSTEM ANALYTICS =====")
            print(f"Total Students     : {analytics['total_students']}")
            print(f"Average Attendance : {analytics['avg_attendance']}%")
            print(f"Average Marks      : {analytics['avg_marks']}")
            print("============================")

        # 7️⃣ Exit
        elif choice == "7":
            print("\nThank you for using Smart Attendance System 👋")
            break

        else:
            print("⚠ Invalid choice! Please select 1-7")

if __name__ == "__main__":
    main()
