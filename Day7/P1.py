class ProductRegistry:
    def __init__(self):
        self.products = {}

    def register_product(self, product_id, product_name):
        self.products[product_id] = product_name

    def get_product(self, product_id):
        return self.products.get(product_id, "Product not found")