from library_item import LibraryItem


class Journal(LibraryItem):
    """
    Represents a scientific journal in the library.

    A Journal has a title, call number, author,
    issue number, publisher, and a number of
    available copies.
    """

    def __init__(self, title, call_number, author, issue_number, publisher, num_of_copies):
        """
        Initializes a Journal object with its details.
        """
        self.title         = title
        self.call_number   = call_number
        self.author        = author
        self.issue_number  = issue_number
        self.publisher     = publisher
        self.num_of_copies = num_of_copies

    def check_availability(self) -> bool:
        """
        Returns True if at least one copy of the journal
        is available for checkout.
        """
        return self.num_of_copies > 0

    def __str__(self) -> str:
        """
        Returns a formatted string containing the
        details of the journal.
        """
        return (
            f"Title:            {self.title}\n"
            f"Call Number:      {self.call_number}\n"
            f"Author:           {self.author}\n"
            f"Issue Number:     {self.issue_number}\n"
            f"Publisher:        {self.publisher}\n"
            f"Available Copies: {self.num_of_copies}"
        )
