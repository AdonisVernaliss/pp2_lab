class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, inc):
        self.balance += inc
        print(self.owner,"completed the deposit. Current balance is",self.balance)

    def withdraw(self, dic):
        if dic > self.balance:
            print("Error!")
        else:
            self.balance-=dic
            print(self.owner,"completed the withdrawal. Current balance is",self.balance)

a1 = Account("Mike", 150000)

a1.withdraw(5000)
a1.withdraw(200000)
a1.deposit(5)