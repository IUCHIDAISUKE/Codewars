def get_grade(s1, s2, s3):
    grade = (s1+s2+s3)//3
    if grade < 60:
        return "F"
    elif grade < 70:
        return "D"
    elif grade < 80:
        return "C"
    elif grade < 90:
        return "B"
    else:
        return "A"
