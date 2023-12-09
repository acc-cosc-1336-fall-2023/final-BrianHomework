#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self._symbol = symbol
        self._company_name = company_name

    def get_symbol(self):
        return self._symbol

    def get_company_name(self):
        return self._company_name

def stock_purchase_history():
    # Create instances of Stock
    aapl = Stock("AAPL", "Apple Inc")
    cat = Stock("CAT", "Caterpillar")
    ek = Stock("EK", "Eastman Kodak")
    goog = Stock("GOOG", "Google")
    msft = Stock("MSFT", "Microsoft")

    # Add stocks to a dictionary
    stocks_dict = {
        aapl.get_symbol(): aapl.get_company_name(),
        cat.get_symbol(): cat.get_company_name(),
        ek.get_symbol(): ek.get_company_name(),
        goog.get_symbol(): goog.get_company_name(),
        msft.get_symbol(): msft.get_company_name(),
    }

    # Display stock purchase history
    print("Stock Purchase History:")
    print("{:<10} {:<20}".format("Symbol", "Company Name"))
    for symbol, company_name in stocks_dict.items():
        print("{:<10} {:<20}".format(symbol, company_name))

#stock_purchase_history()

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
