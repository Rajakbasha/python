#wrute a program to find the greatest of 3 numbers entered by the user
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third  number: "))
if(a>=b and a>=c):
    print("first number is largest")
elif(b>=c):
    print("second number is largest")
else:
    print("third number is largest")
    