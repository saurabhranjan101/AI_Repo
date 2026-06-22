#Write a Class ‘Train’ which has methods to book a ticket,
#get status (no of seats) and get fare information of 
#train running under Indian Railways.
from random import randint
class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
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