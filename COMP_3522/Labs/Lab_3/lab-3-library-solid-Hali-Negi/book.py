from library_item import LibraryItem


class Book(LibraryItem):
    """
    Represents a book in the library.

    A Book has a title, call number, author, and a number
    of available copies.
    """

    def __init__(self, title, call_number, author, num_of_copies):
        """
        Initializes a Book object with its details.
        """
        self.title         = title
        self.call_number   = call_number
        self.author        = author
        self.num_of_copies = num_of_copies

    def check_availability(self):
        """
        Returns True if at least one copy of the book
        is available for checkout.
        """
        return self.num_of_copies > 0

    def __str__(self):
        """
        Returns a formatted string containing the
        details of the book.
        """
        return (
            f"Title:            {self.title}\n"
            f"Call Number:      {self.call_number}\n"
            f"Author:           {self.author}\n"
            f"Available Copies: {self.num_of_copies}"
        )
