import pickle
import bcrypt
from admin import Admin
from user import UserMenu

def load_users():
    try:
        with open("InventoryMS(Project)/users.pkl", "rb") as fp:
            return pickle.load(fp)
    except FileNotFoundError:
        print("User credentials file not found.")
        return {}
    
def save_users(users):
    with open("InventoryMS(Project)/users.pkl", "wb") as fp:
        pickle.dump(users, fp)

def verify_password(stored_hash, input_password):
    return bcrypt.checkpw(input_password.encode(), stored_hash) #converts the string into a byte format because 
                                                                #bcrypt works with bytes, not strings.

def register_user(users):
    username = input("Enter your username: ")
    if username in users:
        print("Username alredy exists!")
        return users
    password = input("Enter password: ").strip()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) #gensalt:genrate random
    users[username] = hashed_pw
    save_users(users)
    print(f"User '{username}' registered successfully!")
    return users

def change_password(users):
    username = input("Enter your username: ")
    if username not in users:
        print("User does not exist!")
        return users
    current_pass = input("Enter current password: ").strip()
    if not verify_password(users[username], current_pass):
        print("Incorrect current password.")
        return users
    new_pass = input("Enter new password: ").strip()
    confirm_pass = input("Confirm new password: ").strip()
    if new_pass != confirm_pass:
        print("Passwords do not match.")
        return users
    users[username] = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt())
    save_users(users)
    print("Password changed successfully.")
    return users

def main():
    users = load_users()
    ch = 0
    while(ch != '5'):
        print('''
============================================
   📦 WELCOME TO INVENTORY MANAGEMENT SYSTEM
============================================
        1️⃣ Admin Login
        2️⃣ User Login
        3️⃣ Register User
        4️⃣ Change Password
        5️⃣ Exit''')

        ch = input("🔸 Enter choice: ").strip()

        if(ch == '1'):
            uname = input("👤 Enter username: ").strip()
            passw = input("🔒 Enter password: ").strip()
            if uname in users and verify_password(users[uname], passw) and uname == "admin":
                print("✅ Welcome admin! 👑")
                Admin().admin_menu()
            else:
                print("❌ Invalid credentials. Please try again.")

        elif(ch == '2'):
            uname = input("👤 Enter username: ").strip()
            passw = input("🔒 Enter password: ").strip()
            if uname in users and verify_password(users[uname], passw):
                print("✅ Welcome user.. ")
                UserMenu().user_menu(uname)
            else:
                print("❌ Invalid credentials. Please try again.")

        elif(ch == '3'):
            users = register_user(users)

        elif(ch == '4'):
            users = change_password(users)
            
        elif(ch == '5'):
            print("👋 Thank you for visiting! Have a great day! 🌟")
            break
        else:
            print("⚠️ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()