#
from decisions import get_options_ratio
from decisions import get_faculty_rating

def main():
    user_options = float(input("Please enter options: "))
    user_total = float(input("Please enter total: "))
    result = get_options_ratio(user_options, user_total)
    print (get_faculty_rating(result))
                       
main()