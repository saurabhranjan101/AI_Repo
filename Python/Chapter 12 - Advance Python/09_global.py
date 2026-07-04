a = 89 #Global Variable - can be used within or outside of function
def fun():
    a = 3 #Local Variable fo Function
    print(a)
fun()
print(a)

#global keyword
a = 89 
def fun():
    global a #this change the global variable to variable inside function
    a = 3 
    print(a)
fun()
print(a)