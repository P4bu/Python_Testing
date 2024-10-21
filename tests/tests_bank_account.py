# python -m unittest discover -v -s tests
import unittest

from src.bank_account import BankAccount

class Bank_AccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)


    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(500)
        assert new_balance == 500    

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transfer(self):
        new_balance = self.account.transfer(9000)
        assert new_balance == 1000