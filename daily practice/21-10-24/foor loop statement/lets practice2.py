# 1) write a program find sum of first n number (using while)
n=10
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("some total natural numbers are :",sum)
# write a program to find the factorial of first n numer (using for loop)

n=int(input("enter a number: "))
fact=1
for i in range(1,n+1):
    fact*=i
    i+=1
    print("factorial of =",fact)
print( " factorial number is : ",n)