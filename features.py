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
    
    search_name = input("Enter the product name: ")
    if not inventory:
            print("Inventory is empty")
    for name in inventory:
        if name['name'] == search_name :
            print(f"Producto: {name['name']}")
            print(f"Price {name['price']}")
            print(f"Quantity: {name['quantity']}\n")
        
        else:
            print("Unknown product")

def update_product(inventory):
      new_price = None
      new_quantity= None
      update_name = input("Enter the product name: ")
      for update in inventory:
            if update['name'] == update_name:
                new_price = float(input("Ingrese nuevo precio: "))
                new_quantity = int(input("Ingrese nueva cantidad: "))
                update['price'] = new_price
                update['quantity'] = new_quantity

                print(f"Producto: {update['name']}")
                print(f"Price {update['price']}")
                print(f"Quantity: {update['quantity']}\n")
                print("Product recorded successfully ")

                                    
      