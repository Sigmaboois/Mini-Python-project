import Admin
import os
import sys
import time

def function_called():
    prompt = input("What function do you want?\n" \
    "1.Make an application to the school\n" \
    "2.Search for classes\n" \
    "3.Exit")
    
def apply():
    parent_name = input("what is the full legal name of the mother/father/legal gaurdian?\n").lower().strip()
    student_age = int(input("What is the age of the student applying?\n"))
    student_name = input("What is the name of the student applying?\n").lower().strip()
    student_status = input("Has the student been to other previous schools (leave empty if not)If yes please state the school(s)\n").lower().strip()
    student_grade = input("What is the student's current grade?\n").lower().strip()
    student_departement = input("What departement is he/she joining? (IGCSE,American)").lower().strip()
    student_allergies = input("Does the student have any medical allergies the school should be aware of?").lower().strip()
    student_gender = input("What is the gender of the student?").lower().strip()
    student_nationality = input("What is the nationality of the student?").lower().strip()
    student_languages = input("What languages does the student speak?")

    if student_status == "":
        student_status = "None"
    print(f"{student_name.capitalize()} Application.\n")
    print("======================================================================================================")
    print("\n")
    print("Student Information:\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"Student Age: {student_age}.\n")
    print(f"Student's previous schools: {sorted(student_status)}\n")
    print(f"Departement: {student_departement}\n")
    print(f"Student current grade: {student_grade}")
    print("____________________________________________________________________________________________________________________________________________________________________________")
    print("Legal Guardian Information:\n")
    print("\n")
    print(f"Full Legal Name: {parent_name}")
    
