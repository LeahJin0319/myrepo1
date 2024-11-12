class BankCustomer:
    def __init__(self, customer_id, name, balance=0):
        self.customer_id = customer_id
        self.name = name
        self.balance = balance
        self.transactions = {}  # To store transaction history, e.g., {"deposit": amount}

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Balance: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions[f"Deposit {len(self.transactions) + 1}"] = amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions[f"Withdrawal {len(self.transactions) + 1}"] = -amount
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def print_transactions(self):
        if self.transactions:
            print("Transaction History:")
            for action, amount in self.transactions.items():
                action_type = "Deposit" if amount > 0 else "Withdrawal"
                print(f"{action_type}: ${abs(amount):.2f}")
        else:
            print("No transactions found.")
