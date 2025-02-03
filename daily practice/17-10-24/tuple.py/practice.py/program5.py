#wap to check if a list contains a palidrome of elements (hint:use copy ()method)
list=[1,2,2]
list.copy()
list2=[3,3,3]
copy_list=list2.copy()
copy_list.reverse()
if(copy_list==list2 and list):
    print("palidrome")
else:
    print("its not palidrome")