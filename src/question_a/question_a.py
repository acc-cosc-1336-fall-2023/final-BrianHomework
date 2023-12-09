#write functions here, don't add input('') statements here!
#def test_config():
 #   return True

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    dna_string1_upper = dna_string1.upper()  # Convert to uppercase
    dna_string2_upper = dna_string2.upper()  # Convert to uppercase

    for i in range(len(dna_string1_upper) - len(dna_string2_upper) + 1):
        if dna_string1.upper()[i:i + len(dna_string2_upper)] == dna_string2_upper:
            positions.append(i + 1)  # Add 1 to convert to 1-based indexing
    return tuple(positions)

def validate_dna_string(input_string, length_condition):
    if not input_string.isalpha() or not length_condition:
        return False
    return True