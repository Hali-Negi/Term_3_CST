# """
#
# Stores and manages all library items.
# Handles searching, adding, removing, checking out, returning,
# and displaying items in the catalogue.
# """
#
# import difflib                          # Used for close title matching
# from library_item_generator import LibraryItemGenerator
#
#
# class Catalogue:
#     """
#     Maintains a single list of library items.
#     """
#
#     def __init__(self):
#         """
#         Constructor.
#         Creates an empty list to store library items.
#         """
#         self.book_list = []   # Stores Book, DVD, and Journal objects
#
#     def find_books(self, string):
#         """
#         Searches for items where the title contains the given string.
#         If nothing is found, prints close matches using difflib.
#         Returns a list of matching items.
#         """
#         found_books = []
#         for book in self.book_list:
#
#             if string.lower() in book.title.lower():
#                 found_books.append(book)
#
#         if not found_books:
#             similar_titles = difflib.get_close_matches(
#                 string, [book.title for book in self.book_list]
#             )
#
#             if similar_titles:
#                 print(f"Book not found. Did you mean one of these titles? {', '.join(similar_titles)}")
#
#             else:
#                 print("Book not found.")
#
#         return found_books
#
#     def add_book(self, book):
#         """
#         Adds a book object to the catalogue list if it does not already exist.
#         """
#         if book not in self.book_list:
#             self.book_list.append(book)
#
#     def add_item(self):
#         """
#         Uses LibraryItemGenerator to create a new item (Book, DVD, or Journal),
#         then adds it to the catalogue list.
#         """
#         generator = LibraryItemGenerator()
#         item = generator.create_item()
#
#         if item is None:
#
#             return
#
#         self.book_list.append(item)
#         print("Item added to catalogue.")
#
#     def remove_book(self, call_number):
#         """
#         Removes the item with the matching call number from the catalogue.
#         """
#         for book in self.book_list:
#
#             if book.call_number == call_number:
#                 self.book_list.remove(book)
#                 print(f"Book with call number {call_number} removed.")
#
#                 return
#         print(f"Book with call number {call_number} not found.")
#
#     def check_out(self, call_number):
#         """
#         Attempts to check out an item by call number.
#         If available, decrements the number of copies.
#         """
#         for book in self.book_list:
#
#             if book.call_number == call_number:
#                 if book.check_availability():
#                     book.num_of_copies -= 1
#                     print(f"Book with call number {call_number} checked out successfully.")
#
#                     return
#
#                 else:
#                     print(f"Book with call number {call_number} is not available for check out.")
#
#                     return
#         print(f"Book with call number {call_number} not found.")
#
#     def return_book(self, call_number):
#         """
#         Returns an item by call number by incrementing its copy count.
#         """
#         for book in self.book_list:
#
#             if book.call_number == call_number:
#                 book.num_of_copies += 1
#                 print(f"Book with call number {call_number} returned successfully.")
#
#                 return
#
#         print(f"Book with call number {call_number} not found.")
#
#     def display_available_books(self):
#         """
#         Prints all items currently stored in the catalogue.
#         """
#         if not self.book_list:
#             print("No books available.")
#
#         else:
#             for book in self.book_list:
#                 print("\n" + str(book))

# book_list → item_list
# find_books uses a comprehension now
# All method names updated to item instead of book

import difflib

class Catalogue:
    """
    Maintains a list of all library items.
    """

    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        if item not in self.item_list:
            self.item_list.append(item)

    def find_items(self, string):
        """
        Searches for items where the title contains the given string.
        """
        found_items = [item for item in self.item_list
                       if string.lower() in item.title.lower()]

        if not found_items:
            similar_titles = difflib.get_close_matches(
                string, [item.title for item in self.item_list]
            )
            if similar_titles:
                print(f"Not found. Did you mean: {', '.join(similar_titles)}?")
            else:
                print("Item not found.")

        return found_items

# add a new method called add_item_from_factory that takes a
# factory and uses it to create and add an item
    def add_item_from_factory(self, factory):
        """
        Uses the provided factory to create a new item
        and adds it to the catalogue.
        """
        item = factory.create_item()
        self.item_list.append(item)
        print("Item added to catalogue.")

    def remove_item(self, call_number):
        """
        Removes an item by call number.
        """
        for item in self.item_list:
            if item.call_number == call_number:
                self.item_list.remove(item)
                print(f"Item {call_number} removed.")
                return
        print(f"Item {call_number} not found.")

    def check_out(self, call_number):
        """
        Checks out an item by call number.
        """
        for item in self.item_list:
            if item.call_number == call_number:
                if item.check_availability():
                    item.num_of_copies -= 1
                    print(f"Item {call_number} checked out successfully.")
                else:
                    print(f"Item {call_number} is not available.")
                return
        print(f"Item {call_number} not found.")

    def return_item(self, call_number):
        """
        Returns an item by call number.
        """
        for item in self.item_list:
            if item.call_number == call_number:
                item.num_of_copies += 1
                print(f"Item {call_number} returned successfully.")
                return
        print(f"Item {call_number} not found.")

    def display_available_items(self):
        """
        Displays all items in the catalogue.
        """
        if not self.item_list:
            print("No items available.")
        else:
            for item in self.item_list:
                print("\n" + str(item))