# Bank Management System

## Introduction
This project is a Python-based Bank Management System designed to automate core banking processes such as account creation, balance checking, deposits, transactions, and account modifications. It provides a command-line interface to manage customer records securely and efficiently.

## Features
- Create, modify, and delete customer accounts
- Deposit and transact money
- Print account statements
- Password-protected account access
- Admin view for full customer database
- Fast data retrieval using binary file storage (`pickle` module)

## Technologies Used
- **Language**: Python
- **Storage**: Binary files via `pickle`
- **Modules**:
  - `random`: for generating account numbers
  - `pickle`: for storing and retrieving records

## Functions Implemented
- `create_acc()`: Create new customer accounts
- `deposit()`: Deposit amount into account
- `trans_amt()`: Withdraw/transfer amount
- `edit()`: Modify customer details
- `delete()`: Delete account
- `statement()`: View account statement
- `pass_word()`: Validate password

## Security
- Password authentication required for account access
- Admin access protected with name and PIN

## Usage
Run the program through a Python IDE or terminal and follow the interactive prompts to access different banking features.

## Disclaimer
This system is a simplified educational project and is not intended for production use.

