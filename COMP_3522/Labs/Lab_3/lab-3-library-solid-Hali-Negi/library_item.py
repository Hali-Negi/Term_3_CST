from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """
    Abstract base class for all library items.

    This class defines the common behaviour that all library
    items (Book, DVD, Journal) must implement.
    """

    @abstractmethod
    def check_availability(self) -> bool:
        """
        Returns True if at least one copy of the item is available.
        Returns False otherwise.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a formatted string containing the
        details of the library item.
        """
        pass
