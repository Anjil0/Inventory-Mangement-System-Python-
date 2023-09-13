
# Function For reading laptops from a file and storing it in a dictionary

def dictionaryLaptops():
    stockLaptops = {}
    with open("laptop_data.txt", "r") as storeRoom:
        for line in storeRoom:
            data = line.strip().split(", ")
            id = len(stockLaptops) + 1
            stockLaptops[id] = {
                "name": data[0],
                "brand": data[1],
                "price": data[2],
                "quantity": int(data[3]),
                "processor": data[4],
                "graphics_card": data[5]
            }
    return stockLaptops

# Function for displaying stock laptops from stored dictionary


def displayLaptops():
    stockLaptops = dictionaryLaptops()
    print("\n#==================================== Available Stocks of Laptop ===================================#")
    print("\n=====================================================================================================")
    print("{:<8} {:<20} {:<15} {:<10} {:<15}{:<15}{:}".format("ID", "Name of Laptop",
                                                            "Brand", "Price", "Quantity", "Processor", "Graphics Card"))
    print("=====================================================================================================\n")
    for id, data in stockLaptops.items():
        print("\033[35m{:<8}{:<20}{:<15}{:<10}{:<15}{:<15}{:}\033[0m".format(
            id, data['name'], data['brand'], data['price'], data['quantity'], data['processor'], data['graphics_card']))
    print("\n#===================================================================================================#")
