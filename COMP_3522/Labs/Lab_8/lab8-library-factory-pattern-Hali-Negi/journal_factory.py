from item_factory import ItemFactory
from journal import Journal


class JournalFactory(ItemFactory):
    """
    Factory responsible for creating Journal objects.
    Prompts the user for journal details and returns a Journal.
    """

    def create_item(self):
        """
        Collects input from the user and creates a Journal object.
        """
        print("\n-- Add a Journal --")
        title = input("Title: ").strip()
        call_number = input("Call Number: ").strip()
        author = input("Author: ").strip()
        issue_number = input("Issue Number: ").strip()
        publisher = input("Publisher: ").strip()
        num_of_copies = int(input("Number of copies: ").strip())

        return Journal(title, call_number, author, issue_number, publisher, num_of_copies)