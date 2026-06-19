#Check if a year is a leap year.
y = int(input("Enter a year - "))
if(y%4 == 0):
    print("It's a leap year")
else:
    print("It's not a leap year")


#Grade a student based on marks.
marks = float(input("Enter a marks of student - "))

if(marks >75):
    print("First Class with Distinction")
elif(marks>=60):
    print("First Class")
elif(marks>=50 and marks<60):
    print("Second Class")
elif(marks>=35 and marks<50):
    print("Just passed")
else:
    print("Fail")