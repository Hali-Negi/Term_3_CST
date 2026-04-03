from datetime import datetime
from user_generator import UserGenerator
from budget_category import BudgetCategory
from rebel_user import RebelUser
from transaction import Transaction


class FAM:

    def __init__(self):
        self.users = []
        self.current_user = None

    def load_test_users(self):
        """Load hardcoded users for testing purposes."""
        user1 = UserGenerator.generate_user(
            name="Mickey",
            age=15,
            user_type="angel",
            bank_name="TD",
            account_number="1111",
            balance=500,
            budgets={
                BudgetCategory.GAMES_AND_ENTERTAINMENT: 100,
                BudgetCategory.CLOTHING_AND_ACCESSORIES: 100,
                BudgetCategory.EATING_OUT: 100,
                BudgetCategory.MISCELLANEOUS: 100
            }
        )

        user2 = UserGenerator.generate_user(
            name="Garfield",
            age=16,
            user_type="troublemaker",
            bank_name="RBC",
            account_number="2222",
            balance=400,
            budgets={
                BudgetCategory.GAMES_AND_ENTERTAINMENT: 100,
                BudgetCategory.CLOTHING_AND_ACCESSORIES: 100,
                BudgetCategory.EATING_OUT: 100,
                BudgetCategory.MISCELLANEOUS: 100
            }
        )

        user3 = UserGenerator.generate_user(
            name="Snoopy",
            age=17,
            user_type="rebel",
            bank_name="BMO",
            account_number="3333",
            balance=300,
            budgets={
                BudgetCategory.GAMES_AND_ENTERTAINMENT: 100,
                BudgetCategory.CLOTHING_AND_ACCESSORIES: 100,
                BudgetCategory.EATING_OUT: 100,
                BudgetCategory.MISCELLANEOUS: 100
            }
        )

        self.users.append(user1)
        self.users.append(user2)
        self.users.append(user3)

    def main_menu(self):
        """
        The main menu loop. Runs when the program starts.
        Options: Register new user, Login, or Exit.
        """
        # Load test users once at startup
        self.load_test_users()

        while True:
            print("\n****** Welcome to the FAM! ******")
            print("Select from the options below:\n")
            print("1. Register new user")
            print("2. Login existing user")
            print("3. Exit program")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.register_user()
            elif choice == "2":
                if len(self.users) == 0:
                    print("No users registered yet. Please register a user first.")
                else:
                    self.login_user()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def register_user(self):
        """
        Prompts the user to enter details for a new user
        and uses UserGenerator to create them.
        """
        print("\n--- Registering a new user ---\n")

        name = input("Enter the user's name: ").strip()
        age = int(input("Enter the user's age: ").strip())

        print("\nSelect user type:")
        print("1. Angel")
        print("2. Troublemaker")
        print("3. Rebel")
        user_type_choice = input("Enter choice (1/2/3): ").strip()

        user_type_map = {"1": "angel", "2": "troublemaker", "3": "rebel"}
        user_type = user_type_map.get(user_type_choice)
        if user_type is None:
            print("Invalid user type. Returning to main menu.")
            return

        bank_name = input("\nEnter bank name: ").strip()
        account_number = input("Enter account number: ").strip()
        balance = float(input("Enter starting balance: $").strip())

        print("\nEnter budget limits for each category:")
        budgets = {}

        for category in BudgetCategory:
            amount = float(input(f"  {category} budget: $").strip())
            budgets[category] = amount

        new_user = UserGenerator.generate_user(
            name, age, user_type, bank_name, account_number, balance, budgets
        )
        self.users.append(new_user)
        print(f"\n✓ User '{name}' has been registered successfully!")

    def login_user(self):
        """
        Displays list of registered users and lets
        the user select one to log in as.
        """
        print("\n--- Select user to log in as ---\n")

        for i, user in enumerate(self.users, 1):
            print(f"{i}. {user.get_user_label()}")

        choice = input("\nChoose a user to log in as: ").strip()

        try:
            index = int(choice) - 1
            if index < 0 or index >= len(self.users):
                print("Invalid selection.")
                return

            selected_user = self.users[index]

            login_success = selected_user.log_in()
            if not login_success:
                return

            self.current_user = selected_user
            self.user_menu()

        except ValueError:
            print("Invalid input. Please enter a number.")

    def user_menu(self):
        """
        The user menu that appears after logging in.
        Options: View Budgets, Record Transaction,
        View Transactions by Budget, View Bank Account Details, Logout.
        """
        while True:
            print("\n****** User Menu ******\n")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("5. Logout")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.display_budgets()
            elif choice == "2":
                self.record_transaction()
                if isinstance(self.current_user, RebelUser):
                    if self.current_user.is_user_locked():
                        break
            elif choice == "3":
                self.view_transactions_by_budget()
            elif choice == "4":
                print(self.current_user.get_bank_account_details())
            elif choice == "5":
                self.current_user = None
                print("Logged out.")
                break
            else:
                print("Invalid option. Please try again.")

    def display_budgets(self):
        """
        Displays all budgets for the current user
        with their status (locked or not), amount spent, amount left, and limit.
        """
        print("\n--- Budget Overview ---\n")
        self.current_user.print_budgets_summary()

    def record_transaction(self):
        """
        Sub-menu to record a new transaction.
        Prompts for amount, category, and merchant.
        """
        print("\n--- Record a Transaction ---\n")

        amount = float(input("Enter transaction amount: $").strip())
        if amount <= 0:
            print("Amount must be a positive number.")
            return

        merchant = input("Enter merchant name: ").strip()

        selected_budget = FAM._select_category()

        transaction = Transaction(amount, datetime.now(), selected_budget, merchant)

        self.current_user.add_transaction(transaction)

    def view_transactions_by_budget(self):
        """
        Sub-menu to select a budget category and view
        all transactions in that category.
        """
        print("\n--- View Transactions by Budget ---\n")

        selected_category = FAM._select_category()
        self.current_user.display_budget_transactions(selected_category)
        print("")

    @staticmethod
    def _select_category():
        """Get a category selection from the user.

        :return: the selected category as a BudgetCategory
        """
        categories = list(BudgetCategory)
        print("Select a budget category:")
        for i, budget in enumerate(categories, 1):
            print(f"  {i}. {budget}")

        cat_choice = input("\nEnter category number: ").strip()
        try:
            cat_index = int(cat_choice) - 1
            if cat_index < 0 or cat_index >= len(categories):
                print("Invalid category.")
                return
        except ValueError:
            print("Invalid input.")
            return

        return categories[cat_index]


def main():
    fam = FAM()
    fam.main_menu()


if __name__ == "__main__":
    main()
