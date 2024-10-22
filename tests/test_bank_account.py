# python -m unittest discover -v -s tests
import unittest, os

from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file='transaction_log.txt')

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, 'r') as f:
            return len(f.readlines())        

    def test_deposit(self):
        new_balance = self.account.deposit(500)
       # assert new_balance == 1500
        self.assertEqual(new_balance, 1500, 'El balance no es igual')

    def test_withdraw(self):
        new_balance = self.account.withdraw(500)
       # assert new_balance == 500
        self.assertEqual(new_balance, 500, 'El balance no es igual')    

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transfer(self):
        new_balance = self.account.transfer(9000)
        assert new_balance == 1000

    def test_transaction_log(self):
        new_balance = self.account.deposit(500)
        assert os.path.exists('transaction_log.txt')

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2