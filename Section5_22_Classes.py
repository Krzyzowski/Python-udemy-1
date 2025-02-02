#example_1

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"
    
my_book = Book(title="1984", author="George Orwell")
my_book2 = Book(title="The code book", author="Simon Singh")

print(my_book.display_info())

print(my_book2.display_info())

print( )
#example_2

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance is ${self.balance}"
        return "inavid deposit amount."
    
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdraw ${amount}. New balance is ${self.balance}."
        return "inwalid withdrawal amount or insufficient funds."
    
    def get_balance(self):
        return f"The current balance is ${self.balance}."
    
my_account = BankAccount(account_number="1234" , account_holder="Bob Smith" , balance=1000)
my_account2 = BankAccount(account_number="5678" , account_holder="John Doe")

print(my_account.deposit(500))

print(my_account.withdraw(200))

print(my_account.get_balance())

print(my_account2.get_balance())

print(my_account2.deposit(5000))

print(my_account2.get_balance())
