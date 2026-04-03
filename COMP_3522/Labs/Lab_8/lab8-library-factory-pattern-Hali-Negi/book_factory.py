from item_factory import ItemFactory
from book import Book


class BookFactory(ItemFactory):
    """
    Factory responsible for creating Book objects.
    Prompts the user for book details and returns a Book.
    """

    def create_item(self):
        """
        Collects input from the user and creates a Book object.
        """
        print("\n-- Add a Book --")
        title = input("Title: ").strip()
        call_number = input("Call Number: ").strip()
        author = input("Author: ").strip()
        num_of_copies = int(input("Number of copies: ").strip())

        return Book(title, call_number, author, num_of_copies)