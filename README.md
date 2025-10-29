# Bank Account Management System (Python OOP)

A simple object-oriented banking system written in Python.
This project demonstrates the use of OOP principles, exception handling, and modular design to simulate real-world banking operations such as creating accounts, depositing, withdrawing, and transferring funds.

## UML Design

<img src="Screenshot 2025-10-29 112549.png" width="600" alt="Bank System Demo" />


## Features

Create and manage multiple bank accounts

Support for multiple currencies

Perform deposits, withdrawals, and transfers

Track all transactions (Deposits and Withdrawals)

Automatic assignment of unique account IDs

Comprehensive error handling with custom exception classes

## Class Structure
### 1. Transaction

Base class for all financial transactions.

Records date, time, amount, and currency.

Raises TransactionError for invalid amounts.

### 2. Deposit and Withdrawal

Subclasses of Transaction.

Represent money added or removed from an account.

### 3. BankAccount

Represents an individual user account.

#### Tracks:

Owner’s name

Account ID

Currency

Balance

Transaction history

Provides methods for:

deposit(amount)

withdraw(amount)

n_transactions() — count transactions by type

### 4. BankAccountManager

Manages multiple BankAccount objects.

Stores accounts in a nested dictionary by name and currency:

{
    "Berrak": {
        "TRY": BankAccount(...),
        "USD": BankAccount(...)
    },
    "Selim": {
        "EUR": BankAccount(...)
    }
}


## Supports:

open_account(name, currency)

check_account(name, currency)

get_account(name, currency)

deposit(name, amount, currency)

withdraw(name, amount, currency)

transfer(from_name, to_name, amount, currency)

balance(name, currency)

## Example Usage
from bank_system import BankAccountManager

manager = BankAccountManager()

### Open accounts
berrak_acc = manager.open_account("Berrak", "TRY")
selim_acc = manager.open_account("Selim", "TRY")

### Deposit and withdraw
manager.deposit("Berrak", 1000, "TRY")
manager.withdraw("Berrak", 200, "TRY")

### Transfer between users
manager.transfer("Berrak", "Selim", 300, "TRY")

### Check balance
print(manager.balance("Berrak", "TRY"))  # Output: 500
print(manager.balance("Selim", "TRY"))   # Output: 300

## Error Handling

Custom exception classes ensure robustness:

AccountError — for missing or duplicate accounts

WithdrawError — for invalid or insufficient withdrawals

DepositError — for invalid deposits

TransactionError — for invalid transaction operations

## Requirements

Python 3.10+

Standard libraries only (no external dependencies)

## Concepts Demonstrated

Object-Oriented Programming (Inheritance, Polymorphism, Encapsulation)

Exception Handling

Static Methods

Type Hinting (typing.Union, List)

Data structures (defaultdict, nested dictionaries)

Time-stamping with datetime

## Author

Berrak
Software Engineering Student @ Middle East Technical University
Passionate about data-driven systems and scalable software design.
