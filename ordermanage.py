from models import Order
from prettytable import PrettyTable


class OrderManager:
    def new_order(self, user_id):
        oid = input("🆔 Enter Order ID: ").strip()
        uid = input("👤 Enter User ID: ").strip()
        item_ids = input("📦 Enter Item ID: ").strip()
        
        try:
            with open("InventoryMS(Project)/orders.txt", "a") as fp:  # Append mode to add new order
                fp.write(f"{oid}, {uid}, {item_ids}\n")
            print("✅ Order added successfully.")
            print("\n📋 --- New Order Record ---")
            table = PrettyTable(["Order ID", "User ID", "Item ID"])
            table.add_row([oid, uid, item_ids])
            print(table)
        except Exception as e:
            print("❌ Error while adding order:", e)

    def delete_order(self, user_id):
        oid = input("🗑️ Enter Order ID to delete: ").strip()
        new_lines = []
        found = False
        deleted_order = []

        try:
            with open("InventoryMS(Project)/orders.txt", "r") as fp:
                for line in fp:
                    orderList = line.strip().split(", ")
                    if orderList[0] == oid:
                        found = True
                        deleted_order = orderList
                        continue
                    new_lines.append(line)
            if found:
                print("\n🗑️ --- Deleted Order Record ---")
                table = PrettyTable(["Order ID", "User ID", "Item ID"])
                table.add_row(deleted_order)
                print(table)

            with open("InventoryMS(Project)/orders.txt", "w") as fp:
                fp.writelines(new_lines)

            print("✅ Order deleted." if found else "❌ Order ID not found.")
        except FileNotFoundError as e:
            print("📁 File error:", e)
        except Exception as e:
            print("❌ Error:", e)

    def view_orders(self, user_id=None):
        try:
            with open("InventoryMS(Project)/orders.txt", "r") as fp:
                table = PrettyTable(["Order ID", "User ID", "Item ID"])
                found = False
                for line in fp:
                    orderList = line.strip().split(", ")
                    if len(orderList) != 3:
                        continue  # skip invalid rows
                    if user_id is None or orderList[1] == user_id:
                        table.add_row(orderList)
                        found = True

                if found:
                    if user_id is None:
                        print("\n📦 --- All Orders (Admin View) ---")
                    else:
                        print(f"\n📦 --- Your Orders (User ID: {user_id}) ---")
                    print(table)
                else:
                    if user_id is None:
                        print("📭 No orders found in the system.")
                    else:
                        print(f"📭 No orders found for User ID: {user_id}")
        except FileNotFoundError:
            print("📁 Order file not found.")

if __name__ == "__main__":  # Run directly
    order = OrderManager()
    order.new_order()
