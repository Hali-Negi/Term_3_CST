from book import Book
from dvd import DVD
from journal import Journal


class LibraryItemGenerator:
    """
    Handles user interaction for creating new library items.

    Prompts the user to select an item type and gathers
    the required information to create that item.
    """

    def get_item_type(self) -> str:
        """
        Displays a menu of item types and returns
        the user's selection.
        """
        print("\nChoose an item type to add:")
        print("1) Book")
        print("2) DVD")
        print("3) Journal")

        return input("Enter 1, 2, or 3: ").strip()

    def create_item(self):
        """
        Creates and returns a library item based
        on the user's selection.
        """
        choice = self.get_item_type()

        if choice == "1":
            return self._create_book()

        elif choice == "2":
            return self._create_dvd()

        elif choice == "3":
            return self._create_journal()

        else:
            print("Invalid choice.")

            return None

    def _create_book(self):
        """
        Collects input from the user and creates a Book object.
        """
        title       = input("Title: ").strip()
        call_number = input("Call Number: ").strip()
        author      = input("Author: ").strip()
        num         = int(input("Number of copies: ").strip())

        return Book(title, call_number, author, num)

    def _create_dvd(self):
        """
        Collects input from the user and creates a DVD object.
        """
        title        = input("Title: ").strip()
        call_number  = input("Call Number: ").strip()
        release_date = input("Release Date: ").strip()
        region_code  = input("Region Code: ").strip()
        num          = int(input("Number of copies: ").strip())

        return DVD(title, call_number, release_date, region_code, num)

    def _create_journal(self):
        """
        Collects input from the user and creates a Journal object.
        """
        title        = input("Title: ").strip()
        call_number  = input("Call Number: ").strip()
        author       = input("Author: ").strip()
        issue_number = input("Issue Number: ").strip()
        publisher    = input("Publisher: ").strip()
        num          = int(input("Number of copies: ").strip())

        return Journal(title, call_number, author, issue_number, publisher, num)
