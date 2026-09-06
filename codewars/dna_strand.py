def DNA_strand(dna):

    pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}

    output = ""

    for char in dna:
        output += pairs[char]

    return output


print(DNA_strand("AAAA"))
