# grade.py — ระบบตัดเกรดนักศึกษา

def calculate_weighted_gpa(scores, credits):
    """คำนวณ GPA แบบถ่วงน้ำหนักตาม credit"""
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    total_points = sum(grade_points[calculate_grade(s)] * c
                       for s, c in zip(scores, credits))
    total_credits = sum(credits)
    return round(total_points / total_credits, 2)

def calculate_grade(score):
    """รับคะแนน 0-100 แล้วคืนค่าเกรด"""
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def calculate_gpa(scores):
    """รับ list คะแนนหลายวิชา แล้วคืน GPA (0.00-4.00)"""
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    grades = [calculate_grade(s) for s in scores]
    gpa = sum(grade_points[g] for g in grades) / len(grades)
    return round(gpa, 2)

def get_honor_roll(students_scores):
    # TODO: กำลังทำอยู่ ยังไม่เสร็จ
    pass

if __name__ == "__main__":
    print("=== ระบบตัดเกรด ===")
    score = float(input("กรอกคะแนน (0-100): "))
    grade = calculate_grade(score)
    print(f"เกรดที่ได้: {grade}")