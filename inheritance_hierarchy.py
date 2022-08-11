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

    def debit(self, amount):
        if super().debit(amount):
            self.balance -= self.fee

#tests for the classes here

#test for Account class with less than 0 balance
test_account = Account(0)

# credit the account
test_account.credit(1000)

# debit the account
test_account.debit(97.5)

# print account balance
print("Account balance is: ", test_account.get_balance())


# Test for Savings_Account
test_savings_account = Savings_Account(100, 10)

interest = test_savings_account.calculate_interest()
test_savings_account.credit(interest)
print('Savings account balance is: ', test_savings_account.get_balance())

# Test for Checking_Account 
test_checking_account = Checking_Account(80, 5)
test_checking_account.credit(100)
test_checking_account.debit(20)
print('Checking account balance is: ', test_checking_account.get_balance())