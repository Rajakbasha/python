#constructor:
#all classes have a function called _init_ function which is alwas executed when the class is being initited 
class student:
    def __init__(self,name,marks,grade):
        self.name= name
        self.marks=marks
        self.grade=grade
        print("adding a new student in data base ...")
s1=student("rajak",79,"grade of is: A")
print(s1.name,s1.marks,s1.grade)
s2=student("shaik rajak basha ",90," grade of  is: A+")
print(s2.name,s2.marks,s1.grade)
s3=student("jack",90,"the garder of is : A+")
print(s3.name,s3.marks,s1.grade)
"""
the self parameter is areference to the current instance of the class,and is used
to access variables  that belongs to the class .
"""