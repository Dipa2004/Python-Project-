from adminmanage import UserManage
from inventorymanage import InventoryManage
from staffmanage import StaffManage

s1 = StaffManage()
p1 = InventoryManage()
em1 = UserManage()

class Admin:

    def admin_menu(self): 
        em1 = UserManage()
        p1 = InventoryManage()
        s1 = StaffManage()
        choice = 0
        while(choice != '4'):
            print('''\nPlease select option:
            1. User Management
            2. Inventory Management
            3. Staff Management
            4. Exit''')

            choice = input("Enter choice: ")
            if(choice == '1'):
                print('''\n--- User Management ---
                1. Add User
                2. Update User
                3. Delete User
                4. Search User
                5. Show All User
                6. Back to Main Menu''')
                ch1 = input("Enter choice: ")
                if(ch1 == '1'): 
                    em1.addUser()
                elif(ch1 == '2'): 
                    em1.updUser()
                elif(ch1 == '3'): 
                    em1.delUser()
                elif(ch1 == '4'): 
                    em1.searchUser()
                elif(ch1 == '5'): 
                    em1.showAllUser()
                else: 
                    print("Back to menu.")

            elif(choice == '2'):
                print('''\n--- Inventory Management ---
                1. Add Item
                2. Update Item
                3. Delete Item
                4. Search Item
                5. Show All Items
                6. Back to Main Menu''')
                ch2 = input("Enter choice: ")
                if(ch2 == '1'): 
                    p1.addItem()
                elif(ch2 == '2'): 
                    p1.updItem()
                elif(ch2 == '3'): 
                    p1.delItem()
                elif(ch2 == '4'): 
                    p1.searchItem()
                elif(ch2 == '5'): 
                    p1.showAllitems()
                else: 
                    print("Back to menu.")

            elif(choice == '3'):
                print('''\n--- Staff Management ---
                1. Add Staff
                2. Update Staff
                3. Delete Staff
                4. Search Staff
                5. Show All Staff
                6. Back to Main Menu''')
                ch3 = input("Enter choice: ")
                if(ch3 == '1'): 
                    s1.addStaff()
                elif(ch3 == '2'): 
                    s1.updStaff()
                elif(ch3 == '3'): 
                    s1.delStaff()
                elif(ch3 == '4'): 
                    s1.searchStaff()
                elif(ch3 == '5'): 
                    s1.showAllStaff()
                else: 
                    print("Back to menu.") 

            elif(choice == '4'):
                print("Exiting Admin Menu.")
            else:
                print("Invalid main menu choice.")       