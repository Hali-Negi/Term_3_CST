class Transaction:
    """
    A transaction class representing a financial transaction.
    """

    def __init__(self, amount, timestamp, category, merchant=""):
        """
        Initialize a Transaction instance.
        
        :param amount: Money exchanged in transaction, can be positive or negative
        :param timestamp: Time of transaction
        :param category: Category of transaction as a BudgetCategory
        :param merchant: Merchant involved in transaction
        """
        self.amount = amount
        self.timestamp = timestamp
        self.category = category
        self.merchant = merchant

    def __str__(self):
        """
        String representation of the Transaction instance.
        """
        return (f"Transaction(amount={self.amount}, timestamp={self.get_formatted_time()}, "
                f"merchant={self.merchant}, category={self.category})")

    def get_formatted_time(self):
        """
        Return a formatted string representation of the transaction's timestamp.
        """
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    