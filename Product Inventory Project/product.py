class product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def getId(self):
        return id

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def changePrice(self, newPrice):
        self.price = newPrice

    def changeQuantity(self, newQuantity):
        self.quantity += newQuantity
