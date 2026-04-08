# grade.py — ระบบตัดเกรดนักศึกษา

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

if __name__ == "__main__":
    score = float(input("กรอกคะแนน (0-100): "))
    grade = calculate_grade(score)
    print(f"เกรดที่ได้: {grade}")