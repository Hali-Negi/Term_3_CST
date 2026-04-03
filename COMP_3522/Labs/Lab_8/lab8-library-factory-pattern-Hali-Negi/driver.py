# from book import Book
# from library import Library
#
#
# def main():
#     """
#     Entry point for the program.
#     Creates a Library instance and tests the main functionality.
#     """
#     my_library = Library()
#
#     # Create a new item using the generator and add it to the catalogue
#     my_library.catalogue.add_item()
#
#     # Add sample books to the library
#     book1 = Book("The Catcher in the Rye", "C123", "J.D. Salinger", 3)
#     book2 = Book("To Kill a Mockingbird", "M456", "Harper Lee", 5)
#     my_library.add_book(book1)
#     my_library.add_book(book2)
#
#     # Display all items currently in the catalogue
#     my_library.display_available_books()
#
#     # Search for a title keyword
#     found_books = my_library.find_books("Mockingbird")
#
#     if found_books:
#         print("\nBooks found:")
#
#         for found_book in found_books:
#             print(found_book)
#
#     # Check out a book and display updated availability
#     my_library.check_out("C123")
#     my_library.display_available_books()
#
#     # Return the book and display updated availability
#     my_library.return_book("C123")
#     my_library.display_available_books()
#
#     # Remove a book and display the final list
#     my_library.remove_book("M456")
#     my_library.display_available_books()
#
#
# if __name__ == "__main__":
#     main()


from book import Book
from library import Library
from book_factory import BookFactory
from dvd_factory import DVDFactory
from journal_factory import JournalFactory


def main():
    """
    Entry point for the program.
    Tests the library system with the new factory pattern.
    """
    my_library = Library()

    # Use factories to create items
    print("Adding a book using BookFactory:")
    my_library.add_item_from_factory(BookFactory())

    print("Adding a DVD using DVDFactory:")
    my_library.add_item_from_factory(DVDFactory())

    print("Adding a Journal using JournalFactory:")
    my_library.add_item_from_factory(JournalFactory())

    # Display all items
    my_library.display_available_items()


if __name__ == "__main__":
    main()