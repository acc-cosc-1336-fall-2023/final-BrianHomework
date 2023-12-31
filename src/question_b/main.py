#add import

import question_b
   
def main():

    stock_file_path = "get_stock_list.txt"
    question_b.create_stock_file(stock_file_path)

    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            stock_list = question_b.get_stock_list(stock_file_path)
            question_b.display_stock_list(stock_list)
            
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
