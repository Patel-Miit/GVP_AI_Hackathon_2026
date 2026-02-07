from typing import Optional

class Student:
    """Student model with attendance and performance tracking"""

    def __init__(self, roll_no: str, name: str, semester: int):
        self.roll_no = roll_no
        self.name = name
        self.semester = semester
        self.total_lectures = 0
        self.attended_lectures = 0
        self.marks: Optional[float] = None

    def get_attendance_percentage(self) -> float:
        if self.total_lectures == 0:
            return 0.0
        return round((self.attended_lectures / self.total_lectures) * 100, 2)

    def get_performance_remark(self) -> str:
        if self.marks is None:
            return "Not Evaluated"
        if self.marks >= 75:
            return "Good"
        elif self.marks >= 50:
            return "Average"
        return "Needs Improvement"

    def get_attendance_warning(self) -> str:
        return "⚠ Attendance Shortage" if self.get_attendance_percentage() < 75 else "✓ Satisfactory"

    def to_dict(self) -> dict:
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "semester": self.semester,
            "total_lectures": self.total_lectures,
            "attended_lectures": self.attended_lectures,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data: dict):
        student = cls(data["roll_no"], data["name"], data["semester"])
        student.total_lectures = data.get("total_lectures", 0)
        student.attended_lectures = data.get("attended_lectures", 0)
        student.marks = data.get("marks")
        return student
