from catalogue import Catalogue


class Library:
    """
    Represents the library system.

    The Library class acts as a controller that delegates
    all catalogue-related operations to the Catalogue class.
    """

    def __init__(self):
        """
        Initializes the Library with a Catalogue instance.
        """
        self.catalogue = Catalogue()

    def find_books(self, string):
        """
        Searches for items by title.
        Delegates the search to the Catalogue.
        """
        return self.catalogue.find_books(string)

    def add_book(self, book):
        """
        Adds a book to the catalogue.
        """
        self.catalogue.add_book(book)

    def add_item(self):
        """
        Creates a new library item using the generator
        and adds it to the catalogue.
        """
        self.catalogue.add_item()

    def remove_book(self, call_number):
        """
        Removes an item from the catalogue by call number.
        """
        self.catalogue.remove_book(call_number)

    def check_out(self, call_number):
        """
        Attempts to check out an item by call number.
        """
        self.catalogue.check_out(call_number)

    def return_book(self, call_number):
        """
        Returns an item to the catalogue by call number.
        """
        self.catalogue.return_book(call_number)

    def display_available_books(self):
        """
        Displays all items currently in the catalogue.
        """
        self.catalogue.display_available_books()
