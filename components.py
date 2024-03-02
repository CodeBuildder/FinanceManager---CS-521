import json
import os

class FinanceManager:
    def __init__(self, data_file):
        self._data_file = data_file  # Private attribute
        self.transactions = self._load_transactions()   # Public attribute
  

    def __str__(self):
        return f"FinanceManager with {len(self.transactions)} transactions."

    def __len__(self):
        return len(self.transactions)

    def _load_transactions(self):  # Private method
        if os.path.exists(self._data_file):
            with open(self._data_file, 'r') as file:
                return json.load(file)
        return []

    def save_transactions(self):
        with open(self._data_file, 'w') as file:  # Corrected to use the private attribute
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, amount, date, category, description):
        self.transactions.append({
            'amount': amount, 'date': date, 'category': category, 'description': description
        })
        self.save_transactions()

    def display_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction['date']} - {transaction['category']} - {transaction['amount']}: {transaction['description']}")

    def summarize_expenses(self):
        summary = {}
        for transaction in self.transactions:
            category = transaction['category']
            summary[category] = summary.get(category, 0) + transaction['amount']
        return summary


