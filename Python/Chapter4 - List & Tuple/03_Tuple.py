a= (1,2,3,4,5,6)
print(type(a))

#Empty Tuple
b = ()
print(type(b))

#Tuple with single value
c =(1,) ##we cannot write c=(1) as this will be integer
print(type(c))

d = (1,45,"Saurabh","False")
print(d[0])
d[1] = 666
print(d)