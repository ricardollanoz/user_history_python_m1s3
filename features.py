# feature to add products to the inventory
def add_product(inventory):
    
    product_name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    # A dictionary is created to storage variables
    product = {
        'name': product_name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product) #this adds a dictionary to list called inventory
    print("Product added successfully ✔")

#feature to show inventory
def show_inventory(inventory):
    for detail in inventory: #For loop to show every dictionary stored 
                print(f"Producto: {detail['name']}")
                print(f"Price {detail['price']}")
                print(f"Quantity: {detail['quantity']}\n")

def search_product(inventory):
    product_namee = input("Enter the product name: ")
    for name in inventory:
        if name['name'] == product_namee :
            print(f"Producto: {name['name']}")
            print(f"Price {name['price']}")
            print(f"Quantity: {name['quantity']}\n")
    
    print("Product unknown")