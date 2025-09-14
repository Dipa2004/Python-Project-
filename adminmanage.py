from models import User
from prettytable import PrettyTable

class UserManage():
    def addUser(self):
        uid = input("🆔 Enter User ID: ")
        name = input("📝 Enter User Name: ")
        e1 = User(uid, name)
        data = str(e1)
        try:
            with open("InventoryMS(Project)/users.txt", "a") as fp:
                fp.write(data + "\n")
            print("✅ User added successfully.") 
            print("\n📄 --- New User Record ---")
            table = PrettyTable(["User ID", "Name"])
            table.add_row([uid, name])
            print(table)
        except Exception as e:
            print("❌ Error while adding User:", e)  

    def updUser(self):
        allEmp = []
        uid = input("🔄 Enter User ID to update: ").strip()
        idchk = False
        try:
            with open("InventoryMS(Project)/users.txt", "r") as fp:
                for line in fp:
                    empList = line.strip().split(", ")
                    if empList[0] == uid:
                        idchk = True
                        print("\n📋 --- Current User Record ---")
                        table = PrettyTable(["User ID", "Name"])
                        table.add_row(empList)
                        print(table)
                        checkName = input("✏️ Do you want to update name (y/n)? ")
                        if checkName.lower() in ['yes', 'y']:
                            empList[1] = input("🆕 Enter new name: ").strip()
                        updated_line = ", ".join(empList)
                        allEmp.append(updated_line + '\n')
                    else:
                        allEmp.append(line)
            if idchk:
                with open("InventoryMS(Project)/users.txt", "w") as fp:
                    fp.writelines(allEmp)   
                print("✅ Data updated successfully.")  
            else:
                print("⚠️ User ID not found.")            
        except FileNotFoundError as e:
            print("📁 File error:", e)
        except Exception as e:
            print("❌ Error:", e)

    def delUser(self):
        uid = input("🗑️ Enter User ID to delete: ")
        new_lines = []
        found = False
        deleted_record = []

        try:
            with open("InventoryMS(Project)/users.txt", "r") as fp:
                for line in fp:
                    empList = line.strip().split(", ")
                    if empList[0] == uid:
                        found = True
                        deleted_record = empList
                        continue
                    new_lines.append(line)
            if found:
                print("\n🗂️ --- Deleted User Record ---")
                table = PrettyTable(["User ID", "Name"])
                table.add_row(deleted_record)
                print(table)        
            with open("InventoryMS(Project)/users.txt", "w") as fp:
                fp.writelines(new_lines)
            print("✅ User deleted." if found else "⚠️ User ID not found.")
        except FileNotFoundError as e:
            print("📁 File error:", e)
        except Exception as e:
            print("❌ Error:", e)

    def searchUser(self):
        uid = input("🔍 Enter User ID to search: ").strip()
        try:
            with open("InventoryMS(Project)/users.txt", "r") as fp:
                for line in fp:
                    empList = line.strip().split(", ")
                    if empList[0] == uid:
                        table = PrettyTable(['User ID', 'Name'])
                        table.add_row(empList)
                        print("✅ User Found:")
                        print(table)
                        return
                print("⚠️ User ID not found.")    
        except FileNotFoundError as e:
            print("📁 File Error:", e) 

    def showAllUser(self):
        try:
            with open("InventoryMS(Project)/users.txt", "r") as fp:
                table = PrettyTable(['User ID', 'Name'])
                found = False
                for line in fp:
                    found = True
                    empList = line.strip().split(", ")
                    table.add_row(empList)
                if found:
                    print("\n📋 ---- All Users ----") 
                    print(table)
                else:
                    print("🛑 No User found.")       
        except FileNotFoundError as e:
            print("📁 File Error:", e)
        except Exception as e:
            print("❌ Exception:", e)

if __name__ == "__main__":
    em1 = UserManage()
    em1.addUser()
    