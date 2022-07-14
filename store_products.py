import random
import product_class, store_class

"""
Start of main program...
"""

my_store = store_class.Store("Groceries")
my_store.products = [
product_class.Product("Apple", 1.00, "Fruit"),    
product_class.Product("Bananas", 1.30, "Fruit"),    
product_class.Product("Pear", 1.50, "Fruit"),    
product_class.Product("Broccoli", .99, "Vegetable"),    
product_class.Product("Lettuce", 1.00, "Vegetable"),    
product_class.Product("Pepper", 1.20, "Vegetable"),    
product_class.Product("Onion", .80, "Vegetable"),    
product_class.Product("Milk", 1.80, "Dairy"),    
product_class.Product("Cheddar", 2.30, "Dairy"),    
product_class.Product("Yogurt", 3.00, "Dairy") 
]

print("\n***Inventory list")
for product in my_store.products:
    product.print_info()

print("\n***Selling Lettuce")
my_store.sell_product(my_store.products[4].id)

print("\n***New inventory list")
for product in my_store.products:
    product.print_info()

print("\n***Adding Tomatoes")
my_store.add_product(product_class.Product("Tomatoes", .80, "Fruit"))

print("\n***New Inventory list")
for product in my_store.products:
    product.print_info()

print("\n***Inflation 5%")
my_store.inflation(5)

print("\n***New Inventory list")
for product in my_store.products:
    product.print_info()

print("\n***Clearance on fruit 15%")
my_store.set_clearance("Fruit", 15)

print("\n***New Inventory list")
for product in my_store.products:
    product.print_info()