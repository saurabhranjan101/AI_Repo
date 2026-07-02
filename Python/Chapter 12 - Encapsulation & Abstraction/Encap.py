class A:
    _a = 10 #Protected
    __b = 20 #Private
    def show(self):
        print(f"Value of a is {self._a}")
        print(f"Value of b is {self.__b}")
obj = A()
obj.show()
print("Outside of class", obj._a)
# print(obj.__b)

#We can define protected with single underscore(_) and private with double underscore(__). 
# Protected can access from method defined within class and from class object.
#Private only be access from class method and not from class object.