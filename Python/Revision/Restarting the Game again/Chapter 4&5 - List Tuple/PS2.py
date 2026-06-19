i = 1
marks = []
for i in range(1,7):
    m = input(f"Enter a marks of Student{i}- ")
    marks.append(m)
    i+=1
marks.sort()
print(marks)