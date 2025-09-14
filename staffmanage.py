from models import Staff
from prettytable import PrettyTable

class StaffManage():
    from prettytable import PrettyTable

    def addStaff(self):
        try:
            sid = input("🆔 Enter Staff ID: ").strip()
            name = input("👤 Enter Name: ").strip()
            address = input("🏠 Enter Address: ").strip()
            adhar = input("🪪 Enter Adhar Number: ").strip()
            phone = input("📞 Enter Phone Number: ").strip()

            staff_data = [sid, name, address, adhar, phone]

            with open("InventoryMS(Project)/staff.txt", "a") as fp:
                fp.write(", ".join(staff_data) + "\n")

            print("✅ Staff added successfully.\n")

            print("📋 --- New Staff Record ---")
            table = PrettyTable(["🆔 Staff ID", "👤 Name", "🏠 Address", "🪪 Adhar Number", "📞 Phone Number"])
            table.add_row(staff_data)
            print(table)

        except Exception as e:
            print("❌ Error while adding employee:", e)


    def updStaff(self):
        allStaff = []
        sid = input("🔄 Enter Staff ID to update: ").strip()
        idchk = False
        try:
            with open("InventoryMS(Project)/staff.txt", "r") as fp:
                for line in fp:
                    Stafflist = line.strip().split(", ")
                    if Stafflist[0] == sid:
                        idchk = True
                        print("\n📋 --- Current Staff Record ---")
                        table = PrettyTable(["🆔 Staff ID", "👤 Name", "🏠 Address", "🪪 Adhar No.", "📞 Phone No."])
                        table.add_row(Stafflist)
                        print(table)
                        checkname = input("✏️ Do you want to update the 👤 name (y/n): ")
                        if checkname.lower() in ['yes', 'y']:
                            Stafflist[1] = input("👤 Enter new name: ")

                        checkname = input("✏️ Do you want to update the 🏠 address (y/n): ")
                        if checkname.lower() in ['yes', 'y']:
                            Stafflist[2] = input("🏠 Enter new address: ")

                        checkname = input("✏️ Do you want to update the 🪪 Adhar No. (y/n): ")
                        if checkname.lower() in ['yes', 'y']:
                            Stafflist[3] = input("🪪 Enter new Adhar No.: ")

                        checkname = input("✏️ Do you want to update the 📞 Phone No. (y/n): ")
                        if checkname.lower() in ['yes', 'y']:
                            Stafflist[4] = input("📞 Enter new Phone No.: ")

                        update_staff = ", ".join(Stafflist)
                        allStaff.append(update_staff + '\n')
                    else:
                        allStaff.append(line)

            if idchk:
                with open("InventoryMS(Project)/staff.txt", "w") as fp:
                    fp.writelines(allStaff)
                print("✅ Staff updated successfully.")
            else:
                print("❌ Staff ID not found.")

        except FileNotFoundError as e:
            print("📁 File error:", e)
        except Exception as e:
            print("❌ Error:", e)

    def delStaff(self):
        sid = input("🗑️ Enter Staff ID to delete: ").strip()
        new_staff = []
        found = False
        deleted_staff = []

        try:
            with open("InventoryMS(Project)/staff.txt", "r") as fp:
                for line in fp:
                    Stafflist = line.strip().split(", ")
                    if Stafflist[0] == sid:
                        found = True
                        deleted_staff = Stafflist
                        continue
                    new_staff.append(line)
            if found:
                print("\n🗑️ --- Deleted Staff Record ---")
                table = PrettyTable(["Staff ID", "Name", "Address", "Adhar_no.", "Phone_no."])
                table.add_row(deleted_staff)
                print(table)
            with open("InventoryMS(Project)/staff.txt", "w") as fp:
                fp.writelines(new_staff)
            print("✅ Staff deleted." if found else "❌ Staff ID not found.")
        except FileNotFoundError as e:
            print("📁 File error:", e)
        except Exception as e:
            print("❌ Error:", e)

    def searchStaff(self):
        sid = input("🔍 Enter Staff ID to search: ").strip()
        try:
            with open("InventoryMS(Project)/staff.txt", "r") as fp:
                for record in fp:
                    Stafflist = record.strip().split(", ")
                    if Stafflist[0] == sid:
                        table = PrettyTable(["Staff ID", "Name", "Address", "Adhar_no.", "Phone_no."])
                        table.add_row(Stafflist)
                        print("✅ Staff found.")
                        print(table)
                        return
                print("❌ Staff ID not found.")
        except FileNotFoundError as e:
            print("📁 File Error:", e)

    def showAllStaff(self):
        try:
            with open("InventoryMS(Project)/staff.txt", "r") as fp:
                table = PrettyTable(["Staff ID", "Name", "Address", "Adhar_no.", "Phone_no."])
                found = False
                for line in fp:
                    found = True
                    Stafflist = line.strip().split(", ")
                    table.add_row(Stafflist)
                if found:
                    print("\n📋 --- All Staff ---") 
                    print(table)
                else:
                    print("📭 No staff found.")
        except FileNotFoundError as e:
            print("📁 File Error:", e)
        except Exception as e:
            print("❌ Exception:", e)

if __name__ == "__main__":
    staff1 = StaffManage()
    staff1.addStaff()
    staff1.updStaff()
    # staff1.delStaff()
    # staff1.searchStaff()
    # staff1.showAllStaff()