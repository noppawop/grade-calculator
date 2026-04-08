# test_grade.py — ทดสอบ functions

from grade import calculate_grade, calculate_gpa

def test_calculate_grade():
    assert calculate_grade(85) == "A"
    assert calculate_grade(75) == "B"
    assert calculate_grade(65) == "C"
    assert calculate_grade(55) == "D"
    assert calculate_grade(40) == "F"
    print("calculate_grade: ผ่านทุก test")

def test_calculate_gpa():
    assert calculate_gpa([85, 75, 65]) == 3.0
    assert calculate_gpa([40, 40, 40]) == 0.0
    print("calculate_gpa: ผ่านทุก test")

if __name__ == "__main__":
    test_calculate_grade()
    test_calculate_gpa()
    print("\n🎉 ผ่านทุก test!")