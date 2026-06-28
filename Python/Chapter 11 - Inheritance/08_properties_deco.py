#Access modifier -> Encapsulation
#private
# class Person:
#     def __init__(self, name, age):
#         self.__name = name #This is defined privately - private access modifier
#         self.__age = age #This is defined privately
#     def display_info(self):
#         print(f"Person name is {self.__name}")
#         print(f"Age is {self.__age}")
# person = Person("Saurabh",32)
# person.display_info()

# #Protected Access Modifier
# class Person:
#     def __init__(self, name, age):
#         self._name = name #This is defined privately - Protected Access Modifier
#         self._age = age #Protectedly defined
#     def display_info(self):
#         print(f"Person name is {self._name}")
#         print(f"Age is {self._age}")
# class Student(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def display_info(self):
#         print(f"Person name is {self._name}")
#         print(f"Age is {self._age}")
# person = Person("Saurabh",32)
# student1 = Student("Saurabh", 35)
# student1.display_info()  
# print(person._age)
# print(person._name)

#Using property decorator you can call method as value.
class Circle:
    def __init__(self, radius):
        self._radius = radius #_ is for the internal usage inside the class.
        print(radius)
    @property
    def radius(self):
        return self._radius
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
rad = int(input("Enter a value of radius - "))
r = Circle(rad) 
print(r.radius) #We are calling the method as value
print(r.area) #We are calling the method as value


#Getter & Setter

class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        if value <=0:
            print("Error - radius must be greater than 0")
        self._radius = value
c = Circle(5)
c.radius = 10
print(c.radius)    