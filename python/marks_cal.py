def marks_calculator(marks):
    print("\n-----MARKS REPORT-----")
    # Total
    total=sum(marks)
    print("Total Marks:", total)
    # Average
    average=total/len(marks)
    print("Average Marks:",average)
    # Highest and Lowest
    print("Highest Mark:",max(marks))
    print("Lowest Mark:",min(marks))
    # Pass and Fail Count
    pass_count=0
    fail_count=0
    for mark in marks:
        if mark>=35:
            pass_count+=1
        else:
            fail_count+=1
    print("Passed Students:",pass_count)
    print("Failed Students:",fail_count)
    # Grades
    print("\n----- GRADES -----")
    for i in range(len(marks)):
        mark=marks[i]
        if mark>=90:
            grade="A"
        elif mark>=75:
            grade="B"
        elif mark>=60:
            grade="C"
        elif mark>=35:
            grade="D"
        else:
            grade="F"
        print("Student",i+1,":",mark,"-> Grade",grade)
# Main Program
marks = list(map(int, input("Enter marks separated by spaces: ").split()))
marks_calculator(marks)
