# Bank Account System

A simple Python-based bank account system that allows users to perform basic banking operations through a command-line interface.

## 📋 Description

This project simulates a basic banking system where users can:
- Deposit money into their account
- Withdraw money from their account
- View their transaction statement
- Exit the system

The system includes safety features like daily transaction limits and maximum transaction amounts to ensure secure operations.

## ✨ Features

- **Deposit Management**: 
  - Maximum 3 deposits per day
  - Maximum deposit amount: US$ 1000 per transaction
  - Positive amount validation

- **Withdrawal Management**:
  - Maximum 3 withdrawals per day  
  - Maximum withdrawal amount: US$ 1000 per transaction
  - Sufficient balance validation

- **Account Statement**: View complete transaction history with current balance
- **User-Friendly Menu**: Simple text-based interface for easy navigation

## 🛠️ Technologies Used

- Python 3.x
- Basic Python concepts (loops, conditionals, variables, string manipulation)

## 🚀 How to Use

1. Run the Python script:
```bash
python bank_account.py
```

2. Choose from the following options:
   - **[D]**: Make a deposit
   - **[W]**: Make a withdrawal  
   - **[S]**: View account statement
   - **[Q]**: Quit the system

3. Follow the prompts to complete your transactions.

## 📁 Project Structure

The main file `bank_account.py` contains:
- User menu interface
- Balance and transaction tracking
- Deposit and withdrawal logic with limits
- Transaction history recording
- Input validation and error handling

## ⚙️ System Rules

- **Initial Balance**: US$ 0
- **Daily Deposit Limit**: 3 transactions
- **Daily Withdrawal Limit**: 3 transactions  
- **Maximum Transaction Amount**: US$ 1000
- **Balance Protection**: Cannot withdraw more than available balance

## 💡 Key Features

- Prevents overdrafts
- Tracks daily transaction counts
- Maintains complete transaction history
- Input validation for amounts
- User-friendly error messages

## 🔒 Security Notes

This is an educational project for demonstration purposes. For real banking applications, additional security measures would be necessary.

## 📝 License

This project is open source and available for educational use.
