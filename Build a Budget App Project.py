class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total_balance = sum(item['amount'] for item in self.ledger)
        return total_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"
            items += f"{item['description'][:23]:23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    total_withdrawals = 0
    category_withdrawals = []

    # Calculate total withdrawals and each category's withdrawals
    for category in categories:
        category_total = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        category_withdrawals.append((category.name, category_total))
        total_withdrawals += category_total

    # Calculate percentage spent in each category
    percentages = [(name, int((amount / total_withdrawals) * 100 // 10 * 10)) for name, amount in category_withdrawals]

    # Create the chart string
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for name, percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    # Find the longest category name
    max_len = max(len(name) for name, _ in percentages)
    for i in range(max_len):
        chart += "     "
        for name, _ in percentages:
            chart += f"{name[i] if i < len(name) else ' '}  "
        chart += "\n"

    return chart.rstrip("\n")

# Example usage
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(clothing)

print(create_spend_chart([food, clothing]))
