#add import

import question_c

def main():
    while True:
        print("\nMenu:")
        print("1- Display stock purchase history")
        print("2- Exit")

        option = input("Select an option (1 or 2): ")

        if option == "1":
            question_c.stock_purchase_history()
        elif option == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1 or 2.")

'''''
def main():
    while True:
        print("\nMenu:")
        print("1- Display stock purchase history")
        print("2- Exit")

        option = input("Select an option (1 or 2): ")

        if option == "1":
            stock_purchase_history()
        elif option == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1 or 2.")

    main()
'''