"""
this is a ptractice run on the topic oop(Oject Oriented Programs)
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default attribute value

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
           self.odometer_reading += miles


# tis create an instances of the car class
"""
my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_descriptive_name())  # Output: 2020 Toyota Camry

my_car.read_odometer()  # Output: This car has 0 miles on it.
my_car.update_odometer(100)  # Update odometer reading
my_car.read_odometer()  # Output: This car has 100 miles on it.

my_car.increment_odometer(50)  # Increment odometer reading
my_car.read_odometer()  # Output: This car has 150 miles on it.

"""




class student:
    def __init__(self,name,age):
        self.name = name # this stores the name of a speific student
        self.age = age   # stores the age
    
     # method to display student info
    def student_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# create student using class
student_1 = student("Ruth", 24)
student_1.student_info() 
student_2 = student("Abamiyo", 28)
student_2.student_info() 
pass


# creating product catalog
class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def total_value(self):
        return self.price * self.quantity
    

product1 = product("Laptop", 1000, 5)
product2 = product("Mouse", 20, 10)

print(product1.total_value())  
print(product2.total_value())




# Exception handling
# Custom exceptions

class OutOfStockError(Exception):
    """Custom exception for handling out-of-stock items."""

    def __init__(self, item_name):
        self.item_name = item_name

    def __str__(self):
        return f"Sorry, the item '{self.item_name}' is out of stock."

# Sample Product Inventory
product_inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 0,  # Out of stock
    "grapes": 3
}

def purchase_item(item, quantity):
    try:
        if product_inventory[item] == 0:
            raise OutOfStockError(item)
        else:
            print(f"Purchase successful: {quantity} {item}(s)")
            product_inventory[item] -= quantity
    except KeyError:
        print(f"Sorry, '{item}' is not available in our inventory.")

# Testing the Custom Exception
try:
    purchase_item("apple", 3)  # Purchase successful
    purchase_item("orange", 1)  # Raises OutOfStockError
    purchase_item("watermelon", 1)  # Item not available
except OutOfStockError as e:
    print(e)  # Output:


