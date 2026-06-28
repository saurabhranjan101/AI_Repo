#Base Class
class employee:
    company1 = "ITC"
    name = "Monty"
    def show(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")
#Derived Class
class programmer(employee):
    company2 = "Infosys"
    def language(self):
        print(f"Language is {self.language}")

a = employee()
b = programmer()
print(f"{a.company1}, {b.company1},{b.name}, {b.company2}") #we are inheriting name using b object