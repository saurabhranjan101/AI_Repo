class Student:
    def __init__(self, Name, Maths, Science, English):
        self.Name = Name
        self.Maths = Maths
        self.Science = Science
        self.English = English
        self.Percentage = int((Maths + Science + English) / 3)

        if self.Percentage >= 90:
            self.Grade = "A"
        elif self.Percentage >= 75:
            self.Grade = "B"
        elif self.Percentage >= 60:
            self.Grade = "C"
        else:
            self.Grade = "D"
    def __str__(self):
        return (f"Student Name : {self.Name},"
                f"Maths : {self.Maths}, Science : {self.Science}, English : {self.English}, "
                f"Percentage : {self.Percentage},"
                f"Grade : {self.Grade}"     
                )

student_list = []
while True:
    Name = input("Enter Student Name - ")
    if(Name.lower() == "exit"):
        break
    Maths = int(input("Enter Maths marks - "))
    Science = int(input("Enter Science marks - "))
    English = int(input("Enter English marks - "))
    s = Student(Name,Maths,Science,English)
    student_list.append(s)
print("\n--- All Students ---")
for stu in student_list:
    print(stu)
# Save all students to a file
with open("gradebook.txt", "w") as f:
    for stu in student_list:
        f.write(str(stu) + "\n")