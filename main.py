# Budget Tool
# To-do:
# Create File I/O system
# Create individual categories
# Put in things

import json
import datetime

#Add subcategories


def main():
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
        reading = json.load(fout)
        print(reading)
    except:
        fout = open(f"{str(datetime.datetime.today())[0:7]}.json", "w")
        json.dump(basebudget, fout)
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
                print(f"You have subtracted {receipt}"
                      f" from {basebudget[selection]}. The total balance is now "
                      f"{basebudget[selection][next(iter(basebudget[selection].keys()))]}")
                continue # Add confirmation message!
            except ValueError:
                print(ValueError("Please select a number."))
                continue

        except ValueError:
            print(ValueError("Please select a number."))
            continue
    return basebudget

main()
