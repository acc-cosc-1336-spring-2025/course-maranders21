#
import class_a

def main():
    user_ext = False
    while user_ext == False:
        Hmwk_Die = class_a.Die()
        Hmwk_Die.roll()
        user_input = input("Do you want to continue? Y/N ")    
        if user_input.upper() == "N":
            return
        print(Hmwk_Die)
    





main()