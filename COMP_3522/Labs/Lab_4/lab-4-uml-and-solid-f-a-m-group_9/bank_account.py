from budget import Budget
from budget_category import BudgetCategory
from transaction import Transaction


class BankAccount:

    def __init__(self, bank_name, account_number, budgets, balance=0.0, ):
        """
        Initialize a BankAccount instance.

        :param bank_name: Name of the bank
        :param account_number: Account number
        :param balance: Initial balance of the account
        """
        # Validate budgets
        for cat in BudgetCategory:
            if cat not in budgets:
                raise ValueError(f"Missing budget category: {cat}")
        self.bank_name = bank_name
        self.account_number = account_number
        self.balance = balance
        self.budgets = {category: Budget(category, budgets.get(category)) for category in BudgetCategory}

    def would_exceed_balance(self, transaction):
        """
        Check if a transaction's amount would exceed the account balance.
        """
        return self.balance - transaction.amount < 0

    def get_budget_percent(self, budget):
        """
        Returns the percentage of the budget used.
        """
        return self.budgets[budget].get_budget_percent()

    def add_transaction(self, transaction):
        """
        Adds a transaction to a specific budget.

        :param transaction: Transaction instance to be added
        """
        if self.would_exceed_balance(transaction):
            print(f"Cannot add transaction. Exceeds the remaining balance of "
                  f"${self.balance}")
            return
        if isinstance(transaction, Transaction):  # This check is probably not needed
            self.budgets[transaction.category].add_transaction(transaction)

        self.balance = self.balance - transaction.amount
        print(f"\n✓ Transaction recorded: ${transaction.amount:.2f} at {transaction.merchant} "
              f"({transaction.category})")

    def get_all_transactions(self):
        """
        Returns a list of all transactions in the account across all budgets sorted by date.
        """
        transaction_list = []
        for budget in self.budgets.values():
            transaction_list.extend(budget.transactions)
        transactions_by_date = sorted(transaction_list, key=lambda transaction: transaction.timestamp)

        return transactions_by_date

    def get_budget_summary(self, budget_category):
        return self.budgets[budget_category].__str__()

    def display_budget_transactions(self, budget_category):
        self.budgets[budget_category].display_transactions()

    def __str__(self):
        """
        String representation of the BankAccount instance.
        """
        account_summary = [(f"----------ACCOUNT DETAILS----------\n"
                            f"Bank Account #{self.account_number}, {self.bank_name}\n"
                            f"-----------------------------------\n"
                            f"Balance: ${self.balance:.2f}\n"
                            f"-----------TRANSACTIONS------------")]
        transactions = [transaction.__str__() for transaction in self.get_all_transactions()]
        account_summary.extend(transactions)
        return "\n".join(account_summary)
