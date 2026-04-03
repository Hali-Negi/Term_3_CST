from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """
    Abstract base class for all library items.
    Holds common attributes shared by all items.
    """

    def __init__(self, title, call_number, num_of_copies):
        self.title = title
        self.call_number = call_number
        self.num_of_copies = num_of_copies

    def check_availability(self) -> bool:
        return self.num_of_copies > 0

    @abstractmethod
    def __str__(self) -> str:
        pass