import os
import sys

file_path = ""
did_it_run = False

def write_message_to_txtfile():
    global did_it_run,file_path
    use_input = input("What do you wanna type to ur file?\n")
    with open("carloww.txt","a") as file:
        file.write(use_input+"\n")
    did_it_run = True
    file_path = os.path.abspath(file.name)
     
if __name__ == "__main__":
    write_message_to_txtfile()

if did_it_run == True:
    print(f"Your text was written to file: {file_path}")
    open_file_prompt = input("Do you want to open the file? (Y or N)").strip().lower()
    if open_file_prompt in ("y","yes"):
        os.startfile(file_path)
    else:
        sys.exit()