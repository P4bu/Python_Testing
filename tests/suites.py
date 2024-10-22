import unittest

from tests.test_bank_account import BankAccountTest

def banck_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTest('test_deposit'))
    suite.addTest(BankAccountTest('test_withdraw'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(banck_account_suite())