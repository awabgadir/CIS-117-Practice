class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, description, amount):
        self.transactions.append({
            "date": date,
            "description": description,
            "amount": amount
        })

    def view_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction['date']}: {transaction['description']} - {transaction['amount']}")

    def calculate_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction["amount"]
        return balance

# Create an instance of the BudgetTracker class
budget_tracker = BudgetTracker()

# Add some transactions
budget_tracker.add_transaction("2022-01-01", "Income", 1000)
budget_tracker.add_transaction("2022-01-01", "Rent", -800)
budget_tracker.add_transaction("2022-01-02", "Groceries", -100)
budget_tracker.add_transaction("2022-01-03", "Entertainment", -50)

# View the transactions
budget_tracker.view_transactions()

# Calculate the balance
balance = budget_tracker.calculate_balance()
print(f"Current balance: {balance}")
