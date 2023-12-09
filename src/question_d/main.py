#add import

import question_d


def main():
    while True:
        # Get user input for table size
        rows = int(input("There should be 5 rows for max results but you may select a different number if you want: "))
        cols = int(input("There should be 10 columns for max results but you may select a different number if you want: "))

        # Generate the multiplication table
        table = question_d.multiplication_table(rows, cols)

        # Display the multiplication table
        print("\nMultiplication Table:")
        question_d.display_table(table)

        # Ask the user if they want to continue
        user_input = input("\nDo you want to continue? (yes/no): ").lower()

        # Check if the user wants to quit
        if (user_input != 'yes') and (user_input != 'y'):
            print("Goodbye!")
            break
main()