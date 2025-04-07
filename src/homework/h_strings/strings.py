#
def get_hamming_distance(dna1, dna2):
    hamming_distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    return hamming_distance

def get_dna_complement(dna):
    reverse_complement = ""
    char_com = "A"
    for char in dna:
        if char == "A":
            char_com = "T"
        elif char == "T":
            char_com = "A"
        elif char == "C":
            char_com = "G"
        elif char == "G":
            char_com = "C"    
        reverse_complement = char_com + reverse_complement
    return reverse_complement
