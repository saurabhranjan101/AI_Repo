#Can you change the self-parameter inside a class to something else (say “harry”). 
#Try changing self to “slf” or “harry” and see the effects.

from random import randint
class train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Train is booked in {self.trainNo} from {fro} to {to}")
    
    def status(self):
        print(f"Train Number - {self.trainNo} is running on time")
        
    def getFare(self, fro, to):
        print(f"Train  fare for {self.trainNo} booked from {fro} to {to} is {randint(222, 5555)}")
t = train(12835)
t.book("HTE","YPR")
t.status()
t.getFare("HTE","YPR")