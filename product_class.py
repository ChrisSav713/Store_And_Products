import random

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.id = random.randrange(100000, 199999)
        self.price = price
        self.category = category

    # def new_id(self):
    #     unique = False
    #     new_id = 0
    #     while unique == False:
    #         new_id = random.randrange(100000, 199999)
    #         unique = True
    #         for product in self.products:
    #             if product.id == new_id:
    #                 unique = False
    #     return new_id

    # - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. 
    #   If False, the price should decrease by the percent_change provided.    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= 1 + (percent_change / 100)
        else:
            self.price *= 1 - (percent_change / 100)
    
    # - print the name of the product, its category, and its price.
    def print_info(self):
        print(f'''Product Name: {self.name:<25} Category: {self.category:<25} Price: {round(self.price,2):<25} ID: {self.id}''')