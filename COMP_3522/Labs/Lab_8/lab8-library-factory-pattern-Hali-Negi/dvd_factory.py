from item_factory import ItemFactory
from dvd import DVD


class DVDFactory(ItemFactory):
    """
    Factory responsible for creating DVD objects.
    Prompts the user for DVD details and returns a DVD.
    """

    def create_item(self):
        """
        Collects input from the user and creates a DVD object.
        """
        print("\n-- Add a DVD --")
        title = input("Title: ").strip()
        call_number = input("Call Number: ").strip()
        release_date = input("Release Date: ").strip()
        region_code = input("Region Code: ").strip()
        num_of_copies = int(input("Number of copies: ").strip())

        return DVD(title, call_number, release_date, region_code, num_of_copies)