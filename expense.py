import os
import datetime
import json


class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.expenses = json.load(file)
            except json.JSONDecodeError:
                print("Error reading file. Starting fresh.")
                self.expenses = []

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description=""):
        expense = {
            "id": len(self.expenses) + 1,
            "date": datetime.datetime.now().strftime("%d-%m-%Y"),
            "amount": amount,
            "category": category,
            "description": description,
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Added: ₹{amount:.2f} for {category}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("\nID  Date       Amount    Category     Description")
        print("-" * 60)
        total = 0
        for e in self.expenses:
            print(
                f"{e['id']:<3} {e['date']:<10} ₹{e['amount']:<8.2f} {e['category']:<12} {e['description']}"
            )
            total += e["amount"]
        print("-" * 60)
        print(f"Total: ₹{total:.2f}")

    def delete_expense(self, expense_id):
        for i, e in enumerate(self.expenses):
            if e["id"] == expense_id:
                del self.expenses[i]
                self.save_expenses()
                print(f"Deleted expense {expense_id}")
                return True
        print(f"Expense {expense_id} not found")
        return False

    def edit_expense(self, expense_id, amount=None, category=None, description=None):
        for e in self.expenses:
            if e["id"] == expense_id:
                if amount:
                    e["amount"] = amount
                if category:
                    e["category"] = category
                if description:
                    e["description"] = description
                self.save_expenses()
                print(f"Updated expense {expense_id}")
                return True
        print(f"Expense {expense_id} not found")
        return False


def main():
    tracker = ExpenseTracker()
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Edit expense")
        print("4. Delete expense")
        print("0. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            try:
                amount = float(input("Amount: ₹"))
                category = input("Category: ")
                description = input("Description: ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid amount")

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            try:
                expense_id = int(input("Enter ID to edit: "))
                amount = float(input("New amount (or 0 to skip): "))
                category = input("New category (or Enter to skip): ")
                description = input("New description (or Enter to skip): ")

                amount = amount if amount > 0 else None
                category = category if category else None
                description = description if description else None

                tracker.edit_expense(expense_id, amount, category, description)
            except ValueError:
                print("Invalid input")

        elif choice == "4":
            try:
                expense_id = int(input("Enter ID to delete: "))
                tracker.delete_expense(expense_id)
            except ValueError:
                print("Invalid ID")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
