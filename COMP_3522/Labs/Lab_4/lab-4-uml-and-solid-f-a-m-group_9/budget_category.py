"""An enum for budget categories."""
from enum import StrEnum, auto


class BudgetCategory(StrEnum):
    """Required budget categories."""
    GAMES_AND_ENTERTAINMENT = "Games and Entertainment"
    CLOTHING_AND_ACCESSORIES = "Clothing and Accessories"
    EATING_OUT = "Eating Out"
    MISCELLANEOUS = "Miscellaneous"
