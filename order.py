from product import Product
from buyer import Buyer


class Order(object):

    def __init__(self, buyer: Buyer):
        self.buyer = buyer
        self.cart = []
        self.quantities = []

    def add_product(self, product: Product, quantities: int | float):
        self.cart.append(product)
        self.quantities.append(quantities)

    def total_price(self):
        total = 0
        for i, item in enumerate(self.cart):
            total += item.price * self.quantities[i]
        return total



