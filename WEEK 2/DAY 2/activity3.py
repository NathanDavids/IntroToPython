def calculate_average(marks, total_marks):
    average = sum(marks) / total_marks
    previous_average = float(input("Enter the student's average for the previous term: "))
    
    if previous_average > average:
        print("Student average down!")
        return 0
    else:
        print("Average: {:.2f}".format(average))
        if average >= 80:
            print("Passed with distinction!")
        elif average >= 60:
            print("Passed without distinction.")
        else:
            print("Failed (average lower than 60%).")
        return 1

marks = []
total_marks = 0

while True:
    mark = float(input("Enter a mark (enter 0 to finish): "))
    if mark == 0:
        break
    marks.append(mark)
    total_marks += 1

result = calculate_average(marks, total_marks)
if result == 0:
    print("Student average down!")