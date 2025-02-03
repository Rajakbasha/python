def order (x):
    print("method called for value :",x)
    return True if x>0 else False
a=order
b=order
c=order
if a(-1)or b(23) or c(10):
    print("atleast one of the number is positive ")