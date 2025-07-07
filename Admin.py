# Admin Application
import os
import sys
import time

names = []
file_path = ""
is_run = False

def file_auto_create():
    global file_path
    with open("class.txt","a") as file:
        file_path = os.path.abspath(file.name)
    

def add_new_member():
    global file_path
    with open("class.txt", "a") as file:
        while True:
            user_input = input("Enter a name (or 'done' to finish):\t")
            if user_input.rstrip().lower() == 'done':
                break
            names.append(user_input.rstrip())
            file.write(f"{user_input}\n")  # Write each name as it’s entered
        file_path = os.path.abspath(file.name)

def printcontentoffile():
    with open("class.txt", "r") as file:
        for line in sorted(file):
            print(line)

def search_for_user():
    
    search_for_user = input("What name are u looking for?\n").strip().lower()
    found = False

    with open(file_path) as file:
        for line in file:
            if line.strip().lower() == search_for_user:
                print(f"Name found: {line.strip()}")
                found = True
                break
        if not found:
           if not found:
                print("name not found")
                prompt_user = input("Would you like to open the file and search manually? (Y or N): ").strip().lower()
                if prompt_user == "y":
                    os.startfile(file_path)

def user_prompt():
    while True:
        try:
            function_called = int(input(
                "\nWhat function do you want?\n"
                "1. Add a new member\n"
                "2. View class list\n"
                "3. Search for a member\n"
                "4. Exit\n"
                "Enter your choice: "
            ))
            if function_called not in range(1, 5):
                print("Please choose a number between 1 and 4.")
                continue
            elif function_called == 1:
                add_new_member()
            elif function_called == 2:
                printcontentoffile()
            elif function_called == 3:
                search_for_user()
            elif function_called == 4:
                print("Exiting program. Goodbye!")
                sys.exit()
        except ValueError:
            print("Only integers are allowed.")
    
def main():
    file_auto_create()
    user_prompt()

if __name__ == "__main__":
    main()