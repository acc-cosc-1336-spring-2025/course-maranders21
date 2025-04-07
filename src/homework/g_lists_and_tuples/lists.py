#
def get_lowest_list_value(list):
    min_value = list[0]
    for item in list:
        if item < min_value:
            min_value = item
    return min_value

def get_highest_list_value(list):
    max_value = list[0]
    for item in list:
        if item > max_value:
            max_value = item
    return max_value