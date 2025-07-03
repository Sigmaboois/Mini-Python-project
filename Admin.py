# Admin Application
import os
import sys

names = []
file_path = ""
is_run = False

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

def find_user():
    while True:  # Loop until valid input is received
        try:
            function_called = int(input("What function do you want? (1 for adding a new member, 2 to see who is in the class)"))
            if function_called not in [1, 2]:
                print("Please choose 1 or 2")
                continue
            elif function_called == 1:
                add_new_member()
            elif function_called == 2:
                printcontentoffile()
            break  # Exit loop after successful function call
        except ValueError:
            print("Only integers are allowed nothing else")
def main():
    find_user()

if __name__ == "__main__":
    main()