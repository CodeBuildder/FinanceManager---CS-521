import unittest
from finance_manager import FinanceManager

class TestFinanceManager(unittest.TestCase):
    def test_add_transaction(self):
        manager = FinanceManager('test_transactions.json')
        manager.add_transaction(100, '2024-02-15', 'Groceries', 'Test')
        self.assertEqual(len(manager), 1)

    def test_summarize_expenses(self):
        manager = FinanceManager('test_transactions.json')
        manager.add_transaction(50, '2024-02-15', 'Utilities', 'Electricity')
        summary = manager.summarize_expenses()
        self.assertIn('Utilities', summary)
        self.assertEqual(summary['Utilities'], 50)

if __name__ == '__main__':
    unittest.main()
