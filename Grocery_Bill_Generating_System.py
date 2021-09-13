# **************************** Grocery Bill Generating System ***************************
""" This function will simply make the receipt bill """

# Importing library
from datetime import datetime

# Generating electric bill
bill_rec = {}
def receipt_bill(name, bill):
    print("**************************************")
    print("\nStore name: Shubham Grocery shop.")
    print(f"\nCostumer name: \t\t{name}")
    print(f"\nBuy Item \t \t Bill / Price\n")
    for i, item in enumerate(bill_rec.keys()):
        print(f"{i + 1}.{item.capitalize()} \t:\t {bill_rec.get(item)}")
    print(f"\nTotal Bill: \t\t{bill}. \n\n\nThanks shopping with us...!\n")
    print("**************************************")

# Recording all the activities in the shop
def login(amount):
    global name
    with open("record.txt", "a") as f:
        f.write(f"{name.capitalize()} Visited our shop and Buy {amount} amount of things on {datetime.now()}\n")

if __name__ == '__main__':

    name = input("\nEnter your name: ")
    bill = 0
    while True:
        try:
            User_Buy = input("\nWhat you buy (Q or D for quit): ")
            if User_Buy.lower() == 'd' or User_Buy.lower() == 'q':
                pass
            else:
                user_input = int(input("\nEnter the price: "))
        except Exception as e:
            print("\nOnly integers are allowerd...!")
            continue
        else:
            if User_Buy.lower() == 'd' or User_Buy.lower() == 'q':
                receipt_bill(name, bill)
                login(bill)
                quit()
            else:
                try:
                    bill = bill + user_input
                    bill_rec[User_Buy] = user_input
                    print("Order total so far is ", bill)
                except Exception as e:
                    print("Sorry something went wrong...!")
            
