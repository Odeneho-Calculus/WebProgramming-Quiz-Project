
#DEVELOPER:: CALCULUS GUY
#PROJECT TITLE:: WEB PROGRAMMING QUIZ
#DATE CREEATED:: 7TH SEPT. 2023
#VERSION CODE:: V 1.0.0_23

import random
import sys
import subprocess
import os
import json
import webbrowser
from colorama import init, Fore, Back, Style
def load_quiz(filename):
    with open(filename, 'r') as file:
        quiz_data = json.load(file)
    return quiz_data

def proceeder(level):
    level = level
    title(f"lv{level}")
    print("")
    print("|| 1. Replay     2. Main Menu")
    while True:
        try:
            opt = int(input("|| Choose an option to proceed (1-2): "))
            if (opt > 0 and opt <3):
                if (opt == 1):
                    if (level == 1):
                        subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                        title("lv1")
                        level1() 
                    elif (level == 2):
                        subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                        title("lv2")
                        level2()
                    elif (level == 3):
                        subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                        title("lv3")
                        level3()
                    elif (level == 4):
                        subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                        title("lv4")
                        level4()
                    elif (level == 5):
                        subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                        title("lv5")
                        level5()
                    else:
                        print("Error occured!")
                    
                elif (opt == 2):
                    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                    mainMenu()
            
                else:
                    print("|| Invalid Option!")
            else:
                print("|| Invalid Option!")
    
        except ValueError:
            print("|| Invalid Input! Please enter a valid number option (1-2).")

    

def level1():
    level = 1
    quiz_data = load_quiz("data/level1.json")
    total_questions = len(quiz_data)
    user_score = run_quiz(quiz_data)
    print(f"You answered {user_score} out of {total_questions} questions correctly.")
    print("")
    proceeder(level)

def level2():
    level = 2
    quiz_data = load_quiz("data/level2.json")
    total_questions = len(quiz_data)
    user_score = run_quiz(quiz_data)
    print(f"You answered {user_score} out of {total_questions} questions correctly.")
    print("")
    proceeder(level)
    
def level3():
    level = 3
    quiz_data = load_quiz("data/level3.json")
    total_questions = len(quiz_data)
    user_score = run_quiz(quiz_data)
    print(f"You answered {user_score} out of {total_questions} questions correctly.")
    print("")
    proceeder(level)
    
def level4():
    level = 4
    quiz_data = load_quiz("data/level4.json")
    total_questions = len(quiz_data)
    user_score = run_quiz(quiz_data)
    print(f"You answered {user_score} out of {total_questions} questions correctly.")
    print("")
    proceeder(level)
    
def level5():
    level = 5
    quiz_data = load_quiz("data/level5.json")
    total_questions = len(quiz_data)
    user_score = run_quiz(quiz_data)
    print(f"You answered {user_score} out of {total_questions} questions correctly.")
    print("")
    proceeder(level)





def title(level):
    l = level
    print("================================================================")
    print("|| ##   ## ##### #####          ####                          ||")
    print("|| ##   ## ##    ##  ##       ##    ##                        ||")
    print("|| ##   ## ####  #####   ##  ##      ##  ##  ## ##  #####     ||")
    print("|| ## # ## ##    ##  ##      ###  ## ##  ##  ## ##    ##      ||")
    print("|| ### ### ##    ##   ##      ##    ###  ##  ## ##   ##       ||")
    print(f"|| ##   ## ##### ######         ####  ##  ####  ##  ##### {l} ||")
    print("||============================================================||")

def mainMenu():
    print("================================================================")
    print("|| ##   ## ##### #####          ####                          ||")
    print("|| ##   ## ##    ##  ##       ##    ##                        ||")
    print("|| ##   ## ####  #####   ##  ##      ##  ##  ## ##  #####     ||")
    print("|| ## # ## ##    ##  ##      ###  ## ##  ##  ## ##    ##      ||")
    print("|| ### ### ##    ##   ##      ##    ###  ##  ## ##   ##       ||")
    print("|| ##   ## ##### ######         ####  ##  ####  ##  #####     ||")
    print("||============================================================||")
    print("||            CONTENTS           ||       INFORMATION         ||")
    print("||===============================||===========================||")
    print("|| 1. LEVEL 1                    || THIS SOFTWARE IS DESIGN   ||")
    print("|| 2. LEVEL 2                    || BY A COMPUTER SCIENTIST   ||")
    print("|| 3. LEVEL 3                    || CALLED CALCUCLUS GUY.     ||")
    print("|| 4. LEVEL 4                    || KINDLY GIVE CREDIT WHEN   ||")
    print("|| 5. LEVEL 5                    || YOU REMOD THIS SOFTWARE.  ||")
    print("|| 6. QUIT                       || PLEASE MAKE SURE YOU CHECK||")
    print("|| 7. CHECK FOR UPDATE           || FOR UPDATE COS IS NEEDY.  ||")
    print("================================================================")
    while True:
        try:
            opt = int(input("|| Choose an option to proceed (1-7): "))
            if (opt > 0 and opt <8):
                if (opt == 1):
                    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                    title("lv1")
                    level1()
                    
                    
                elif (opt == 2):
                    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                    title("lv2")
                    level2()
                    
                elif (opt == 3):
                    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                    title("lv3")
                    level3()
                    
                elif (opt == 4):
                    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                    title("lv4")
                    level4()
                    
                elif (opt == 5):
                    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                    title("lv5")
                    level5()
                    
                    
                    
                elif (opt == 6):
                    subprocess.run("clear" if os.name == "posix" else "cls", shell=True)
                    title("quiting")
                    print("|| Thanks for choosing our product. @Calculus Guy             ||")
                    print("|| Press any Key to close this.                               ||")
                    print("================================================================")
                    exit()
                    
                elif (opt == 7):
                    # URL to open
                    url = "https://t.me/+vQjm1OaXw4hjZjA0"

                    # Open the URL in a new browser window or tab
                    webbrowser.open_new(url)
                    
                    
                    
                else:
                    print("|| Invalid Option!")
            else:
                print("|| Invalid Option!")
    
        except ValueError:
            print("|| Invalid Input! Please enter a valid number option (1-7).")


def run_quiz(quiz_data):
    random.shuffle(quiz_data)  # Shuffle the questions for randomness
    score = 0

    for idx, question in enumerate(quiz_data, start=1):
        print(f"Question {idx}: {question['question']}")
        for option in question['options']:
            print(f"{option['option']}. {option['text']}")

        while True:
            user_answer = input("Your answer (a, b, c, d): ").lower()
            if user_answer in ['a', 'b', 'c', 'd']:
                break  # Exit the loop if the input is valid

            print("Invalid choice. Please enter a valid option (a, b, c, or d).\n")

        if user_answer == question['correct_option']:
            print(f"{question['description_correct']}\n")
            score += 1
        else:
            print(f"{question['description_incorrect']}\n")

    return score

if __name__ == "__main__":
    mainMenu()
    