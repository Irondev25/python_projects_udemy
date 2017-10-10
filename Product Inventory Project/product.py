# a simple shop inventory
import shelve

class product:
    # initilization method
    def __init__(self, id, name, price, quantity):
        self.id = str(id)
        self.name = name
        self.price = (price)
        self.quantity = quantity

    #getter methods
    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def changePrice(self, newPrice):
        self.price = newPrice

    def changeQuantity(self, newQuantity):
        self.quantity = str(int(self.quantity) + int(newQuantity))

    def showIndividualProduct(self, key):
        print("Current Product Status: ")
        print(str(self.getId()) + '\n' + str(self.getPrice()) + '\n' + str(self.getQuantity()) + '\n' + str(
            self.getName()))


class inventory(product):
    def showProduct(self):
        print("\n")
        print("ID: " + str(self.getId()) + '\n' +
              "Name: " + str(self.getName()) + '\n' +
              "Price: " + str(self.getPrice()) + '\n' +
              "Quantity: " + str(self.getQuantity()))
        print("\n")

    def totalValueOfProduct(self):
        sum = 0
        ProductDatabase = shelve.open('database')
        for key in ProductDatabase:
            sum = sum + int(ProductDatabase[key].getPrice()) * int(ProductDatabase[key].getQuantity())
        ProductDatabase.close()
        return sum


def sellAProduct(ID):
    db = shelve.open('database')
    productSell = db[ID]
    productSell.changeQuantity(-1)
    db[ID] = productSell
    db.close()


def startInvertory():
    print("Menu: ")
    print("1. Show all Poduct. ")
    print("2. Sell a product")
    print("3. Add a Product")
    print("4. Total value of the Products")
    print("5. Update Price")
    print("6. Update Quantity")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        db = shelve.open('database')
        for key in db:
            db[key].showProduct()
        db.close()
    elif choice == 2:
        productSellID = input("Enter Product ID: ")
        sellAProduct(productSellID)
    elif choice == 3:
        choiceProduct = 'y'
        while choiceProduct == 'y' or choiceProduct == 'Y':
            ID = input("Enter new product id: ")
            Name = input("Enter name of the product: ")
            Price = input("Enter price of the product: ")
            Quatity = input("Enter Quatity of the product: ")
            newProduct = inventory(ID, Name, Price, Quatity)
            db = shelve.open('database')
            db[newProduct.getId()] = newProduct
            db.close()
            choiceProduct = input("Do you want to add another product(y/n)")
    elif choice == 4:
        totalWorth = inventory.totalValueOfProduct(inventory)
        print(totalWorth)
    elif choice == 5:
        db = shelve.open('database')
        key = str(input("Enter the ID of The product: "))
        currentProduct = db[key]
        print("Current  price is " + str(currentProduct.getPrice()))
        newPrice = input("Enter new Price. ")
        currentProduct.changePrice(newPrice)
        currentProduct.showIndividualProduct(key)
        db[key] = currentProduct
        db.close()
    elif choice == 6:
        db = shelve.open('database')
        key = str(input("Enter the ID of The product: "))
        currentProduct = db[key]
        print("Current stock: " + str(currentProduct.getQuantity()))
        newStock = input("How much stock do you want to stock:")
        currentProduct.changeQuantity(newStock)
        currentProduct.showIndividualProduct(key)
        db[key] = currentProduct
        db.close()


mainChoice = 'y'
while mainChoice == 'y' or mainChoice == 'Y':
    startInvertory()
    mainChoice = input("Go Back(y/n)")
