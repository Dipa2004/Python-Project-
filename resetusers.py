# create_users.py
import bcrypt
import pickle

def save_users():
    users = {
        "admin": bcrypt.hashpw("admin1234".encode(), bcrypt.gensalt()),
        "Dipali": bcrypt.hashpw("user123".encode(), bcrypt.gensalt())
    }
    with open("InventoryMS(Project)/users.pkl", "wb") as fp:
        pickle.dump(users, fp)

save_users()