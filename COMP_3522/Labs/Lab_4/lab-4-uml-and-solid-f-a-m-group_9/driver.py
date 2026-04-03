# Bank Account example implementation
from bank_account import BankAccount
from transaction import Transaction


account = BankAccount("Example bank", "123456789", 1000.0)

transaction1 = Transaction(100.0, "2024-10-01", "Cloud 9")
transaction2 = Transaction(50.0, "2024-10-02", "Translink")
transaction3 = Transaction(200.0, "2024-10-03")

account.add_transaction("Grocery", transaction1)
account.add_transaction("Transport", transaction2)
account.add_transaction("Entertainment", transaction3)

print(account)