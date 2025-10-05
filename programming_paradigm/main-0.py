# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Set up an example account with a starting balance of $100
    account = BankAccount(100.0)

    # If no arguments are given, show usage
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        print("Examples:")
        print("  python main-0.py deposit:50")
        print("  python main-0.py withdraw:20")
        print("  python main-0.py display")
        sys.exit(1)

    # Parse the first argument, support "command" or "command:amount"
    command_part = sys.argv[1]
    parts = command_part.split(':', 1)
    command = parts[0].strip().lower()
    amount = None
    if len(parts) == 2 and parts[1] != '':
        try:
            amount = float(parts[1])
        except ValueError:
            print("Invalid amount. Please provide a numeric value.")
            sys.exit(1)

    # Execute command
    if command == "deposit":
        if amount is None:
            print("Please provide an amount to deposit, e.g. deposit:50")
            sys.exit(1)
        if account.deposit(amount):
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit failed. Amount must be greater than 0.")

    elif command == "withdraw":
        if amount is None:
            print("Please provide an amount to withdraw, e.g. withdraw:20")
            sys.exit(1)
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command. Available commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()