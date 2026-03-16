import json
import random
from tips import tips
from colorama import init, Fore
import pyfiglet

DATA_FILE = "bank_data.json"
DATA_FILE2 = "bank2_data.json"

def load_balance():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data["balance"]
    except FileNotFoundError:
        return 0
    
def load_goal():
    try:
        with open(DATA_FILE2, "r") as file:
            data = json.load(file)
            return data["Goal"]
    except FileNotFoundError:
        return 0

def save_balance(balance):
    with open(DATA_FILE, "w") as file:
        json.dump({"balance": balance}, file)

def save_goal(goal):
    with open(DATA_FILE2, "w") as file:
        json.dump({"Goal": goal}, file)

def deposit(balance):
    try:
        amount = float(input("Enter a amount of money you want to deposit: "))
    except ValueError:
        print("Invalid number, try again.")
        return 0

    if amount < 0:
        print("That is not a valid amount, please try again")
        return 0 
    else:
        print(f"You Deposited ${amount} in your bank account")
        return amount

def withdraw(balance):
    try:
        amount = float(input("Enter the amount of money you want to withdraw: "))
    except ValueError:
        print("Invalid number, try again.")
        return 0
    if amount < 0:
        print("That is not a valid amount")
        return 0
    elif amount > balance:
        print("Insufficient funds")
        return 0
    else:
        print(f"You withdrew ${amount} from your bank account") 
        return amount
def Goal(goal):
    choice = float(input("Enter your goal: "))
    
    if choice < 0:
        print("Invalid choice, please pick a number more than 0")
        return 0
    else:
        print(f"You set a goal for ${choice}")
        return choice
def check_goal(goal, balance):
    print(f"your goal is ${goal}")
    if goal > balance:
        print(f"You are ${goal - balance} away from your goal")
    elif goal <= balance:
        print(f"You have reached your goal!")
    
def main():
    balance = load_balance()
    goal = load_goal()
    is_running = True
    while is_running:
        progress =goal - balance
        print()
        print("===================")
        print(Fore.CYAN + pyfiglet.figlet_format("Smart Save"))
        print(Fore.WHITE + "===================")
        if balance < goal*0.2:
            print(Fore.RED + " ⚠️ Warning, your balance is less than 20% of your goal,\nconsider saving more money")
        print()
        print(Fore.WHITE + f"Balance: {balance}")
        print(Fore.WHITE + f"Goal: {goal}")
        if goal > balance:
            print(Fore.WHITE + f"You are ${progress} away from your goal!")
        else:
            howmuchover = balance - goal
            print(Fore.WHITE + f"You are ${howmuchover} over your goal!")
        print()
        print(Fore.CYAN + "[1] Check Balance")
        print(Fore.YELLOW + "[2] Deposit Money")
        print(Fore.RED + "[3] Withdraw Money")
        print(Fore.MAGENTA + "[4] Set Goal")
        print(Fore.BLUE + "[5] See Goal")
        print(Fore.GREEN + "[6] Financial Tip")
        print(Fore.WHITE + "[7] Exit")
        print("===================")
        choice = input("Choose what you want to do! 1-7 : ")
        print()

        if choice == "1":
            print(f"Your Balance is {balance}")
        elif choice == "2":
            balance += deposit(balance)
            save_balance(balance)
        elif choice == "3":
            balance -= withdraw(balance)
            save_balance(balance)
        elif choice == "4":
            goal = Goal(goal)
            save_goal(goal)
        elif choice == "5":
            check_goal(goal, balance)
        elif choice == "6":
            print("-----------------")
            print("Financial Tip")
            print(random.choice(tips))
            print("-----------------")
        elif choice == "7":
            break
        else:
            print("INVALID CHOICE")
            

if __name__ == "__main__":
    main()