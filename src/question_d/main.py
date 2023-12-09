#add import

from question_d.question_d import display_table, multiplication_table


def main():
    while True:
        # Get user input for table size
        rows = int(input("Enter the number of rows for the multiplication table: "))
        cols = int(input("Enter the number of columns for the multiplication table: "))

        # Generate the multiplication table
        table = multiplication_table(rows, cols)

        # Display the multiplication table
        print("\nMultiplication Table:")
        display_table(table)

        # Ask the user if they want to continue
        user_input = input("\nDo you want to continue? (yes/no): ").lower()

        # Check if the user wants to quit
        if user_input != 'yes':
            print("Goodbye!")
            break
    main()