class BudgetCategory:
    def __init__(self, money, name, budget):
        self.money_left = money
        self.money_start = money
        self.name = name
        budget.categories.append(self)
        self.money_total = 0