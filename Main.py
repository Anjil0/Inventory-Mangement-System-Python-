# importing some modules
import os
import Sale
import Order
import Display

# creating user input action function
def userAction():
    while (True):
        print("""\n
    #################################
    !       Hitmans Laptop Shop     !
    *********************************
    !      1: For Display Laptop    !   
    !      2: For Sale Laptop       !   
    !      3: For Order Laptop      !
    !      4: For Exit              !  
    #################################   
    """)
        try:
            userInput = int(input(" Enter a option to procced: >> "))
        # User has selected 1 to display Laptops of Shop
            if userInput == 1:
                Display.displayLaptops()

        # User has selected 2 to Sell Laptops For Customer
            elif userInput == 2:
                isGenerate = Sale.customerUse()
                Sale.sellLaptops(isGenerate)
                Sale.AllTotal()
                print("""-------------------------""")
                print("""|  PLEASE, VISIT AGAIN  |""")
                print("""-------------------------""")
                os.startfile(f"{Sale.customerName}_Sale_Receipt.txt")

        # User has Selected 3 to Order Laptops from Manufacture
            elif userInput == 3:
                isCreate = Order.forDistributorName()
                Order.forOrderDetails(isCreate)
                Order.forReceiptGenerate()
                os.startfile(f"{Order.distributorName}_Order_Receipt.txt")

        # User has Selected 4 to Exit the Program
            elif userInput == 4:
                print("\n**********!!!!!! Exiting Shopppp !!!!!!*********\n")
                break
            else:
                print("\n!!------- Please, Choose a Given Option from 1 to 4 --------!!")

        except:
            print("\n!!-------- Please, Input Valid Option ( Integer ) -------!!")

userAction()
