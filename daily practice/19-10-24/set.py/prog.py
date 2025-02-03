#write a program to enter of 3 subjects from the user &
#store them in a dictionary &add one by one use subjects name as
#subject name as key & marks as  value
marks={}
x=int(input("enter physics marks: "))
marks.update({"physics":x}),
y=int(input("enter computer science:"))
marks.update ({"computer science":x})
z=int(input("enter mathemtics"))
marks.update({"mathematics":z})
print(marks)