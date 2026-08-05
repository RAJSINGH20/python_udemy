# Define a base class
class Chai:
    pass

# Define a derived class that inherits from Chai
class ChaiTime(Chai):
    pass

# Print the type of the class itself
print(type(Chai))

# Create an object of the Chai class
ginger_tea = Chai()

# Print the type of the object
print(type(ginger_tea))

# Check if the object's type is exactly Chai
print(type(ginger_tea) is Chai)

# Check if the object's type is ChaiTime (returns False)
print(type(ginger_tea) is ChaiTime)