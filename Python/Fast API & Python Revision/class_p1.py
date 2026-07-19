class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculate_bonus(self):
        return self.salary *0.10
    def show_bonus(self):
        print(f"{self.name}'s bonus is ₹ {self.calculate_bonus():.2f}")
emp = Employee("Mohan",80000)
print(emp.calculate_bonus())
emp.show_bonus()