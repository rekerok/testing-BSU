class Item:
    def __init__(self, name="", price=""):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_name(self, new_name):
        self.name = new_name

    def set_price(self, new_price):
        self.price = new_price
