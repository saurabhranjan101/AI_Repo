fruits = ['apple','grapes','banana','orange','pineapple']
print(fruits[0], "&",fruits[len(fruits)-1])
fruits.insert(1,'Mango') #replace second fruits with Mango
print(fruits) #Updated list

fruits = ['apple','grapes','banana','orange','pineapple']
print(f"{fruits[0]} & {fruits[len(fruits)-1]}")

#Tuple
color = ('red', 'black', 'grey')
color_list = list(color) #converting tuple to list
color_list[2] = 'Purple'
color = tuple(color_list) #converting list to tuple
print(color)
print(color[1])

#List Operation
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)
numbers.remove(30)
print(numbers)

#Tuple Methods – Count & Index
marks = (85, 90, 75, 90, 60, 90)
print(marks.count(90))
print(marks.index(75))

#Q5. Advanced – Nested Structures
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
t = students[1]
print(t[1]) #Bob’s marks.
students.append(("Diana", 88))
print(students)
# Sort students by marks (ascending)
students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)
