#1)print the element of the following list using a loop 
# [1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)
print("end the program")
#2)search for a number of x in this tuple using loop
nums=[1,4,9,16,25,36,49,64,81,100,81]
x=81
idx=0
for i in nums:
    if(i==x):
        print("found at a idx of x is : ",x)
        idx+=1
        
