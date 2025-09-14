class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def __str__(self):
        return f'{self.uid}, {self.name}'     

class InventoryItem:
    def __init__(self, iid, name, quantity, price):
        self.iid = iid
        self.name =  name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f'{self.iid}, {self.name}, {self.quantity}, {self.price}' 

class Staff:
    def __init__(self, sid, name, add, adhar_no, phone_no):
        self.sid = sid
        self.name = name
        self.add = add
        self.adhar = adhar_no
        self.phone = phone_no

    def __str__(self):
        return f'{self.sid}, {self.name}, {self.add}, {self.adhar}, {self.phone}'

class Order:
    def __init__(self, oid, uid, item_ids):
        self.oid = oid
        self.uid = uid
        self.item_ids = item_ids

    def __str__(self):
        return f'Order ID: {self.oid}\nUser ID: {self.uid}\nItem ID: {self.item_ids}'                