#write a program to check if a number is a multiple 5,6,7
x=int(input("enter a number: "))
if(x%7==0):
    print("multiple of 7 ")
elif(x%5==0):
    print("multiple of 5")
elif(x%6==0):
    print("multiple is 6")
else:
    print(" this is not multiple of 5,6,7")