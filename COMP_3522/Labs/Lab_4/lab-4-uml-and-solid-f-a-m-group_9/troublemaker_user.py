from budget_category import BudgetCategory
from budget_lockable import BudgetLockable
from user import User


class TroublemakerUser(User, BudgetLockable):
    """User subclass for the Troublemaker."""

    # TODO Check with Nabil if he means lock at 120% of the limit or limit + 120%
    BUDGET_LOCK_PERCENTAGE = 120
    BUDGET_APPROACHING_PERCENTAGE = 75

    def __init__(self, username, age, bank_account):
        super().__init__(username, age, bank_account)

    def is_budget_locked(self, budget_category):
        """Indicate if a particular budget is locked.

        :param budget_category: a BudgetCategory
        :return: a boolean indicating if the budget is locked
         """
        return (self.bank_account.get_budget_percent(budget_category) >
                TroublemakerUser.BUDGET_LOCK_PERCENTAGE)

    def is_approaching_limit(self, budget_category):
        """Indicate if the user should receive a notification of approaching a budget limit.

        :param budget_category: a BudgetCategory
        :return: a boolean indicating if the user should receive a notification of approaching
            a budget limit.
        """
        return (self.bank_account.get_budget_percent(budget_category) >
                TroublemakerUser.BUDGET_APPROACHING_PERCENTAGE)

    def notify_approaching_limit(self, budget_category):
        print(f"\nYou are over {TroublemakerUser.BUDGET_APPROACHING_PERCENTAGE}% of your budget "
              f"for {budget_category}.\n")

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
            print(f"\n{transaction.category} is now locked due to exceeding "
                  f"{TroublemakerUser.BUDGET_LOCK_PERCENTAGE}% of your budget!")

    def get_user_label(self):
        """Return a string identifying the user."""
        return f"{self.username} (Troublemaker)"

    def print_budgets_summary(self):
        for budget in BudgetCategory:
            locked = "[LOCKED] " if self.is_budget_locked(budget) else ""
            print(locked, self.bank_account.get_budget_summary(budget), sep="")

    def is_user_locked(self): # TODO Please add the locking logic for this - AJ
        """Return a boolean indicating the user is locked if two or more budgets are locked."""
        return False

    def log_in(self):
        """Log in as the user.

        :return: a boolean indicating if login was successful
        """
        if self.is_user_locked():
            print(f"{self.username}'s account is LOCKED, they can not log in")
            return False
        return super().log_in()
    