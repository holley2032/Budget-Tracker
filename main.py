# Budget Tool

# To-do:
# Add ability to edit categories post-initializing.
# Add ability for budget to "rollover" to the next month.
# Add ability to import categories from Excel, JSON, etc. in the create_budget function
# Add some checks and confirmations throughout.
# Make data structure class-based? Perhaps each category would be an instance of the category class?
# - And maybe there would be an overarching budget class that could keep track of the overall budget spend.
# - It would probably make the code much cleaner than the current dictionary data structure.
# Create user-friendly experience, i.e. have a webapp or something that isn't the command prompt!
# Clean code, make names of functions and variables clearer and cleaner.

import datetime
import pickle


def main():
    budget_choice = check_budget()
    month = budget_choice[0]
    year = budget_choice[1]
    try:
        with open(f"Budget-{month}-{year}", "rb") as file:
            budget = pickle.load(file)
    except FileNotFoundError:
        try:
            new_month = int(month)
            new_year = int(year)
            if new_month == 1:
                new_month = "12"
                new_year = new_year - 1
                new_year = str(new_year)
            else:
                new_month = new_month - 1
                new_month = str(new_month)
                new_year = str(new_year)
            with open(f"Budget-{new_month}-{new_year}", "rb") as file:
                budget = pickle.load(file)
                for category in budget.categories:
                    category.money_total = 0
                    category.money_left = category.money_start
        except FileNotFoundError:
            budget = create_budget(Budget())
            with open(f"Budget-{month}-{year}", "wb") as file:
                pickle.dump(budget, file)
    budget = inp(budget)
    with open(f"Budget-{month}-{year}", "wb") as file:
        pickle.dump(budget, file)
    print("Your budget has been saved. Have a lovely day!")


class Budget:
    def __init__(self):
        self.categories = []
        self.name = f"{datetime.date.today().month}-{datetime.date.today().year}"

        @property
        def money_left(self):
            return self._money_left

        @money_left.setter
        def money_left(self):  # Computationally inefficient, probably not relevant for a local machine.
            self._money_left = 0
            for cat in self.categories:
                self._money_left += cat.money_left

        @property
        def money_total(self):
            return self._money_total

        @money_total.setter
        def money_total(self):  # Computationally inefficient, but that is probably not relevant for a local machine.
            self._money_total = 0
            for cat in self.categories:
                self._money_total += cat.money_total


class BudgetCategory:
    def __init__(self, money, name, budget):
        self.money_left = money
        self.money_start = money
        self.name = name
        budget.categories.append(self)
        self.money_total = 0


def check_budget():
    try:
        year = input("What year would you like to choose for your budget? ")
        month = input("What month? ")
        with open(f"Budget-{month}-{year}", "rb") as file:
            pass
        return (month, year)
    except IOError:
        return (month, year)


def create_budget(budget):
    # total_budget = input("Please enter your total budget:")  # Not certain if I want to keep these two lines.
    # budget = Budget(total_budget)
    while True:
        cat = input("Please name your category. Type exit to finish editing your budget: ")
        if cat.lower() == "exit":
            break
        value = int(input("Please insert the amount allotted to this budget item: "))
        print("Is the following correct?")
        print(f"{cat}, {value}")
        confirm = input("Please confirm if this is accurate (Y/N): ")  # Make more user-friendly?
        if confirm.lower() == "y":
            BudgetCategory(value, cat, budget)
            print("Your category has been added.")
            continue
        if confirm.lower() == "n":
            print("The category has NOT been added. Please continue.")
            continue
        else:
            print("Sorry, please type Y for yes, or N for no.")
            counter = 0
            while True:  # Is there a better, cleaner way to accomplish this?
                counter += 1
                if counter >= 5:  # In case a user is completely stuck, this will terminate this inner loop and proceed
                    # as if the the user typed "N".
                    break
                print("Is the following correct?")
                print(f"{cat}, {value}")
                confirm = input("Please confirm if this is accurate (Y/N): ")  # Make more user-friendly?
                if confirm.lower() == "y":
                    BudgetCategory(value, cat, budget)
                    print("Your category has been added.")
                    break
                if confirm.lower() == "n":
                    print("The category has NOT been added. Please continue.")
                    break
                else:
                    print("Sorry, please type Y for yes, or N for no.")
                    continue
    return budget


def inp(budget):
    while True:  # Add a time-out? Like, after 1 minute of inactivity maybe?
        try:
            print(budget.name)
            for x, cat in enumerate(budget.categories):  # Display decimals to 2 digits.
                print(f"{x + 1}: {cat.name}")  # Needs to have a better format.
            selection = input("Please select which category you would like to view.\n"
                              "Type 'add' to add more categories to your budget\n"
                              "Type 'eval' to evaluate your spending so far this month\n"
                              "Type 'exit' to end the program: ")
            if selection.lower() == "add":
                create_budget(budget)
            if selection.lower() == "eval":
                total = 0
                for cat in budget.categories:
                    print(f"{cat.name}: {cat.money_total}")  # Format in a clearer, cleaner way.
                    total += cat.money_total
                print(f"total: {total}")
            if selection.lower() == "exit":
                print("Have a good day!")
                break
            selection = int(selection) - 1  # Add ability to select category with the category name.
            if selection not in range(0, len(budget.categories)):
                print('Please select a valid number.')
                continue
            category = budget.categories[selection]
            print(f"{category.name}: {round(category.money_left, 2)}")
            try:
                receipt = round(float(input("How much money does the receipt indicate? ")), 2)
                category.money_left -= receipt
                category.money_total += receipt
                print(f"{receipt} has been deducted from {category.name}.\n"  # Make this message better.
                      f" The remaining balance for this category is now {round(category.money_left, 2)}.\n"
                      f" You have spent {round(category.money_total, 2)} on this category this month.")
                continue
            except ValueError:
                print(ValueError("Please select a number."))
                continue

        except ValueError:
            print(ValueError("Please select a number."))
            continue
    return budget


main()
