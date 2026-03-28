from features import add_product, show_inventory, search_product, update_product, delete_product, statistics, valid_text, valid_positive_number
from files import save_csv, load_csv
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
    option = valid_positive_number("Select the option to enter: ") #While loop to repeat menu options once the user finishes some option
    if option == 1: #Add product
        status = "yes"
        while status == "yes": # while loop to add product if the user enters "yes" again
            
                add_product(inventory)
                
                status = input("Do you want to register another product? (yes/no): ")
                # while loop where the user must enters "yes" to continue or "no" to exit
                while status not in["yes", "no"]: 
                    print("ERROR! Only enter yes/no to continue")
                    status = input("Do you want to register another product? (yes/no): ")
    
    elif option == 2: #Show inventory
        if not inventory:
            print("\nInventory is empty\n")
            
        else:
            show_inventory(inventory)
    
    elif option == 3: #Search product 
         search_product(inventory)

    elif option == 4: #Update product
        update_product(inventory)
    
    elif option == 5: #Delete product
         delete_product(inventory)
    
    elif option == 6: #Statistics of inventory
         statistics(inventory)
    
    elif option == 7: #Save inventory in csv
        path = input("Enter file path: ")
        save_csv(inventory, path)
    
    elif option == 8: #load csv file
        path = input("Enter file path: ")
        data = load_csv(path)

        if data:
            status = input("Overwrite current inventory? (yes/no): ")
            

            while status not in ["yes", "no"]:
                status = input("ERROR! Only enter yes/no to continue: ")

            if status == "yes":
                inventory = data
                print("Replaced inventory")

            else:
                # FUSION
                for new in data:
                    found = False

                    for current in inventory:
                        if current['name'] == new['name']:
                            # Policy: Add quantity and update price
                            current['quantity'] += current['quantity']
                            current['price'] = new['price']
                            found = True
                            break

                    if not found:
                        inventory.append(new)

                print("Consolidated inventory (quantities totaled and prices updated))")

            print(f"Products uploaded: {len(data)}")
    elif option == 9: #exit of program
        print("Thank you very much for using our services")
        validate = False
    
    else: #if user enters option different to 1-9
        print("ERROR! Only enter the options below")


            
            
            
         
