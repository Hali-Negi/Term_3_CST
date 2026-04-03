from angel_user import AngelUser
from bank_account import BankAccount
from budget_category import BudgetCategory
from rebel_user import RebelUser
from troublemaker_user import TroublemakerUser


class UserGenerator:

    @staticmethod
    def generate_user(
            name: str,
            age: int,
            user_type: str,
            bank_name: str,
            account_number: str,
            balance: float,
            budgets: dict[BudgetCategory, float]
    ):
        """
        Generates a User based on the provided details.
        """
        try:
            # Create bank account
            bank_account = BankAccount(bank_name, account_number, budgets, balance)
        except ValueError as e:
            print(e)
            return

        user_types = {
            "angel": AngelUser,
            "troublemaker": TroublemakerUser,
            "rebel": RebelUser
        }

        user_class = user_types.get(user_type.lower())
        if user_class is None:
            raise ValueError("Invalid user type. Choose angel, troublemaker, or rebel.")

        return user_class(name, age, bank_account)
