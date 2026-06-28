class Employee:
    a = 1
    @classmethod #This is to print value of class attribute.
    def show(cls):
        print(f"Class value of A is {cls.a}")
e = Employee()
e.a = 45
e.show()