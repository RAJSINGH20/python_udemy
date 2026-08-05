# Define a class to represent a tea leaf
class TeaLeaf:

    # Initialize the tea leaf with an age
    def __init__(self, age):
        self._age = age

    # Getter method using @property
    @property
    def age(self):
        return self._age + 2

    # Setter method with validation
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf does not satisfy the condition")


# Create a TeaLeaf object
leaf = TeaLeaf(2)

# Access the age property
print(leaf.age)

# Update the age using the setter
leaf.age = 4

# Access the updated age property
print(leaf.age)