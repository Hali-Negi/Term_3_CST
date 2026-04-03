from abc import ABC, abstractmethod


class ItemFactory(ABC):
    """
    Abstract base factory for creating library items.
    Each subclass is responsible for creating one type of item.
    """

    @abstractmethod
    def create_item(self):
        """
        Creates and returns a library item.
        """
        pass