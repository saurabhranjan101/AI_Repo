# class car:
#     def __init__(self, brand):
#         self.__brand = brand #Private attribute
#     @property
#     def brand(self): #getter
#         return self.__brand #Private attribute will be accessed within the class and you cannot access from outside or from object of the class.
# c = car("Suzuki")
# print(c.brand)

#adding a setter
class car:
    def __init__(self, brand):
        self.__brand = brand
    @property #Getter - it just return value and doesn't change the value
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, value):
        self.__brand = value
c = car("Suzuki")
print(c.brand)
c.brand = "Toyota" #Setting value to the brand.setter
print(c.brand)