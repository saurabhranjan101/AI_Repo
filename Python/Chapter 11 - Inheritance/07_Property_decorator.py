class Developer:
    def __init__(self, name, age, salary, companyName): #Constructor
        self.name = name
        self.age = age
        self.salary = salary
        self.companyName = companyName
    @property #We are defining getter
    def company(self):
        return self.companyName
    @company.setter #We are defining setter
    def company(self, companyName):
        self.companyName = companyName
developer_object = Developer("Alex", 22, 65000, "Infy")
print(developer_object.company) ##This will give company as Infy becoz this is returning the value of companyName
developer_object.company = "Google"
print(developer_object.company)