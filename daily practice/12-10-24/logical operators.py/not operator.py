a=int(input("enter a number is "))
if not a:
    print("boolean value of a is True ")
if not(a%3==0 or a%5==0):
    print("10 is not divisible by either 10 or 3")
else:
    print("10 is divisible by either 3 or 5")