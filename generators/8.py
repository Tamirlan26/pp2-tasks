class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
    def takeout(self,amount):
        if amount<self.balance:
            self.balance-=amount
        else:
            print("You do not have enough to takeout")
    def show(self):
        print(self.balance)

account1 = Bank("Иван", 1000)

account1.show()   # 1000
account1.deposit(500)
account1.show()   # 1500
account1.takeout(200)
account1.show()   # 1300

