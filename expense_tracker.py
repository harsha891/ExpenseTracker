from transactions import add_transaction, view_transactions, edit_transaction, delete_transaction
from categories import add_category, view_categories
from summaries import generate_summary
from visualizations import create_pie_chart
from database import create_schema


def main_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. Manage Categories")
        print("6. Generate Summaries")
        print("7. Create Visualizations")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            add_transaction(amount, category_id, date, description)
        elif choice == '2':
            transactions = view_transactions()
            for t in transactions:
                print(t)
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID: "))
            amount = float(input("Enter new amount: "))
            category_id = int(input("Enter new category ID: "))
            date = input("Enter new date (YYYY-MM-DD): ")
            description = input("Enter new description: ")
            edit_transaction(transaction_id, amount, category_id, date, description)
        elif choice == '4':
            transaction_id = int(input("Enter transaction ID: "))
            delete_transaction(transaction_id)
        elif choice == '5':
            print("1. Add Category")
            print("2. View Categories")
            cat_choice = input("Enter your choice: ")
            if cat_choice == '1':
                name = input("Enter category name: ")
                add_category(name)
            elif cat_choice == '2':
                categories = view_categories()
                for c in categories:
                    print(c)
        elif choice == '6':
            summary = generate_summary()
            for s in summary:
                print(s)
        elif choice == '7':
            create_pie_chart()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    create_schema()
    main_menu()
