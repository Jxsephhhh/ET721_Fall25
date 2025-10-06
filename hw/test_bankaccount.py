import unittest
from hw.bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Joseph", 100)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_sequence_operations(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.account.deposit(25)
        self.account.withdraw(75)
        self.assertEqual(self.account.get_balance(), 100)

if __name__ == '__main__':
    unittest.main()
