from user import User


class AngelUser(User):
    """User subclass for the Angel."""
    BUDGET_APPROACHING_PERCENTAGE = 90

    def __init__(self, username, age, bank_account):
        super().__init__(username, age, bank_account)

    def is_approaching_limit(self, budget_category):
        """Indicate if the user should receive a notification of approaching a budget limit.

        :param budget_category: a BudgetCategory
        :return: a boolean indicating if the user should receive a notification of approaching
            a budget limit.
        """
        return (self.bank_account.get_budget_percent(budget_category) >
                AngelUser.BUDGET_APPROACHING_PERCENTAGE)

    def notify_approaching_limit(self, budget_category):
        print(f"\nYou are over {AngelUser.BUDGET_APPROACHING_PERCENTAGE}% of your budget for "
              f"{budget_category}.\n")

    def get_user_label(self):
        """Return a string identifying the user."""
        return f"{self.username} (Angel)"
