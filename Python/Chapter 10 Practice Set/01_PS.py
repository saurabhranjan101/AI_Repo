#Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):  ##Dendur method - getts called as soon as object gets created
        self.name = name
        self.salary = salary
        self.pincode = pincode
p = Programmer("Saurabh", 300000, 560068) #Object with Atributes created then dendur method will get called
print(p.name, p.company, p.salary, p.pincode)        
r = Programmer("Rohan", 200000, 560037) #Object with Atributes created then dendur method will get called
print(r.name, r.company, r.salary, r.pincode)        