from ordermanage import OrderManager

class UserMenu:
    def user_menu(self, user_id):
        order = OrderManager()
        choice = 0
        while choice != '4':
            print('''User Menu......
1. New Order
2. Delete Order
3. View Orders
4. Exit''')
            choice = input("Enter choice: ").strip()
            if choice == '1':
                order.new_order(user_id)      
            elif choice == '2':
                order.delete_order(user_id)
            elif choice == '3':
                order.view_orders(user_id)
            elif choice == '4':
                print("Thank you for ordering with us!") 
                break
            else:
                print("Invalid choice.")

