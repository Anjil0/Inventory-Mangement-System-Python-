# importing some modules
import Display
import Sale
import datetime
import random
date = datetime.datetime.now()
currentDate = date.strftime("%m/%d/%Y")


def forDistributorName():
    global distributorName
    isReceiptOrder = True
    print("\n!----------------- Enter Some Details of Distributor to generate Receipt -----------------!\n")
    while (isReceiptOrder):
        # Asking Distributor Name
        distributorName = (
            input("\n\t------- Enter The Distributor Name (Without Space)-------\n>>> ")).strip()
        # checking Distributor name is empty or not
        if distributorName == "":
            print("\n!!!!!!! Please, Input Distributor Name (Without Space)!!!!!!\n")
            isReceiptOrder = True
        # checking input value is alphabetical name or not
        elif distributorName.isalpha():
            orderNo = random.randint(1, 500)
            with open(distributorName+"_Order_Receipt.txt", "w") as distributorFile:
                # creating a new text file for Distributor Receipt and writing on it
                distributorFile.write("""
+====================================== Hitmans Laptop Shop =====================================+
    +==================================== Order Receipt =====================================+

        """)
                distributorFile.write(
                    f"Order No: {orderNo}\t\t\t\t\t\t\t\t\t Date: {currentDate}\n")
                distributorFile.write(
                    f"\t\t\t\t\t\t\tDistributor Name: {distributorName}\n\n")
                distributorFile.write(
                    "\t________________________________________________________________________________________\n\t")
                distributorFile.write("{:<18} {:<15} {:<15} {:<15}{:}".format("Name of Laptop",
                                                                    "Brand", "Price", "Quantity", "Total"))
                distributorFile.write(
                    "\n\t========================================================================================\n\t")
                break
        else:
            print(
                "\n!!!!!!!!!! Please, Input Proper Distributor Name (Alphabet letters) !!!!!!!!!!!\n")
            isReceiptOrder = True
    return isReceiptOrder


def forOrderDetails(isReceiptOrder):
    inventory = Display.dictionaryLaptops()
    Display.displayLaptops()
    print("\n")
    global netTotal
    netTotal = 0
    isOrdered = False
    while isReceiptOrder:
        # Asking User To input Id number to buy that laptop
        try:
            print(
                "\n\t----- Choose a ID number of Laptop from Above listed Laptops To Order ----\n")
            id = int(input(">>>>>>>>>>>>>> "))
            if id in inventory.keys():
                loopOrder = True
                while loopOrder:
                    try:
                        # Asking User To input Quantity of that selected laptop
                        quantity = int(
                            input("\n\t--------- Enter quantity of Selected laptop to Be Order -------\n\n>>>>>>>>>>>>>> "))
                        if quantity <= 0:
                            loopOrder = True
                            print(
                                "!!!!!!!! Please input positive value in quantity !!!!!!!")
                        else: 
                            loopOrder = False
                            isOrdered = True
                            # changing dollar sign in price to emptystring
                            price = inventory[id]['price'].replace("$", "")
                            price1 = int(price) * quantity
                            netTotal = netTotal + price1
                            with open(f"{distributorName}_Order_Receipt.txt", "a+") as distributorFile:
                                distributorFile.write("{:<18} {:<15} {:<15} {:<15}{:}".format(inventory[id]['name'],
                                   inventory[id]['brand'], inventory[id]['price'], quantity, price1))
                                distributorFile.write("\n\t")
                            inventory[id]["quantity"] += quantity
                    except:
                        print(
                            "\n!!!!!!! Please, Input Integer Number in Quantity !!!!!!!!\n")
                        loopOrder = True
            else:
                print(
                    "\n!!!!!! ID number Not Found / See Laptop Id Carefully !!!!!!!\n")
                isReceiptOrder = True
        except:
            print("\n!!!!!!! Please, Input Proper Id Integer Number !!!!!!!!\n")
            isReceiptOrder = True
        while isOrdered:
            print("\n\t--------- Do you Want to Order More ( y- yes/ n - No)--------\n")
            orderMore = input(">>>>>>>>>>>>>> ")
            if orderMore.lower() == "y":
                isReceiptOrder = True
                loopOrder = True
                isOrdered = False
            elif orderMore.lower() == "n":
                isReceiptOrder = False
                loopOrder = False
                isOrdered = False
                Sale.writinglaptops(inventory)
            else:
                print("\n!!!!!!! Please, Choose ('y' or 'n') !!!!!!!!!\n")


def forReceiptGenerate():
    grandTotal_with_VAT = netTotal * (1 + 0.13)
    grandTotal_with_VAT = round(grandTotal_with_VAT, 2)
    vat_Charge = grandTotal_with_VAT - netTotal
    vat_Charge = round(vat_Charge, 2)
    # Adding VAT Charge
    with open(f"{distributorName}_Order_Receipt.txt", "a+") as distributorFile:
        distributorFile.write(
            """\n\t________________________________________________________________________________________\n""")
        distributorFile.write(
            "                                Net Total: $"+str(netTotal)+"\n")
        distributorFile.write(
            "                                VAT Rate : 13%"+"\n")
        distributorFile.write(
            "                                VAT Charge : $"+str(vat_Charge)+"\n")
        distributorFile.write(
            "                              Grand Total with VAT charge: $"+str(grandTotal_with_VAT))
        distributorFile.write(
            """\n\t+========================================================================================+\n""")
        distributorFile.write(
            """+========================================Thanks For Ordering========================================+""")
    print("""
            !#######################!
            !                       !
            !  Ordered Successfully !
            !                       !
            !#######################!""")
