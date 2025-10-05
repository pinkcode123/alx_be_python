class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Create a new bank account.
        initial_balance: optional starting balance (defaults to 0.0)
        """
        # Encapsulated attribute: we prefix with a single underscore to signal it's internal
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Add money to the account.
        Returns True if deposit succeeds, False for invalid amounts.
        """
        if amount <= 0:
            return False  # do not accept zero or negative deposits
        self._account_balance += amount
        return True

    def withdraw(self, amount):
        """
        Withdraw money if sufficient funds exist.
        Returns True on successful withdrawal, False if insufficient funds or invalid amount.
        """
        if amount <= 0:
            return False
        if amount > self._account_balance:
            return False
        self._account_balance -= amount
        return True

    def display_balance(self):
        """
        Print the current balance in a friendly format.
        """
        print(f"Current Balance: ${self._account_balance:.2f}")