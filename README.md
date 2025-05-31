# Expense-Tracker

# Expense Tracker

A simple yet powerful command-line Expense Tracker application written in Python. This program helps you manage your daily expenses by allowing you to add, view, edit, and delete expense records with persistent storage.

## Features

- Add expenses with amount, category, and description
- View all expenses with a formatted display
- Edit existing expenses
- Delete expenses
- Automatic date tracking for expenses
- Persistent storage using JSON
- Total expense calculation
- Indian Rupee (₹) currency support

## Requirements

- Python 3.x
- No additional packages required (uses only built-in libraries)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. No additional installation required!

## How to Run

Run the program using Python:
```
python expense.py
```

## Usage

The program presents a menu-driven interface with the following options:

1. Add expense
2. View expenses
3. Edit expense
4. Delete expense
0. Exit

### Adding an Expense
- Select option 1
- Enter the amount (in ₹)
- Specify the category
- Add an optional description

### Viewing Expenses
- Select option 2
- Displays a formatted table with:
  - ID
  - Date
  - Amount
  - Category
  - Description
- Shows total expenses at the bottom

### Editing an Expense
- Select option 3
- Enter the expense ID
- Input new values (or skip to keep existing):
  - Amount
  - Category
  - Description

### Deleting an Expense
- Select option 4
- Enter the expense ID to delete

## Data Storage

- Expenses are stored in `expenses.json`
- Data persists between program runs
- Automatic file creation on first run
- JSON format for easy data portability

## Example Usage

```
===== Expense Tracker =====
1. Add expense
2. View expenses
3. Edit expense
4. Delete expense
0. Exit

Enter choice: 1
Amount: ₹500
Category: Food
Description: Lunch with colleagues
Added: ₹500.00 for Food
```

## Error Handling

The program includes error handling for:
- Invalid numeric inputs
- File reading/writing operations
- JSON parsing errors
- Invalid expense IDs

## Contributing

Feel free to fork this project and submit pull requests with improvements. Some areas for potential enhancement:
- Adding expense categories management
- Implementing date range filtering
- Adding data export features
- Creating expense reports and analytics

## License

This project is open source and available for educational and personal use. 
