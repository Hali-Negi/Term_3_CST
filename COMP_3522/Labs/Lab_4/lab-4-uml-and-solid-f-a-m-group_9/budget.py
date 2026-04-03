from budget_category import BudgetCategory
from transaction import Transaction


class Budget:
    """
    A budget class representing a budget for a specific category.
    """

    def __init__(self, category, limit=0.0):
        """
        Initialize a Budget instance. Holds a list of transactions for a specific category.

        :param category: the BudgetCategory of the budget
        :param limit: Spending limit for the budget
        """
        if limit < 0:
            raise ValueError("Limit cannot be negative")
        if category not in BudgetCategory:
            raise ValueError("Category must be a valid BudgetCategory")
        self.category = category
        self._limit = limit
        self.transactions = []

    def get_total_transaction_values(self):
        """
        Calculate the total value of all transactions in this budget category.

        :return: Total amount from all transactions
        """
        total = sum(transaction.amount for transaction in self.transactions)
        return total
    
    def add_transaction(self, transaction):
        """
        Record a new transaction in this budget category.

        :param transaction: Transaction instance to be recorded
        """
        if isinstance(transaction, Transaction):
            self.transactions.append(transaction)
        else:
            raise TypeError("Expected a Transaction instance")
        
    def get_limit(self):
        """
        Get the spending limit for this budget.

        :return: Spending limit
        """
        return self._limit

    def set_limit(self, new_limit):
        """
        Set a new spending limit for this budget.

        :param new_limit: New spending limit
        """
        if new_limit < 0:
            raise ValueError("Limit cannot be negative")
        self._limit = new_limit
        
    limit = property(get_limit, set_limit)

    def get_budget_percent(self):
        """
        Returns the percentage of the budget limit used.
        """
        return 100 * self.get_total_transaction_values() / self.limit

    def display_transactions(self):
        if not self.transactions:
            print("\nNo transactions in", self.category, end="\n")
            return
        print(f"{self.category} Transactions:")
        for transaction in self.transactions:
            print(transaction.__str__())

    def __str__(self):
        """
        String representation of the Budget instance.
        """
        spent = self.get_total_transaction_values()
        remaining = self.limit - spent
        return (f"{self.category}:\n"
                f"  Limit:     ${self.limit:.2f}\n"
                f"  Spent:     ${spent:.2f}\n"
                f"  Remaining: ${remaining:.2f}\n")
    