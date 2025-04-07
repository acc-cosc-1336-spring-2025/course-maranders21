#
from repetition import get_factorial
from repetition import sum_odd_numbers

def main():
    while True:
        print("Homework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        user_choice = int(input("Choose a menu option: "))
        if user_choice == 1:
            user_num = int(input("Enter a number: "))
            while user_num <= 0 or user_num >= 10:
                user_num = int(input("Invalid Input. Try again... "))
            factorial_result = get_factorial(user_num)
            print(f"The factorial of {user_num} is {factorial_result}.")
        elif user_choice == 2:
            user_num = int(input("Enter a number: "))
            while user_num <= 0 or user_num >= 100:
                user_num = int(input("Invalid Input. Try again... "))
            sum_result = sum_odd_numbers(user_num)
            print(f"The sum of all numbers from 0 to {user_num} is {sum_result}.")
        elif user_choice == 3:
            exit_check = input("Are you sure you want to exit? Y/N... ")
            if exit_check.lower() == "y":
                break
        else:
            print("Error! Incorrect choice!")
    return

main()