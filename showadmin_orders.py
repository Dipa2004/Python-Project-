from ordermanage import OrderManager  # or wherever your class is

def admin_menu():
    order = OrderManager()
    while True:
        print('''\n--- Admin Menu ---
1. View All Orders
2. Exit''')
        choice = input("Enter choice: ")
        if choice == '1':
            order.view_orders()  # No user_id passed = show all orders
        elif choice == '2':
            print("🔙 Exiting Admin Menu.")
            break
        else:
            print("❌ Invalid choice.")

# Run it
admin_menu()
