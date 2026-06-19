fruits = []
i = 1
# f1 = input("Please enter Fruit - ")
# f2 = input("Please enter Fruit - ")
# f3 = input("Please enter Fruit - ")
# f4 = input("Please enter Fruit - ")
# f5 = input("Please enter Fruit - ")
# f6 = input("Please enter Fruit - ")
# fruits.insert(1,f1)
# fruits.insert(2,f2)
# fruits.insert(3,f3)
# fruits.insert(4,f4)
# fruits.insert(5,f5)
# fruits.insert(6,f6)
while(i<=7):
    f1 = input(f"Please enter Fruit Name{i}-")
    fruits.insert(i,f1)
    i+=1
print(fruits)