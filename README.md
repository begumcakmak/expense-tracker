# expense-tracker

A simple command-line expense tracker written in Python. This program allows you to add, view, and filter expenses, as well as calculate the total amount spent.

## Features
- Add a new expense with an amount and category.
- View all recorded expenses.
- Calculate the total of all expenses.
- Filter expenses by category.
- Prevents actions when no expenses are recorded.
- Simple and user-friendly menu interface.

## How It Works
1. When the program starts, a menu is displayed with the following options:
   - **1:** Add an expense
   - **2:** List all expenses
   - **3:** Show total expenses
   - **4:** Filter expenses by category
   - **5:** Exit the program
2. Users can input data, and the program stores it in memory (list of dictionaries).
3. All data is lost when the program is closed (no file storage).

## How to Run
1. Save the script as `expense_tracker.py`.
2. Open a terminal or comand prompt.
3. Run:
   ```bash
   python expense_tracker.py

## Example 
Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit  
Enter your choice: 1  
Enter amount: 50  
Enter category: food  

Expense Tracker
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Exit  
Enter your choice: 3  
Total Expenses:  50.0  
