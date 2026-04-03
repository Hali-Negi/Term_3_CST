import abc


class BudgetLockable(abc.ABC):
    """Mix-in for users who can have budgets locked."""

    @abc.abstractmethod
    def is_budget_locked(self, budget_category):
        """Indicate if a particular budget is locked.

        :param budget_category: a BudgetCategory
        :return: a boolean indicating if the budget is locked
         """
        ...
