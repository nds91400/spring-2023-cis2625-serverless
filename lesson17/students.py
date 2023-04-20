grade = [67, 78, 77, 87, 91, 69]

for x in range(len(grade)):
    if grade[x] >= 90:
        print("A")
    elif grade[x] >= 80:
        print("B")
    elif grade[x] >= 70:
        print("C")
    elif grade[x] >= 60:
        print("D")
    else:
        print("F")