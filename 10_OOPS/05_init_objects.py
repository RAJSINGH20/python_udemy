# Define a class to represent a chai order
class ChaiOrder:

    # Constructor to initialize the chai type and size
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    # Method to return the order summary
    def summary(self):
        return f"Order: {self.size} ml {self.type} Chai"


# Take chai size as input from the user
size = int(input("Enter size of chai in ml: "))

# Take chai type as input from the user
chaitype = input("Enter type of chai (e.g., masala, ginger, cardamom): ")

# Create an object of ChaiOrder
brewedchai = ChaiOrder(chaitype, size)

# Display the order summary
print(brewedchai.summary())