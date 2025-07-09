# Initialize categories and expenses
expenses = []

# Add expenses manually
def add_expense(name, amount, category):
    expenses.append({"name": name, "amount": amount, "category": category})

# Sample entries
add_expense("Groceries", 2000, "Food")
add_expense("Movie", 5000, "Entertainment")
add_expense("Internet Bill", 1000, "Utilities")
add_expense("Bus Pass", 3000, "Transport")
add_expense("Dinner", 5000, "Food")

# Total spent
total = sum(item['amount'] for item in expenses)
print(f"Total Expenses: ₹{total}\n")

# Expense by category
category_totals = {}
for item in expenses:
    cat = item["category"]
    category_totals[cat] = category_totals.get(cat, 0) + item["amount"]

print("Expenses by Category:")
for category, amount in category_totals.items():
    print(f"{category}: ₹{amount}")

# Find highest spending category
max_cat = max(category_totals, key=category_totals.get)
print(f"\nHighest Spending Category: {max_cat} (₹{category_totals[max_cat]})")

# Optional: Monthly budget check
monthly_budget = 9000
print(f"\nMonthly Budget: ₹{monthly_budget}")
if total > monthly_budget:
    print("⚠️ You are over budget!")
else:
    print("✅ You are within your budget.")