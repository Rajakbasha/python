#wap to check if a list contains a palidrome of elements (hint:use copy ()method)
list1=[1,2,1]
list1.copy()
list2=(1,2,3)
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palidrome")
else:
    print("not palidrome")