# core/current_account.py

from core.account import Account

class CurrentAccount(Account):
    def __init__(self, user, balance=0):
        super().__init__(user, balance)
        # Future: Add overdraft limit
