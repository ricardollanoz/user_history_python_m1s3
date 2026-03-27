from features import add_product

inventory=[]

print("********** Welcome **************\n")
print("******* Options Menu ***********")
print("[1] Add product")
print("[2] Show inventory")
print("[3] Search product in stock")
print("[4] Update product")
print("[5] Delete product record")
print("[6] Statistics")
print("[7] Save CSV")
print("[8] Load CSV")
print("[9] Exit")
option = int(input("Select the option to enter: "))
validate = True
while validate:
    if option == 1:
        add_product(inventory)
        





