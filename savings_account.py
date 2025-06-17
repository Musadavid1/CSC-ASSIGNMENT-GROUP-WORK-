# core/savings_account.py

from core.account import Account

class SavingsAccount(Account):
    def __init__(self, user, balance=0):
        super().__init__(user, balance)
        # Future: Add interest features
