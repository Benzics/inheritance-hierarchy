class Account:
    def __init__(self, balance):
        if balance < 0.0:
            print("The initial balance is invalid")
            self.balance = float(0.0)
        else:
            self.balance = float(balance)

        #credit method to add to the account balance
        def credit(self, amount):
            self.balance += float(amount)