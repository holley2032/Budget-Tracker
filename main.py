# Budget Tool
# To-do:
# Create File I/O system
# Create individual categories
# Put in things

import json
import datetime

basebudget = [{"Tithing": 125}, {"Food": 600}, {"Counseling": 156}]

#Add subcategories


def main(filename):
    # json load
    # ask if new month
    # list categories of budget
    # ask for number
    pass

def new_month(): # Should create a new json file when the month has changed.
    try:
        fout = open(f"{str(datetime.datetime.today())[0:7]}.json", "r")
        reading = json.load(fout)
        print(reading)
    except:
        fout = open(f"{str(datetime.datetime.today())[0:7]}.json", "w")
        json.dump(basebudget, fout)
        # Do things to prep this for adjusting numbers.
    finally:
        fout.close()

def jsonload(filename):
    pass

def inp():
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
                continue
            except ValueError:
                print(ValueError("Please select a number."))
                continue

        except ValueError:
            print(ValueError("Please select a number."))
            continue

inp()