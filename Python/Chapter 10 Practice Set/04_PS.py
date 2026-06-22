#Update bank Account
class Bank:
    def __init__(self,Saving):
        self.Saving = Saving
    def deposit(self,amount):
        self.Saving = self.Saving + amount
trans = Bank(5000) #Object
trans.deposit(500)
print(trans.Saving)
# amount = int(input("Enter an amount - ")) 
# Bank.deposit(trans, amount) 
# print(trans.Saving)     