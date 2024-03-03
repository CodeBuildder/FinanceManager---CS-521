from components import FinanceManager

def main():
    manager = FinanceManager('transactions.json')

    while True:
        print("\n\nHi!, I am your Personal Finance Manager")
        print("\n1. Add Transaction")
        print("\n2. Show Transactions")
        print("\n3. Show Summary")
        print("\n4. Exit")
        choice = input("\n\nEnter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: $ "))
            date = input("Enter date (DD/MM/YY): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            manager.add_transaction(amount, date, category, description)

        elif choice == '2':
            manager.display_transactions()

        elif choice == '3':
            summary = manager.summarize_expenses()
            total_expense = sum(summary.values())
            print("\n\n\n\n\n Your Expenses were:")
            for category, amount in summary.items():
                print(f"{category}: {amount} ({amount/total_expense*100:.2f}%)")

        elif choice == '4':
            break

if __name__ == "__main__":
    main()