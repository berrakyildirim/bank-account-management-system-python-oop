import datetime
from typing import Union, List
from collections import defaultdict

id = 20250001  # Global ID counter for assigning unique account IDs

class AccountError(Exception):
    pass

class WithdrawError(Exception):
    pass

class DepositError(Exception):
    pass

class TransactionError(Exception):
    pass

class Transaction:
    def __init__( self, amount: int, currency: str='TRY' ):
        self.datetime = datetime.datetime.now()  # Record the date and time of the transaction
        self.amount = amount                     
        self.currency = currency                 

        if amount < 0:
            raise TransactionError               # Raise an error if the amount is negative

    @staticmethod
    def check_type( transaction_type: Union["Withdrawal", "Deposit"] ):
        # Static method to validate the type of transaction
        if transaction_type != "Withdrawal" and transaction_type != "Deposit":
            raise TransactionError               # Raise an error if type is not valid

# Subclass representing a deposit transaction
class Deposit(Transaction):
    def __init__( self, amount: int, currency: str='TRY' ):
        super().__init__(amount, currency)       # Call the constructor of the base Transaction class

# Subclass representing a withdrawal transaction
class Withdrawal(Transaction):
    def __init__( self, amount: int, currency: str='TRY' ):
        super().__init__(amount, currency)       # Call the constructor of the base Transaction class

# Class representing a bank account
class BankAccount:
    def __init__( self, name: str, account_id: int, currency: str='TRY' ):
        self.name = name                               
        self.account_id = account_id                   
        self.balance = 0                              
        self.currency = currency                       
        self.transactions: List[Transaction] = []      

    # Method to withdraw money from the account
    def withdraw( self, amount: int ):
        if amount < 0:
            raise WithdrawError                        # Raise error for negative amount
        elif amount > self.balance:
            raise WithdrawError                        # Raise error if insufficient balance
        self.balance -= amount                         # Deduct amount from balance
        self.transactions.append(Withdrawal(amount))   # Record the withdrawal transaction

    # Method to deposit money into the account
    def deposit( self, amount: int ):
        if amount < 0:
            raise WithdrawError                        # Raise error for negative amount
        self.balance += amount                         # Add amount to balance
        self.transactions.append(Deposit(amount))      # Record the deposit transaction

    # Method to count transactions by type
    def n_transactions( self, t_type: Withdrawal | Deposit | None=None, is_verbose: bool=True ) -> int:
        count = 0
        if t_type is None:
            return len(self.transactions)              # Return total number of transactions
        
        elif t_type is Deposit:
            for index in self.transactions:
                if isinstance(index, Deposit):         # Count only deposit transactions
                    count += 1
            return count

        elif t_type is Withdrawal:
            for index in self.transactions:
                if isinstance(index, Withdrawal):      # Count only withdrawal transactions
                    count += 1
            return count

# Manager class for handling multiple bank accounts
class BankAccountManager:
    def __init__(self):
        self.accounts = defaultdict(dict)  # Dictionary of a dictionary
        
        """
        Example structure of self.accounts:
        {
            "Berrak": {
                "TRY": BankAccount object,
                "USD": BankAccount object
            },
            "Selim": {
                "EUR": BankAccount object
            }
        }
        """

    # Opens a new account if one does not already exist with the same name and currency
    def open_account(self, name: str, currency: str = 'TRY') -> 'BankAccount':
        try:
            self.check_account(name, currency)  # Try to find an existing account
        
        # If account does not exist, create a new one
        except AccountError:
            global id
            new_account = BankAccount(name, id, currency)        # Create a new BankAccount object
            self.accounts[name][currency] = new_account          # Store it in the accounts dictionary
            id += 1                                              # Increment the global ID
            return new_account

    # Checks if an account exists and returns it; raises AccountError if not found
    def check_account(self, name: str, currency: str) -> 'BankAccount':
        currency_dict = self.accounts.get(name)                  # Get the dictionary for the person
        if currency_dict:
            account = currency_dict.get(currency)                # Check if the currency-specific account exists
            if account is not None:
                return account
        raise AccountError                                       # Raise error if account not found

    # Returns an existing account object; raises error if not found
    def get_account(self, name: str, currency: str = 'TRY') -> 'BankAccount':
        account = self.check_account(name, currency)             # Use check_account for validation
        if account is not None:
            return account
        raise AccountError

    # Transfers money from one account to another (same currency)
    def transfer(self, from_name: str, to_name: str, amount: int, currency: str = 'TRY'):
        try:
            from_account = self.check_account(from_name, currency)
            to_account = self.check_account(to_name, currency)
            from_account.withdraw(amount)                        # Withdraw from sender
            to_account.deposit(amount)                           # Deposit to receiver
            
        # If either account is not found
        except AccountError:
            print("No account found!")

    # Withdraws money from the specified user's account
    def withdraw(self, name: str, amount: int, currency: str):
        account = self.check_account(name, currency)
        account.withdraw(amount)

    # Deposits money into the specified user's account
    def deposit(self, name: str, amount: int, currency: str):
        account = self.check_account(name, currency)
        account.deposit(amount)

    # Returns the balance of the specified user's account
    def balance(self, name: str, currency: str):
        try:
            account = self.check_account(name, currency)
            return account.balance
        except AccountError:
            print("No account found!")
