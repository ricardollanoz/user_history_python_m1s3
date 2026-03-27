from features import add_product, show_inventory, search_product
#List to store dictionaries
inventory=[]

print("********** Welcome **************")
validate = True
while validate:
    
    print("******** Menu options ***********")
    print("[1] Add product")
    print("[2] Show inventory")
    print("[3] Search product in stock")
    print("[4] Update product")
    print("[5] Delete product record")
    print("[6] Statistics")
    print("[7] Save CSV")
    print("[8] Load CSV")
    print("[9] Exit")
    option = int(input("Select the option to enter: ")) #While loop to repeat menu options once the user finishes some option
    if option == 1:
        status = "yes"
        while status == "yes": # while loop to add product if the user enters "yes" again
            
                add_product(inventory)
                
                status = input("Do you want to register another product? (yes/no): ")
                # while loop where the user must enters "yes" to continue or "no" to exit
                while status not in["yes", "no"]: 
                    print("ERROR! Only enter yes/no to continue")
                    status = input("Do you want to register another product? (yes/no): ")
    elif option == 2:
        if not inventory:
            print("\nInventory is empty\n")
            
        else:
            show_inventory(inventory)
    elif option == 3:
         search_product(inventory)
         

