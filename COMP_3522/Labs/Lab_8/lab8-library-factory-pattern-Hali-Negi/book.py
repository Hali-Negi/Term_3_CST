# from library_item import LibraryItem
#
#
# class Book(LibraryItem):
#     """
#     Represents a book in the library.
#     """
#
#     def __init__(self, title, call_number, author, num_of_copies):
#         """
#         Initializes a Book object with its details.
#         """
#         self.title         = title
#         self.call_number   = call_number
#         self.author        = author
#         self.num_of_copies = num_of_copies
#
#     def check_availability(self):
#         """
#         Returns True if at least one copy of the book
#         is available for checkout.
#         """
#         return self.num_of_copies > 0
#
#     def __str__(self):
#         """
#         Returns a formatted string containing the
#         details of the book.
#         """
#         return (
#             f"Title:            {self.title}\n"
#             f"Call Number:      {self.call_number}\n"
#             f"Author:           {self.author}\n"
#             f"Available Copies: {self.num_of_copies}"
#         )


#No more repeated self.title, self.call_number, self.num_of_copies
#super().__init__() handles those now
# check_availability is gone — inherited from base class

from library_item import LibraryItem


class Book(LibraryItem):
    """
    Represents a book in the library.
    """

    def __init__(self, title, call_number, author, num_of_copies):
        super().__init__(title, call_number, num_of_copies)
        self.author = author

    def __str__(self):
        return (
            f"Title:            {self.title}\n"
            f"Call Number:      {self.call_number}\n"
            f"Author:           {self.author}\n"
            f"Available Copies: {self.num_of_copies}"
        )