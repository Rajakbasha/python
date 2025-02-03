marks=input(int("enter your marks:[->]:"))
if (marks<=90):
    grade="A"
elif(marks>=8 and marks<90):
    grade=("B")
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("grade of student ->",grade)
    