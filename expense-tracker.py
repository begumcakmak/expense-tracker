def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return list(filter(lambda expense: expense['category'] == category, expenses))
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ').strip().lower()
            add_expense(expenses, amount, category)

        elif choice == '2':
            if not expenses:
                print("\nList is empty.")
            else:
                print('\nAll Expenses:')
                print_expenses(expenses)
    
        elif choice == '3':
            if not expenses:
                print("\nList is empty.")
            else:
                print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            if not expenses:
                print("\nList is empty.")
            else:
                category = input('Enter category to filter: ').strip().lower()
                expenses_from_category = filter_expenses_by_category(expenses, category)
                if not expenses_from_category:
                    print(f"\nNo expenses found for category {category}.")
                else:
                    print(f'\nExpenses for {category}:')
                    print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break
        else:
            print("\nPlease enter a valid number.")
main()