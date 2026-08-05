# Base class for all chai types
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai")


# Derived class
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding masala spices to the chai")


# Shop class
class Shop:
    # Store the class, not an object
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Masala")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


# Fancy shop uses MasalaChai instead of BaseChai
class FancyChaiShop(Shop):
    chai_cls = MasalaChai


# Create shop objects
shop = Shop()
fancy = FancyChaiShop()

# Serve chai
shop.serve()
fancy.serve()

# Add extra spices in the fancy shop
fancy.chai.add_spices()