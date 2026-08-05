# Define a class with class attributes
class chai:
    temp = "hot"
    strength = "strong"


# Create an object
cutting = chai()

# Access the class attribute through the object
print(cutting.temp)

# Create an instance attribute (overrides the class attribute)
cutting.temp = "cold"
print(cutting.temp)

# Access the class attribute directly
print(chai.temp)

# Delete the instance attribute
del cutting.temp

# Falls back to the class attribute after deletion
print(cutting.temp)