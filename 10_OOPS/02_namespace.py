# Define a class with a class attribute
class Chai:
    origin = "India"

# Dynamically add a class attribute
Chai.is_hot = True

# Access class attributes directly
# print(Chai.origin)
# print(Chai.is_hot)

# Create an object of the Chai class
masala = Chai()

# Access class attributes through the object
print(masala.origin)
print(masala.is_hot)

# Create an instance attribute that overrides the class attribute
masala.is_hot = False

# The origin attribute is still inherited from the class
print(masala.origin)

# The instance attribute is used instead of the class attribute
print(masala.is_hot)