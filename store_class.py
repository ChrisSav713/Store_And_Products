import product_class

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    # takes a product and adds it to the store
    def add_product(self, new_product):
        self.products.append(new_product)

    # remove the product from the store's list of products given the id 
    # (assume id is the index of the product in the list) and print its info.
    def sell_product(self, id):
        for product in self.products:
            if product.id == id:
                print("We have sold:")
                product.print_info()
                self.products.remove(product)
    
    # - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)

    #- updates all the products matching the given category by reducing the price by the percent_discount given 
    # (use the method you wrote in the Product class!)
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
