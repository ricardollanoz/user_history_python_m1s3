# inventory = []
# product_name = input("Product name: ")
# price = float(input("Price: "))
# quantity = int(input("Quantity: "))
# # A dictionary is created to storage variables
# product = {
#     'name': product_name,
#     'price': price,
#     'quantity': quantity
# }
# inventory.append(product)

# product_namee = input("Enter the product name: ")
# for name in inventory:
#         if name['name'] == product_namee :
#             print(f"Producto: {name['name']}")
#             print(f"Price {name['price']}")
#             print(f"Quantity: {name['quantity']}\n")

inventory = [{
    'name' : 'pan',
    'price': 200,
    'quantity': 2
}]
variable = input("d")
new_price = float(input("e"))
for data in inventory:
    if data['name'] == variable:
        data['price'] = new_price
print(inventory)

