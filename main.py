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

import json
import datetime

#Add subcategories


def main():
    new_month()
    basebudget = jsonload()
    basebudget = inp(basebudget)
    jsonsave(basebudget)
    # json load
    # ask if new month
    # list categories of budget
    # ask for number
    pass

def new_month(): # Should create a new json file when the month has changed.
    try: #Rollover option? Add in last month's budget to this month's?
        fout = open(f"{str(datetime.datetime.today())[0:7]}.json", "r")
    except:
        fout = open(f"{str(datetime.datetime.today())[0:7]}.json", "w")
        basebudget = create_budget()
        jsonsave(basebudget)
        # Do things to prep this for adjusting numbers.
    finally:
        fout.close()

def jsonload():
    try:
        file = open(f"{str(datetime.datetime.today())[0:7]}.json", "r")
        basebudget = json.load(file)
        file.close()
        return basebudget
    except: # Convert to with statement instead?
        pass
    finally:
        try:
            file.close()
        except:
            pass

def jsonsave(basebudget): # Make sure this datetime object ends up being the same as in jsonload.
    try: # Export to Excel too?
        file = open(f"{str(datetime.datetime.today())[0:7]}.json", "w")
        basebudget = json.dump(basebudget, file)
        file.close()
    except:
        pass
    finally:
        try:
            file.close()
        except:
            pass



def inp(basebudget):
    while True: # Add a time-out? Like, after 1 minute of inactivity maybe?
        try:
            for x, di in enumerate(basebudget): # Display decimals to 2 digits.
                print(f"{x + 1}: {di}") # Format better, but I like having the current money number.
            selection = input("Please select which category you would like to view. Type exit to end the program: ")
            if selection.lower() == "exit":
                print("Have a good day!")
                break
            selection = int(selection) - 1
            if selection not in range(0, len(basebudget)):
                print('Please select a valid number.')
                continue
            print(basebudget[selection])
            try:
                receipt = float(input("How much money does the receipt indicate? "))
                basebudget[selection][next(iter(basebudget[selection].keys()))] -= receipt
                print(f"You have subtracted {receipt}" # Make this message better!
                      f" from {basebudget[selection]}. The total balance for this category is now "
                      f"{basebudget[selection][next(iter(basebudget[selection].keys()))]}")
                continue # Add confirmation message!
            except ValueError:
                print(ValueError("Please select a number."))
                continue

        except ValueError:
            print(ValueError("Please select a number."))
            continue
    return basebudget


def create_budget():
    budget = []
    while True:
        key = input("Please name your category. Type exit to finish your budget: ") # Make it a bit nicer of a prompt?
        # I.e. maybe have the "type exit" on a new line and find a way to keep the input come in on the first line?
        # Probably something that would need a user interface beyond the console anyway, though.
        if key.lower() == "exit":
            break
        value = int(input("Please insert the amount alloted to this budget item: "))
        print("Is the following correct?")
        print(f"{key}: {value}")
        confirm = input("Please confirm if this is accurate (Y/N): ") # Make more user-friendly?
        if confirm.lower() == "y":
            budget.append({key: value})
            print("Your category has been added.")
            continue
        if confirm.lower() == "n":
            print("The category has NOT been added. Please continue.")
            continue
        else:
            print("Sorry, please type Y for yes, or N for no.")
            counter = 0
            while True: # Is there a better, cleaner way to accomplish this?
                counter += 1
                if counter >= 5: # In case a user is completely stuck, this will terminate this inner loop and proceed
                    # as if the the user typed "N".
                    break
                print("Is the following correct?")
                print(f"{key}: {value}")
                confirm = input("Please confirm if this is accurate (Y/N): ")  # Make more user-friendly?
                if confirm.lower() == "y":
                    budget.append({key: value})
                    print("Your category has been added.")
                    break
                if confirm.lower() == "n":
                    print("The category has NOT been added. Please continue.")
                    break
                else:
                    print("Sorry, please type Y for yes, or N for no.")
                    continue
    return budget


main()
