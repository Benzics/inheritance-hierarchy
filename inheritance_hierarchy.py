class Account:
    def __init__(self, balance):
        if balance < 0.0:
            print("The initial balance is invalid")
            self.balance = float(0.0)
        else:
            self.balance = float(balance)