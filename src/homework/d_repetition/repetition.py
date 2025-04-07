#
def get_factorial(num):
    factorial = 1
    for i in range(1,num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    total = 0;
    counter = 0;
    while counter < num:
        total += counter + 1;
        counter += 2
    return total
