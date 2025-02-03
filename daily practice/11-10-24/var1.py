#input two variables 
a=int(input("enter the value of first variable:"))
b=int(input("enter the value of second variable:"))
print(f"original values : a ={a} ,b={b}")
temp=a
a=b
b=temp
print(f"swapped values : a={a},b={b}")