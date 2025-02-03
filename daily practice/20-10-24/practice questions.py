# 1) print numbers 1 to 10
i=1
while i<=100:
    print(i)
    i+=1

print("********** first program ended ********* ")
#2)print numbers 100 to 1
i=100
while i>0:
    print(i)
    i-=1
    
    
print("+++++++++++ second program ended ++++++++++")    
# 3) print the multiplication of table of a number n .
n=int(input("enter a number : "))
i=1
while i<=20:
    print(n*i)
    i+=1
print("=========third program ended========= ")
#4) print the element of the  following list using a loop 
# [ 1,4,9,16,25,36,49,64,81,100]
number=[ 1,4,9,16,25,36,49,64,81,100]
print(number[1])
print(number[2])
print(number[3])
print(number[4])
print(number[5])
print(number[6])
print(number[7])
print(number[8])
print(number[9])
print(number[0])
print(len(number))
print("===========fourth program ended ================")
#example : heroes which movie action of cinema name 
heroes=["prabhas:mirchi","ramcharan:rangastalam","NTR: TEMPER","MAHESHBABU: pokiri"]
idx=0
while idx<len(heroes):
    print(heroes[idx])
    idx+=1
print(" +++=========++++4th program ended heroes+++++++++========= ")
#5)search for a number x in this tuple using loop:
#[ 1,4,9,16,25,36,49,64,81,100]
nums=[ 1,4,9,16,25,36,49,64,81,100,4]
x=4
idx=0
while idx<len(nums):
     print(nums[idx])
     idx+=1
print(" ___________ cpmpleted 5 th question___________")
nums=[1,4,9,16,25,36,49,64,81,40,4]
x=16
i=0
while i <len(nums):
    if(nums[i]==x):
        print("found at idx 4:  ")
        i+=1
print("@@@@@@@@@@@@@@@@@")

