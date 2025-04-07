#
from strings import get_hamming_distance
from strings import get_dna_complement

def main():
    while True:
        print("1-Hamming Distance")
        print("2-Dna Complement")
        print("3-Exit")
        user_choice = int(input("Choose a menu option: "))
        if user_choice == 1:
            dna1 = input("First DNA string: ")
            dna2 = input("Second DNA string: ")
            if len(dna1) != len(dna2):
                print("Error - DNA strings must be the same length to get a hamming distance.")
            else:
                dist_result = get_hamming_distance(dna1, dna2)
                print(f"The hamming distance of the 2 strings is {dist_result}.")
        elif user_choice == 2:
            dna1 = input("Original DNA string: ")
            complement_result = get_dna_complement(dna1)
            print("The DNA reverse complement of ", dna1, " is ", complement_result, ".")
        elif user_choice == 3:
            break
        else:
            print("Error! Invalid Menu Choice!")

main()
