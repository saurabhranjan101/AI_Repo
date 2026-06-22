#Calculate area of rectangle using init constructor

# class rectangle:
#     def __init__(self, length,breadth):
#         self.length = length
#         self.breadth = breadth
# area_rectangle = rectangle(10, 20)
# print(f"Ares of rectangle is {area_rectangle.length * area_rectangle.breadth} Sqft")        

#Let's take input from user

class rectangle:
    def __init__(self, length,breadth):
        self.length = length
        self.breadth = breadth
length = int(input("Enter length - "))
breadth = int(input("Enter Breadth - "))
area_rectangle = rectangle(length, breadth)
print(f"Ares of rectangle is {area_rectangle.length * area_rectangle.breadth} Sqft")