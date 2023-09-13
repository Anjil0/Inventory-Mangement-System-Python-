# importing some modules
import datetime
import random
import Display
date = datetime.datetime.now()
currentDate = date.strftime("%m/%d/%Y")

# For Updating Dictionary after sale/order


def writinglaptops(laptops):
    with open("laptop_data.txt", "w") as f:
        for id, details in laptops.items():
            if details['quantity'] > 0:
                f.write(
                    f"{details['name']}, {details['brand']}, {details['price']}, {details['quantity']}, {details['processor']}, {details['graphics_card']}\n")

# Taking some data from Customer and Creating Receipt


def customerUse():
    global customerName
    global isCreated
    isCreated = True
    print("\n!----------------- Enter Some Details of Customer to generate Receipt -----------------!\n")
    while (isCreated):
        # Asking Customer Name
        customerName = (input("Enter Customer Name(Without Space) : ")).strip()
        # checking customer name is empty or not
        if customerName == "":
            print("\n!!!!!!!!!! Please, Input Customer Name Without Space !!!!!!!!!\n")
            isCreated = True
        # checking input value is alphabetical name or not
        elif customerName.isalpha():
            saleNo = random.randint(1, 500)
            with open(customerName+"_Sale_Receipt.txt", "w") as customerFile:
                # creating a new text file for Customer Receipt and writing on it
                customerFile.write("""
+===================================== Hitmans Laptop Shop ======================================+
    +===================================== Sale Receipt =====================================+

        """)
                customerFile.write(
                    f"Sale No: {saleNo}\t\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                customerFile.write(
                    f"\t\t\t\t\t\t\tCustomer Name: {customerName}\n\n")
                customerFile.write(
                    "\t________________________________________________________________________________________\n\t")
                customerFile.write("{:<18} {:<15} {:<15} {:<15}{:}".format("Name of Laptop",
                                                                           "Brand", "Price", "Quantity", "Total"))
                customerFile.write(
                    "\n\t========================================================================================\n\t")
                break
        else:
            print(
                "\n!!!!!!!!!! Please, Input Proper String Name Without Space !!!!!!!!!!!\n")
            isCreated = True
    return isCreated

# Asking Data from Customer to know which laptop they want to buy


def sellLaptops(isCreated):
    inventory = Display.dictionaryLaptops()
    Display.displayLaptops()
    print("\n")
    global grandTotal
    grandTotal = 0
    global bought
    bought = False  
    while isCreated:
        # Asking User To input Id number to buy that laptop
        try:
            print(
                "\n\t---------- Choose a ID number of Laptop from Above listed Laptops To Sell--------\n")
            id = int(input(">>>>>>>>>>>>>> "))
            if id in inventory.keys():
                loopSell = True
                while loopSell:
                    try:
                        # Asking User To input Quantity of that selected laptop
                        quantity = int(
                            input("\n\t------------ Enter quantity of laptops to sell ----------\n\n>>>>>>>>>>>>>> "))
                        if quantity <= 0:
                            loopSell = True
                            print(
                                "\n!!!!!!!! Please input positive value in quantity !!!!!!!")
                        elif inventory[id]["quantity"] >= quantity:
                            loopSell = False
                            bought = True
                            # changing dollar sign in price to emptystring
                            price = int(
                                inventory[id]['price'].replace("$", ""))
                            price1 = price * quantity
                            grandTotal = grandTotal + price1
                            with open(f"{customerName}_Sale_Receipt.txt", "a+") as customer:
                                customer.write("{:<18} {:<15} {:<15} {:<15}{:}".format(inventory[id]['name'],
                                               inventory[id]['brand'], inventory[id]['price'], quantity, price1))
                                customer.write("\n\t")
                            inventory[id]["quantity"] -= quantity
                        else:
                            print(
                                "\n!!!!!!!! Insufficient quantity of laptops !!!!!!!\n")
                            loopSell = True
                    except:
                        print(
                            "\n!!!!!!! Please, Input Integer Number in Quantity !!!!!!!!\n")
                        loopSell = True
            else:
                print(
                    "\n!!!!!! ID number Not Found / See Laptop Id Carefully !!!!!!!\n")
                isCreated = True
        except:
            print("\n!!!!!!! Please, Input Proper Id Integer Number !!!!!!!!\n")
            isCreated = True
        while bought:
            print("\n\t--------- Do you Want to Buy More ( y- yes/ n - No)?--------\n")
            buyMore = input(">>>>>>>>>>>>>> ")
            if buyMore.lower() == "y":
                isCreated = True
                loopSell = True
                bought = False
            elif buyMore.lower() == "n":
                isCreated = False
                bought = False
                writinglaptops(inventory)
            else:
                print("\n!!!!!!! Please, Choose ('y' or 'n') !!!!!!!!!\n")


def AllTotal():
    totalPrice = grandTotal
    print("""
***********************************************************
|   Do you want to buy physically or Online?              |
***********************************************************
|              1 for: Physical                            |
|              2 for: Online                              |
***********************************************************""")
    while True:
        try:
            ship = int(input(">> "))
            if ship == 2:
                # Adding Shipping Charge
                total_Ship_Price = totalPrice + 500
                with open(f"{customerName}_Sale_Receipt.txt", "a+") as customer:
                    customer.write(
                        """\n\t________________________________________________________________________________________\n""")
                    customer.write(
                        "                                                           Total Price: $"+str(totalPrice)+"\n")
                    customer.write(
                        "                                                           Shipping Charge: $500\n")
                    customer.write(
                        "                                                           Total with Shipping charge: $"+str(total_Ship_Price))
                    customer.write(
                        """\n\t+========================================================================================+\n""")
                    customer.write(
                        """+========================================Thanks For Buying========================================+""")
                print("""
                        !#######################!
                        !                       !
                        !   Sold Successfully   !
                        !                       !
                        !#######################!""")
                return
            elif ship == 1:
                with open(f"{customerName}_Sale_Receipt.txt", "a+") as customer:
                    customer.write(
                        """\n\t________________________________________________________________________________________\n""")
                    customer.write(
                        "                                                             Total Price: $"+str(totalPrice)+"\n")
                    customer.write(
                        """\t+===========================================================================================+\n""")
                    customer.write(
                        """+========================================Thanks For Buying========================================+""")

                print("""
                        !#######################!
                        !                       !
                        !   Sold Successfully   !
                        !                       !
                        !#######################!""")
                return
            else:
                print("\n\t---------- Please, Choose a Given Option 1 or 2 ----------\n")
        except:
            print("\n!!!!!!!! Please, Enter Valid Option of Integer !!!!!!!!!!\n")
        totalPrice = 0
