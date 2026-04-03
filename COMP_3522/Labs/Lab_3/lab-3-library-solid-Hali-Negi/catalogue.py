"""

Stores and manages all library items.
Handles searching, adding, removing, checking out, returning,
and displaying items in the catalogue.
"""

import difflib                          # Used for close title matching
from library_item_generator import LibraryItemGenerator


class Catalogue:
    """
    Maintains a single list of library items.
    """

    def __init__(self):
        """
        Constructor.
        Creates an empty list to store library items.
        """
        self.book_list = []   # Stores Book, DVD, and Journal objects

    def find_books(self, string):
        """
        Searches for items where the title contains the given string.
        If nothing is found, prints close matches using difflib.
        Returns a list of matching items.
        """
        found_books = []
        for book in self.book_list:

            if string.lower() in book.title.lower():
                found_books.append(book)

        if not found_books:
            similar_titles = difflib.get_close_matches(
                string, [book.title for book in self.book_list]
            )

            if similar_titles:
                print(f"Book not found. Did you mean one of these titles? {', '.join(similar_titles)}")

            else:
                print("Book not found.")

        return found_books

    def add_book(self, book):
        """
        Adds a book object to the catalogue list if it does not already exist.
        """
        if book not in self.book_list:
            self.book_list.append(book)

    def add_item(self):
        """
        Uses LibraryItemGenerator to create a new item (Book, DVD, or Journal),
        then adds it to the catalogue list.
        """
        generator = LibraryItemGenerator()
        item = generator.create_item()

        if item is None:

            return

        self.book_list.append(item)
        print("Item added to catalogue.")

    def remove_book(self, call_number):
        """
        Removes the item with the matching call number from the catalogue.
        """
        for book in self.book_list:

            if book.call_number == call_number:
                self.book_list.remove(book)
                print(f"Book with call number {call_number} removed.")

                return
        print(f"Book with call number {call_number} not found.")

    def check_out(self, call_number):
        """
        Attempts to check out an item by call number.
        If available, decrements the number of copies.
        """
        for book in self.book_list:

            if book.call_number == call_number:
                if book.check_availability():
                    book.num_of_copies -= 1
                    print(f"Book with call number {call_number} checked out successfully.")

                    return

                else:
                    print(f"Book with call number {call_number} is not available for check out.")

                    return
        print(f"Book with call number {call_number} not found.")

    def return_book(self, call_number):
        """
        Returns an item by call number by incrementing its copy count.
        """
        for book in self.book_list:

            if book.call_number == call_number:
                book.num_of_copies += 1
                print(f"Book with call number {call_number} returned successfully.")

                return

        print(f"Book with call number {call_number} not found.")

    def display_available_books(self):
        """
        Prints all items currently stored in the catalogue.
        """
        if not self.book_list:
            print("No books available.")

        else:
            for book in self.book_list:
                print("\n" + str(book))
