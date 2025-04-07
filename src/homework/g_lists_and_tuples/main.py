#
from lists import get_lowest_list_value
from lists import get_highest_list_value

def main():
    while True:
        print("1-Show the list low/high values")
        print("2-Exit")
        user_choice = int(input("Choose option: "))
        if user_choice == 1:
            input_list = []
            count = 0
            cont_choice = True
            while count < 3 or cont_choice == True:
                temp_val = int(input("Enter a list value: "))
                input_list.append(temp_val)
                count += 1
                if count > 2:
                    cont_val = str(input("Do you want to enter another value? Y/N... "))
                    if cont_val.lower() == "n":
                        cont_choice = False
            min_val = get_lowest_list_value(input_list)
            max_val = get_highest_list_value(input_list)
            print(f"The minimum list value is {min_val}.")
            print(f"The maximum list value is {max_val}.")
        elif user_choice == 2:
            break
        else:
            print("Error! Invalid choice!")

main()