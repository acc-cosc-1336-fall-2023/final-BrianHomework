#add import
#from question_a.question_a import get_most_likely_ancestor_consensus, validate_dna_string
import question_a

def main():
    while True:
            
        while True:    
            try:
                dna_string1 = input("Enter a DNA string (length from 9 and 16): ").upper()
                if not question_a.validate_dna_string(dna_string1, 9 <= len(dna_string1) <= 16):
                    raise ValueError("Invalid DNA string length.")
                break
                  
            except ValueError as e:
                print("Error:", e)

        while True:
            try:    
                dna_string2 = input("Enter a DNA substring of exactly 4 characters: ")
                if not question_a.validate_dna_string(dna_string2, 4 == len(dna_string2)):
                    raise ValueError("Invalid DNA substring length.")
            
                positions = question_a.get_most_likely_ancestor_consensus(dna_string1, dna_string2)
                break

            except ValueError as e:
                print("Error:", e)
        
        print("Occurrences of {} in {} are at positions: ".format(dna_string2, dna_string1, positions), end= " ")

        for i in range(len(positions)):
            print (positions[i], end=" ")

        print(" ")    

        while True:
            opt_out = input("Do you want to continue? (yes/no): ").lower()
            if opt_out in ('yes', 'no', 'y', 'n'):
                break
            else:
                print("Please enter a valid input ('yes', 'no', 'y', 'n'). ")

        if opt_out.lower() == 'no' or opt_out.lower() == 'n':
            break  # Exit the outermost loop
main()