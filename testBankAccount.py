from bankAccount import BankAccount
import unittest

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Create instances of BankAccount to be used in tests.
        self.account1 = BankAccount('John Doe', account_number='123456')
        self.account2 = BankAccount('Jane Smith', account_number='789012')

    def test_deposit(self):
        # Test if the deposit method works correctly.
        self.account1.deposit(500)
        self.assertEqual(self.account1.balance, 500)

    def test_withdraw_sufficient_funds(self):
        # Test if the withdraw method works correctly with sufficient funds.
        self.account1.deposit(1000)
        self.account1.withdraw(300)
        self.assertEqual(self.account1.balance, 700)

    def test_withdraw_insufficient_funds(self):
        # Test if the withdraw method handles insufficient funds correctly.
        self.account1.deposit(200)
        self.account1.withdraw(300)
        self.assertEqual(self.account1.balance, 200)


if __name__ == '__main__':
    unittest.main()