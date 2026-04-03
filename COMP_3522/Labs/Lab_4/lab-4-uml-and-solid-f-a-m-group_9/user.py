"""Base class representing a FAM user."""
import abc

from budget_category import BudgetCategory


class User(abc.ABC):
    """A FAM user."""

    def __init__(self, username, age, bank_account):
        """Set up basic user attributes.

        :param username: the user's name as a string
        :param age: the user's age as an integer
        :param bank_account: the user's BankAccount
        """
        self._username = username
        self._age = age
        self.bank_account = bank_account

    def get_username(self):
        """Get the user's name.

        :return: the user's name as a string
        """
        return self._username

    username = property(get_username)

    def get_age(self):
        """Get the user's age.

        :return: the user's age as an int
        """
        return self._age

    age = property(get_age)

    def log_in(self):
        """Log in as the user.

        :return: a boolean indicating if login was successful
        """
        print(f"\nLogged in as {self.get_user_label()}\n")
        return True

    @abc.abstractmethod
    def get_user_label(self):
        """Return a string identifying the user."""
        ...

    @abc.abstractmethod
    def is_approaching_limit(self, budget_category):
        """Indicate if the user should receive a notification of approaching a budget limit.

        :param budget_category: a BudgetCategory
        :return: a boolean indicating if the user should receive a notification of approaching
            a budget limit.
        """
        ...

    def is_over_limit(self, budget_category):
        """Indicate if the user should receive a notification of exceeding a budget limit.

        :param budget_category: a BudgetCategory
        :return: a boolean indicating if the user should receive a notification of exceeding
            a budget limit.
        """
        return self.bank_account.get_budget_percent(budget_category) > 100

    def print_budgets_summary(self):
        for budget in BudgetCategory:
            print(self.bank_account.get_budget_summary(budget))

    def display_budget_transactions(self, budget_category):
        self.bank_account.display_budget_transactions(budget_category)

    def get_bank_account_details(self):
        return self.bank_account.__str__()

    def add_transaction(self, transaction):
        """Add a transaction to the user's bank account.

        :param transaction: a Transaction to add to the user's bank account
        """
        self.bank_account.add_transaction(transaction)
        over_limit = self.is_over_limit(transaction.category)
        approaching_limit = self.is_approaching_limit(transaction.category)
        if over_limit or approaching_limit:
            if over_limit:
                self.exceed_limit(transaction.category)
            elif approaching_limit:
                self.notify_approaching_limit(transaction.category)
            self.bank_account.display_budget_transactions(transaction.category)

    def exceed_limit(self, budget_category):
        print(f"\nPlease note that you have exceeded your budget for {budget_category}.\n")

    @abc.abstractmethod
    def notify_approaching_limit(self, budget_category):
        ...
