from budget_category import BudgetCategory
from budget_lockable import BudgetLockable
from user import User


class RebelUser(User, BudgetLockable):
    """User subclass for the Rebel."""
    BUDGET_LOCK_PERCENTAGE = 100
    BUDGET_APPROACHING_PERCENTAGE = 50

    def __init__(self, username, age, bank_account):
        super().__init__(username, age, bank_account)

    def is_budget_locked(self, budget_category):
        """Indicate if a particular budget is locked.

        :param budget_category: a BudgetCategory
        :return: a boolean indicating if the budget is locked
         """
        return (self.bank_account.get_budget_percent(budget_category) >
                RebelUser.BUDGET_LOCK_PERCENTAGE)

    def is_approaching_limit(self, budget_category):
        """Indicate if the user should receive a notification of approaching a budget limit.

        :param budget_category: a BudgetCategory
        :return: a boolean indicating if the user should receive a notification of approaching
            a budget limit.
        """
        return (self.bank_account.get_budget_percent(budget_category) >
                RebelUser.BUDGET_APPROACHING_PERCENTAGE)

    def notify_approaching_limit(self, budget_category):
        print(f"\nYou are over {RebelUser.BUDGET_APPROACHING_PERCENTAGE}% of your budget for "
              f"{budget_category}.\n")

    def exceed_limit(self, budget_category):
        print(f"\nYou are over budget for {budget_category}!!!\n")

    def is_user_locked(self):
        """Return a boolean indicating the user is locked if two or more budgets are locked."""
        locked_budgets = 0
        for category in BudgetCategory:
            if self.is_budget_locked(category):
                locked_budgets += 1
        return locked_budgets >= 2

    def add_transaction(self, transaction):
        """Add a transaction to the user's bank account.

        :param transaction: a Transaction to add to the user's bank account
        """
        if self.is_budget_locked(transaction.category):
            print(f"{transaction.category} is locked! You cannot add more transactions to this "
                  f"category.")
            return
        super().add_transaction(transaction)
        if self.is_budget_locked(transaction.category):
            print(f"\n{transaction.category} is now locked due to exceeding"
                  f"{RebelUser.BUDGET_LOCK_PERCENTAGE}% of your budget!")
        if self.is_user_locked():
            print("\nYou have exceeded your budget in multiple categories. Your account is now "
                  "locked. Goodbye.\n")

    def log_in(self):
        """Log in as the user.

        :return: a boolean indicating if login was successful
        """
        if self.is_user_locked():
            print(f"\n{self.username}'s account is LOCKED, they can not log in")
            return False
        return super().log_in()

    def get_user_label(self):
        """Return a string identifying the user."""
        locked_warning = " - LOCKED" if self.is_user_locked() else ""
        return f"{self.username} (Rebel){locked_warning}"

    def print_budgets_summary(self):
        for budget in BudgetCategory:
            locked = "[LOCKED] " if self.is_budget_locked(budget) else ""
            print(locked, self.bank_account.get_budget_summary(budget), sep="")
