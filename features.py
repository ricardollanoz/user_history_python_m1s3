# feature to add products to the inventory
def add_product(inventory):
    
    product_name = valid_text("Product name: ").upper()
    price = valid_positive_number("Price: ")
    quantity = valid_positive_number("Quantity: ")
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
                

#feature to search for product into inventory
def search_product(inventory):
    search_name = valid_text("Enter the product name: ").upper() #new variable to coincide with some product in the inventory
    if not inventory:
            print("Inventory is empty")
    
    found = False
    for name in inventory:
        if name['name'] == search_name : #
            print(f"Producto: {name['name']}")
            print(f"Price {name['price']}")
            print(f"Quantity: {name['quantity']}\n")
            found = True
            break
            
        
    if not found:
        print("Product is not in inventory")

def update_product(inventory):
    new_price = None
    new_quantity= None
    update_name = valid_text("Enter the product name: ").upper()
    found = False
    for update in inventory:
        if update['name'] == update_name:
            new_price = valid_positive_number("Ingrese nuevo precio: ")
            new_quantity = valid_positive_number("Ingrese nueva cantidad: ")
            update['price'] = new_price
            update['quantity'] = new_quantity

            print(f"Producto: {update['name']}")
            print(f"Price {update['price']}")
            print(f"Quantity: {update['quantity']}\n")
            print("Product updated successfully ")
            found = True
            break
            
    if not found:
            print("Product is not in inventory")

def delete_product(inventory):
     
     if not inventory:
            print("Inventory is empty")
     delete_name = valid_text("Enter the product name: ").upper()
     found = False
     for delete in inventory:
         if delete['name'] == delete_name:
            inventory.remove(delete)
            print("Product deleted successfully")
            found = True
            break
        
     if not found:
        print("Product is not in inventory")

def statistics(inventory):
    if not inventory:
            print("Inventory is empty")
    else:
        total_inventory = 0
        recording_products = 0
        
        for index in inventory:
            total_inventory += index['price'] * index['quantity']
            recording_products += index['quantity']
            max_stock = max(inventory, key=lambda index: index['quantity'])
            max_price = max(inventory, key=lambda index: index['price'])
        print("\n STATISTICS")
        print("-----------------------")
        print(f"Total inventory value: {total_inventory}")
        print(f"Total units: {recording_products}")
        print("\nProduct with highest stock:")
        print(f"Name: {max_stock['name']}")
        print(f"Quantity: {max_stock['quantity']}")
        print("\nMost expensive product:")
        print(f"Name: {max_price['name']}")
        print(f"Price: {max_price['price']}\n")

#VALIDATIONS
#function to allow only letters and not empty space
def valid_text(message):
    validate = True
    while validate:
        text = input(message).strip()
        
        # Verify if text has only alphabet
        if text.replace(" ", "").isalpha():
            validate = False
        
        else:
             print("ERROR! Name must only contain letters")
    return text

#This function is used to verify that a number cannot be negative
def valid_positive_number(message):
    validate = True
    while validate:
        try:
            data = int(input(message).strip())
            if  data <= 0:
                 print("\n The value cannot be negative")
            else:
                 validate=False 
                 return data
        
        except ValueError:
                print("\n The input is invalid")
    


             
        
     



                                    
      