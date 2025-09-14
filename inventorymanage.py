from models import InventoryItem
from prettytable import PrettyTable

class InventoryManage():
    def addItem(self):
        iid = input("🆔 Enter Item ID: ")
        name = input("📦 Enter Product Name: ")
        qty = input("🔢 Enter Quantity: ")
        price = float(input("💰 Enter Price: "))
        p1 = InventoryItem(iid, name, qty, price)
        allData = str(p1)
        try:
            with open("InventoryMS(Project)/inventory.txt", "a") as fp:
                fp.write(allData + "\n")
            print("✅ Product added successfully.")
            print("\n📋 --- New Product Record ---")
            table = PrettyTable(["Item ID", "Name", "Quantity", "Price"])
            table.add_row([iid, name, qty, price])
            print(table)
        except Exception as e:
            print("❌ Error while adding product:", e)

    def updItem(self):
        allProduct = []
        iid = input("🔍 Enter Item ID to update: ").strip()
        idchk = False
        try:
            with open("InventoryMS(Project)/inventory.txt", "r") as fp:
                for record in fp:
                    pList = record.strip().split(", ")
                    if pList[0] == iid:
                        idchk = True
                        print("\n📋 --- Current Product Record ---")
                        table = PrettyTable(["Item ID", "Name", "Quantity", "Price"])
                        table.add_row(pList)
                        print(table)

                        chk = input("✏️ Do you want to change the name (y/n): ")
                        if chk.lower() in ['y', 'yes']:
                            pList[1] = input("🔢 Enter new name: ")

                        chk = input("✏️ Do you want to change the quantity (y/n): ")
                        if chk.lower() in ['y', 'yes']:
                            pList[2] = input("📦 Enter new quantity: ")

                        chk = input("✏️ Do you want to change the price (y/n): ")
                        if chk.lower() in ['y', 'yes']:
                            pList[3] = str(float(input("💰 Enter new price: "))) + '\n'

                        record = ", ".join(pList)
                        allProduct.append(record)
                    else:
                        allProduct.append(record)

        except FileNotFoundError:
            print("📁 Error: inventory.txt file not found.")
        except Exception as e:
            print("❌ Error:", e)
        else:
            if idchk:
                with open("InventoryMS(Project)/inventory.txt", "w") as fp:
                    for record in allProduct:
                        fp.write(record)
                print("✅ Data updated successfully.")
            else:
                print("❌ Item ID not found.")

    def delItem(self):
        iid = input("🗑️ Enter Item ID to delete: ")
        new_product = []
        found = False
        deleted_record = []

        try:
            with open("InventoryMS(Project)/inventory.txt", "r") as fp:
                for product in fp:
                    pList = product.strip().split(", ")
                    if pList[0] == iid:
                        found = True
                        deleted_record = pList
                        continue
                    new_product.append(product)
            if found:
                print("\n🗑️ --- Deleted Product Record ---")
                table = PrettyTable(["Item ID", "Name", "Quantity", "Price"])
                table.add_row(deleted_record)
                print(table)

            with open("InventoryMS(Project)/inventory.txt", "w") as fp:
                fp.writelines(new_product)

            print("✅ Product deleted." if found else "❌ Product ID not found.")
        except FileNotFoundError as e:
            print("📁 File error:", e)
        except Exception as e:
            print("❌ Error:", e)

    def searchItem(self):
        iid = input("🔍 Enter Product ID to search: ").strip()
        try:
            with open("InventoryMS(Project)/inventory.txt", "r") as fp:
                for line in fp:
                    pList = line.strip().split(", ")
                    if pList[0] == iid:
                        table = PrettyTable(["Item ID", "Name", "Quantity", "Price"])
                        table.add_row(pList)
                        print("✅ Product Found:")
                        print(table)
                        return
                print("❌ Product ID not found.")
        except FileNotFoundError as e:
            print("📁 File Error:", e)

    def showAllitems(self):
        try:
            with open("InventoryMS(Project)/inventory.txt", "r") as fp:
                table = PrettyTable(["Item ID", "Name", "Quantity", "Price"])
                found = False
                for line in fp:
                    item = line.strip().split(", ")
                    if len(item) != 4:
                        print(f"⚠️ Skipping bad row: {line.strip()}")
                        continue
                    table.add_row(item)
                    found = True
                if found:
                    print("\n📦 --- All Inventory Items ---")
                    print(table)
                else:
                    print("📭 No items found.")
        except FileNotFoundError:
            print("📁 Items file not found.")
        except Exception as e:
            print(f"❌ Exception: {e}")


if __name__ == "__main__":
    product1 = InventoryManage()
    # product1.addItem()
    # product1.updItem()
    # product1.delItem()
