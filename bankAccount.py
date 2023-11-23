class BankAccount:

    def __init__(self, account_holder, balance=0, account_number=None):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        # Deposit money into the account. Check if the amount is valid,
        # and update the balance accordingly.
        if amount > 0:
            self.balance += amount
            print(f'Deposit of ${amount} successful. New balance: ${self.balance}')
        else:
            print('Invalid deposit amount.')

    def withdraw(self, amount):
        # Withdraw money from the account. Check if the amount is valid,
        # and update the balance if there are sufficient funds.
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Withdrawal of ${amount} successful. New balance: ${self.balance}')
        else:
            print('Insufficient funds or invalid withdrawal amount.')

    def consult_balance(self):
        # Print the current balance of the account.
        print(f'Current balance of {self.account_holder}: ${self.balance}')


    def print_account_info(self):
        # Print detailed information about the account, including the
        # account holder's name, account number, and balance.
        print(f'Account Holder: {self.account_holder}')
        print(f'Account Number: {self.account_number}')
        print(f'Balance: ${self.balance}')