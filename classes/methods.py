# instance methods to update and use class attributes

class BankAccount:
    def __init__(self, first_name, last_name, account_id , account_type , pin ,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def display_balance(self):
        print(self.balance)
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(self.balance)

customer = BankAccount("John", "Doe", 123456, "Savings", 1234, 0)
customer.deposit(96.0)
customer.withdraw(25.0)
customer.display_balance()