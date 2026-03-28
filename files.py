import csv
#CRUD METHOD
def save_csv(inventory, path, include_header=True):
    if not inventory:
        print("Inventory is empty. Nothing to save.")
        

    
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if include_header: #write in csv 3 header
            writer.writerow(['name', 'price', 'quantity'])

        for data in inventory:
            writer.writerow([
                data['name'],
                data['price'],
                data['quantity']
            ])

    print(f"Inventory stored in: {path}")

    

def load_csv(path):
    inventory_uploaded = [] #new inventory
    errors = 0

    try:
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)

            # validate header
            if header != ['name', 'price', 'quantity']:
                print("Incorrect header. It should be: name, price, quantity")
                return []

            for row in reader:
                if len(row) != 3:
                    errors += 1
                    continue

                name, price, quantity = row

                try:
                    price = float(price)
                    quantity = int(quantity)

                    if price < 0 or quantity < 0:
                        raise ValueError

                    inventory_uploaded.append({
                        'name': name,
                        'price': price,
                        'quantity': quantity
                    })

                except ValueError:
                    errors += 1

        print(f"File uploaded successfully")
        print(f"{errors} Invalid rows omitted")

        return inventory_uploaded

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except UnicodeDecodeError:
        print("Error: File encoding issue.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return []