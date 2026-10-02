import datetime
import os

# Journal Manager Class
class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

        try:
            file = open(self.filename, "x")
            file.close()

        except FileExistsError:
            pass

    # Add New Entry
    def add_entry(self):

        entry = input("Enter Your Journal Entry :\n")

        try:
            file = open(self.filename, "a")

            current_time = datetime.datetime.now()

            file.write(f"[{current_time}] \n {entry}\n")

            file.close()

            print("\nEntry Added Successfully!")

        except FileNotFoundError:
            print("Error : Journal file does not exist.")

        except PermissionError:
            print("Error : You don't have permission to write the file.")

    # View All Entries
    def all_entries(self):

        try:
            file = open(self.filename, "r")

            entries = file.readlines()

            file.close()

            if len(entries) == 0:
                print("No Journal Entries found. Start by adding a new entry.")

            else:
                print("\nOutput (If the file exists):")
                print("Your Journal Entries:")
                print("--------------------------------------------------")

                for entry in entries:
                    print(entry.strip())

        except FileNotFoundError:
            print("Error : The file does not exist. Please add a new entry first.")

        except PermissionError:
            print("You do not have permission to read the file.")

    # Search Entry
    def search_entry(self):

        keyword = input("Enter a keyword or date to Search : ")

        try:
            file = open(self.filename, "r")

            found = False

            for entry in file:

                if keyword.lower() in entry.lower():

                    print("\nMatching Entry:")
                    print(entry.strip())

                    found = True

            file.close()

            if found == False:
                print("\nOutput (If no Match is Found):")
                print(f"No Entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("Error : Journal file does not exist.")

        except PermissionError:
            print("You do not have permission to read the file.")

    # Delete All Entries
    def delete_entry(self):

        try:
            ask = input("Are you sure you want to delete all entries (yes/no):")

            if ask.lower() == "yes":

                file = open(self.filename, "w")
                file.close()

                print("All Journal Entries have been deleted successfully.")

            else:
                print("Delete operation cancelled.")

        except FileNotFoundError:
            print("Error : Journal file does not exist.")

        except PermissionError:
            print("You do not have permission to delete the file.")


# Create Object
journal = JournalManager()


# Main Menu
while True:

    print("\nWelcome to Personal Journal Manager!")
    print("Please Select an Option:")
    print()
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    print()

    try:
        user = int(input("User Input:\n"))

        if user == 1:
            journal.add_entry()

        elif user == 2:
            journal.all_entries()

        elif user == 3:
            journal.search_entry()

        elif user == 4:
            journal.delete_entry()

        elif user == 5:
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option from the menu.")

    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")




