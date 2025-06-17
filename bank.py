# core/bank.py

from core.savings_account import SavingsAccount
from core.current_account import CurrentAccount

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # key: (user, account_type)

    def create_account(self, user, account_type, balance=0):
        key = (user, account_type)
        if key in self.accounts:
            return f"{account_type} account for {user} already exists."

        if account_type == "Savings":
            self.accounts[key] = SavingsAccount(user, balance)
        elif account_type == "Current":
            self.accounts[key] = CurrentAccount(user, balance)
        else:
            return "Invalid account type."

        return f"{account_type} account created for {user} with ${balance}."

    def deposit(self, user, account_type, amount):
        key = (user, account_type)
        if key not in self.accounts:
            return f"No {account_type} account found for {user}."
        return self.accounts[key].deposit(amount)

    def withdraw(self, user, account_type, amount):
        key = (user, account_type)
        if key not in self.accounts:
            return f"No {account_type} account found for {user}."
        return self.accounts[key].withdraw(amount)

    def get_balance(self, user, account_type):
        key = (user, account_type)
        if key not in self.accounts:
            return "Account not found."
        return self.accounts[key].get_balance()
