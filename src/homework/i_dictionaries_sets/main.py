#
from dictionary import add_inventory
from dictionary import remove_inventory_widget
main_dictionary = {}

def main():
    while True:
        print("Inventory Menu")
        print("1- Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")
        user_choice = int(input("Choose Menu Option: "))
        if user_choice == 1:
            insert_key = input("What is the key for the dictionary item you wish to add? ")
            insert_value = input("What is the value you wish to assign / add to this key? ")
            add_inventory(main_dictionary, insert_key, insert_value)
            print("Inserted!")
        elif user_choice == 2:
            delete_key = input("What is the key for the dictionary item you wish to remove? ")
            print(remove_inventory_widget(main_dictionary(delete_key)))
        elif user_choice == 3:
            break
        else:
            print("Error! Invalid Menu Option...")

main()

