# creating a class Shoe with the following attributes of country, code, product, cost and quantity
class Shoes():

    # initialize the methods from the the class Shoes
    def __init__(self, country, code, product, cost, quantity):
       
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost 
        self.quantity = quantity

    # a function in the class Shoes where it will return the cost of the shoes
    def get_cost(self):
        return f"The cost of the shoes is R{self.cost}"

    # a function in the class Shoes where it will return the quantity of the shoes
    def get_quantity(self):
        return self.quantity

    # the function setQuantity takes in a parameter called quantity and adds it to the quantity attribute of the object
    def setQuantity(self, quantity):
        self.quantity += quantity

    # the function returns the code of the object
    def get_code(self):
        return self.code

    # returns a string representation of the class Shoes
    def __str__(self):
        return f"Country: {self.country}| Code: {self.code}| Product: {self.product}| Cost: {self.cost}| Quantity: {self.quantity}"

# an empty list used to store a list of shoe objects
shoe_list = []

# this function will read from the inventory.txt file and append objects into the shoe list 
def read_shoes_data():
    
    with open("inventory.txt", "r+") as f:
        f.readline()
        for line in f:
            line = line.strip("\n").split(",")
            country = line[0]
            code = line[1]
            product= line[2]
            cost = line[3]
            quantity = line[4]
            print(quantity)
            shoe = Shoes(country, code, product, cost, int(quantity))
            shoe_list.append(shoe)

# allow user to capture data about a shoe
def capture_shoes():
    shoe_country = input("What country is the shoe available in: ")
    shoe_code = input("Enter the shoe code(e.g SKU76000): ")
    brand_shoe = input("What brand of shoe is it? ")
    shoe_cost = input("Enter the price of the shoe: ")
    shoe_quantity = input("Enter the quanitity: ")
    
    shoe_obj = Shoes(shoe_country, shoe_code, brand_shoe, shoe_cost, shoe_quantity)
    shoe_list.append(shoe_obj)

# display the details of the shoe using a for loop
def view_all():
    for i in shoe_list:
        print(i)

# function will find the shoe with the lowest quantity for restock
# ask user for input if they want to add the quantity shoes
def restock():
    lowest_shoe = shoe_list[0]

    for shoeObject in shoe_list:
        if shoeObject.quantity <= lowest_shoe.quantity:
            lowest_shoe = shoeObject

    new_quantity = input("New Quantity: ")
    lowest_shoe.setQuantity(new_quantity)

# function that will search for a shoe and return the object
def search_shoe():
    shoe_obj = Shoes("SA", "12345", "ABC", "shoe_cost", "shoe_quantity")

    find_shoes = input("What shoe are you looking for? ")

    for shoe in shoe_list:
        if shoe.get_code == find_shoes:
            print(shoe_obj)
            break
        else:
            continue
        
# function will calculate the total value for each item
def value_per_item():
    for shoe in shoe_list[1:]:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"The stock value of {shoe} is: {value}")
                  
# determine the product with the highest quantity
# display the shoe for sale
def highest_quantity():
   
    highest_shoe = shoe_list[0]
    print(highest_shoe)

    for shoeObject in shoe_list:
        print(shoeObject)
        if shoeObject.get_quantity() >= highest_shoe.get_quantity():
            highest_shoe = shoeObject
        else:
            continue

    print(f"This shoe is for sale!")
    print(highest_shoe)


# main menu that executes each function above using a while loop
while True:
    menu = input("\n"'''Select one of the following Options below:
    rsd - Read shoes data
    caps - Capture shoes
    va - View all 
    rs - Restock
    ss - Search shoe
    vpi - Value per item 
    hq - Highest quantity
    : ''').lower()

    if menu == "rsd":
        read_shoes_data()

    if menu == "caps":
        capture_shoes()

    elif menu == "va":
        view_all()

    elif menu == "rs":
        restock()

    elif menu == "ss":
        search_shoe()

    elif menu == "vpi":
        value_per_item()

    elif menu == "hq":
        highest_quantity()

    else:
        print("Going back to main menu.")
