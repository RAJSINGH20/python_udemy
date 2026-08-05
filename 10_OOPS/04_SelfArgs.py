# Define a class representing a chai cup
class chaiCup:
    # Class attribute (shared by all objects)
    size = 150

    # Instance method to describe the cup
    def describe(self):
        return f"Cup size: {self.size} ml"


# Create the first object
cup = chaiCup()

# Call the instance method using the object
print(cup.describe())

# Call the instance method using the class (passing the object explicitly)
print(chaiCup.describe(cup))

# Create another object
cup_2 = chaiCup()

# Call the method for the second object
print(cup_2.describe())