#add import
#from question_a.question_a import get_most_likely_ancestor_consensus, validate_dna_string
import question_a

def main():
    while True:
            
        while True:    
            try:
                dna_string1 = input("Enter a DNA string (length between 8 and 16): ")
                if not question_a.validate_dna_string(dna_string1, 8 <= len(dna_string1) <= 16):
                    raise ValueError("Invalid DNA string length.")
                break
                  
            except ValueError as e:
                print("Error:", e)

        while True:
            try:    
                dna_string2 = input("Enter a DNA substring of exactly 4 characters: ")
                if not question_a.validate_dna_string(dna_string2, 4 <= len(dna_string2) <= 4):
                    raise ValueError("Invalid DNA substring length.")
            
                positions = question_a.get_most_likely_ancestor_consensus(dna_string1, dna_string2)
                break

            except ValueError as e:
                print("Error:", e)
        
        print("Occurrences of {} in {} are at positions: ".format(dna_string2, dna_string1), end= " ")

        for i in range(len(positions)):
            print (positions[i], end=" ")

        print(" ")    

        opt_out = input("Do you want to continue? (yes/no): ").lower()
        if opt_out not in ('yes', 'y'):
            break
main()   