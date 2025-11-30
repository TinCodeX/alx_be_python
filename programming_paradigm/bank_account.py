# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Initialize a new BankAccount.
        :param initial_balance: (float) Optional starting balance — defaults to 0.0
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add the specified amount to the balance.
        :param amount: (float) the amount to deposit — should be non-negative
        """
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative")
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Subtract the amount from balance if funds are sufficient.
        :param amount: (float) the amount to withdraw — should be non-negative
        :return: True if withdrawal succeeded, False otherwise
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be non-negative")
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Print the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
