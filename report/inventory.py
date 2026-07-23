class Inventory:
    def __init__(self,products):
        self.products

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration 
        
        product = self.products[self.index]
        self.index += 1

        return product
    
    def inventory_generator(products):

# Context Manager
class InventoryReport:
    def __init__(self, filename):
        self.filename = filename

        def __enter__(self):
            self.file = open(self.filename,"w")
            return self.file
        
        def __exit__(self,exc_type,exc_val,exc_tb):
            self.file.close()
            