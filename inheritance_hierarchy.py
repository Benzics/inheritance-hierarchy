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

        #debit method that debits from the account balance
        def debit(self, amount):
            if self.balance < amount:
                print("Insufficient funds")
                return False
            else:
                self.balance -= float(amount)
                return True

        #returns the current balance
        def get_balance(self):
            return self.balance


class Savings_Account(Account):
    def __init__(self, balance, interest):
        super().__init__(balance)
        self.interest = float(interest)

    def calculate_interest(self):
        interest_earned = self.interest * self.balance
        return float(interest_earned)


class Checking_Account(Account):
    def __init__(self, balance, fee):
        super().__init__(balance)
        self.fee = float(fee)

    #subtracts fee from the account balance
    def credit(self, amount):
        super().credit(amount)
        self.balance -= self.fee
