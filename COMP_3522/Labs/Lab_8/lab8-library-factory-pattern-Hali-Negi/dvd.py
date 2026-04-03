# from library_item import LibraryItem
#
#
# class DVD(LibraryItem):
#     """
#     Represents a DVD in the library.
#
#     A DVD has a title, call number, release date,
#     region code, and a number of available copies.
#     """
#
#     def __init__(self, title, call_number, release_date, region_code, num_of_copies):
#         """
#         Initializes a DVD object with its details.
#         """
#         self.title        = title
#         self.call_number  = call_number
#         self.release_date = release_date
#         self.region_code  = region_code
#         self.num_of_copies = num_of_copies
#
#     def check_availability(self) -> bool:
#         """
#         Returns True if at least one copy of the DVD
#         is available for checkout.
#         """
#         return self.num_of_copies > 0
#
#     def __str__(self) -> str:
#         """
#         Returns a formatted string containing the
#         details of the DVD.
#         """
#         return (
#             f"Title:            {self.title}\n"
#             f"Call Number:      {self.call_number}\n"
#             f"Release Date:     {self.release_date}\n"
#             f"Region Code:      {self.region_code}\n"
#             f"Available Copies: {self.num_of_copies}"
#         )

# Remove repetition — before, DVD.__init__ was manually setting self.title,
# self.call_number, and self.num_of_copies itself. Now super().__init__() handles
# those 3 lines, so DVD only sets what's unique to it (release_date and region_code).

#  Remove check_availability — it was identical in Book, DVD, and Journal. Now it
# lives once in the parent class and all subclasses inherit it automatically.

from library_item import LibraryItem


class DVD(LibraryItem):
    """
    Represents a DVD in the library.
    """

    def __init__(self, title, call_number, release_date, region_code, num_of_copies):
        super().__init__(title, call_number, num_of_copies)
        self.release_date = release_date
        self.region_code = region_code

    def __str__(self):
        return (
            f"Title:            {self.title}\n"
            f"Call Number:      {self.call_number}\n"
            f"Release Date:     {self.release_date}\n"
            f"Region Code:      {self.region_code}\n"
            f"Available Copies: {self.num_of_copies}"
        )