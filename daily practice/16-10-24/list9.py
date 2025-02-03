list1=[1,2,3,4,5,7,6,8]
list2=[6,8,5,6,7,6,8,7]
for item in list1:

    if item in  list2:
        print("yes considered over laping ")
    else:
        print("no")