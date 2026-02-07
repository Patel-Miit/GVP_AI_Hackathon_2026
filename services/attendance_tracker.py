import json
import os
from typing import Dict, List, Optional
from models.student import Student


class AttendanceTracker:
    def __init__(self, data_file: str = "data/student_data.json"):
        self.students: Dict[str, Student] = {}
        self.data_file = data_file
        self.load_data()

    def validate_roll_no(self, roll_no: str) -> bool:
        try:
            return 1 <= int(roll_no) <= 9999
        except ValueError:
            return False

    def validate_semester(self, semester: int) -> bool:
        return 1 <= semester <= 8

    def validate_marks(self, marks: float) -> bool:
        return 0 <= marks <= 100

    def add_student(self, roll_no: str, name: str, semester: int):
        if not self.validate_roll_no(roll_no):
            return False, "Invalid roll number"
        if roll_no in self.students:
            return False, "Student already exists"
        if not self.validate_semester(semester):
            return False, "Invalid semester"

        self.students[roll_no] = Student(roll_no, name.strip(), semester)
        self.save_data()
        return True, "Student added successfully"

    def mark_attendance(self, roll_no: str, total: int, attended: int):
        if roll_no not in self.students:
            return False, "Student not found"
        if attended > total or total < 0:
            return False, "Invalid attendance data"

        s = self.students[roll_no]
        s.total_lectures = total
        s.attended_lectures = attended
        self.save_data()
        return True, "Attendance marked"

    def enter_marks(self, roll_no: str, marks: float):
        if roll_no not in self.students:
            return False, "Student not found"
        if not self.validate_marks(marks):
            return False, "Invalid marks"

        self.students[roll_no].marks = marks
        self.save_data()
        return True, "Marks saved"

    def get_student(self, roll_no: str) -> Optional[Student]:
        return self.students.get(roll_no)

    def get_all_students(self) -> List[Student]:
        return list(self.students.values())

    def get_analytics(self) -> dict:
        if not self.students:
            return {
                "total_students": 0,
                "avg_attendance": 0,
                "avg_marks": 0
            }

        attendance = [s.get_attendance_percentage() for s in self.students.values()]
        marks = [s.marks for s in self.students.values() if s.marks is not None]

        return {
            "total_students": len(self.students),
            "avg_attendance": round(sum(attendance) / len(attendance), 2),
            "avg_marks": round(sum(marks) / len(marks), 2) if marks else 0
        }

    def save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.students.items()}, f, indent=2)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file) as f:
                data = json.load(f)
                self.students = {k: Student.from_dict(v) for k, v in data.items()}
