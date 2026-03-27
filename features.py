# feature to add products to the inventory
inventory=[]
def add_productt(inventory):
    product_name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = {
        'name': product_name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product) #this adds a dictionary to list called inventory

add_productt(inventory) 
print(inventory)