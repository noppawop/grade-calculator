# report.py — แสดงผลรายงานเกรด

from grade import calculate_grade, calculate_gpa

def print_report(student_name, scores):
    """พิมพ์รายงานเกรดของนักศึกษา"""
    subjects = ["คณิตศาสตร์", "ภาษาอังกฤษ", "วิทยาการคอมพิวเตอร์"]
    print(f"\n{'='*40}")
    print(f"  รายงานเกรด: {student_name}")
    print(f"{'='*40}")
    for subject, score in zip(subjects, scores):
        grade = calculate_grade(score)
        print(f"  {subject:<25} {score:>5.1f}  [{grade}]")
    print(f"{'─'*40}")
    gpa = calculate_gpa(scores)
    print(f"  {'GPA':<25} {gpa:>7.2f}")
    print(f"{'='*40}\n")

if __name__ == "__main__":
    name = input("ชื่อนักศึกษา: ")
    scores = []
    for subject in ["คณิตศาสตร์", "ภาษาอังกฤษ", "วิทยาการคอมพิวเตอร์"]:
        s = float(input(f"คะแนน {subject}: "))
        scores.append(s)
    print_report(name, scores)