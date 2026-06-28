#Parent Class 1
class employee:
    company1 = "ITC"
    name = "Monty"
    salary = 5000
    def show(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")

#Parent Class 2
class coder:
    Language = "python"
    def printLanguage(self):
        print(f"Language is {self.Language}")

#Derived Class
class programmer(employee, coder):
    company2 = "Infosys"
    def program(self):
        print(f"Company is {self.company2}")

##a = employee()
b = programmer()
print(f"{b.company1}, {b.company2},{b.name},{b.Language}") #we are inheriting name using b object
b.show()
b.printLanguage()
b.program() 