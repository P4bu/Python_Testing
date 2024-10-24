# python -m unittest discover -v -s tests
import unittest, os
from unittest.mock import patch
from src.exceptions import WithdrawalTimeRestrictionError, InsufficientFundsError
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

    def test_withdraw_raises_error_when_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(100)
        self.assertAlmostEqual(new_balance, 900)  

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)    

    def test_deposit_varios_ammounts(self):
        test_cases = [
            {'ammount': 100, 'expected': 1100},
            {'ammount': 3000,'expected': 4000},
            {'ammount': 4500,'expected': 5500}
        ]
        for case in test_cases:
            with self.subTest(case = case):
                self.account = BankAccount(balance=1000, log_file='transaction.txt')
                new_balance = self.account.deposit(case['ammount'])
                self.assertEqual(new_balance, case['expected'])