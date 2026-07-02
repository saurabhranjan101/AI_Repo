from abc import ABC,abstractmethod
class Car(ABC): #This class is Abstract class
    def show(self):
        print("Every car has four wheels")
    @abstractmethod
    def speed(self):
        pass
class Maruti(Car):
    def speed(self):
        print("Speed is 100kmph")
class Suzuki(Car):
    def speed(self):
        print("Speed is 70kmph")
obj = Maruti()
obj.show()
obj.speed()

obj1 = Suzuki()
obj1.speed()
obj1.show()