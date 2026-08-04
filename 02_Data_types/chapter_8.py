# ==============================
# Python List Operations Example
# ==============================

# Create a list of ingredients
ingredients = ["flour", "sugar", "eggs", "milk"]

# Add a new ingredient to the end of the list
ingredients.append("butter")

print("After append:")
print(ingredients)

# Remove a specific ingredient from the list
ingredients.remove("sugar")

print("\nAfter removing sugar:")
print(ingredients)


# =====================================
# Working with Chai Ingredient Lists
# =====================================

# List of spices
spice_options = ["cumin", "turmeric", "coriander"]

# Basic chai ingredients
chai_ingredients = ["tea leaves", "water", "milk", "sugar"]

# Add all spices to the chai ingredient list
chai_ingredients.extend(spice_options)

print("\nAfter extending spices:")
print(chai_ingredients)

# Insert ginger at index position 2
chai_ingredients.insert(2, "ginger")

print("\nAfter inserting ginger:")
print(chai_ingredients)

# Remove and store the last item from the list
last_ingredient = chai_ingredients.pop()

print(f"\nRemoved ingredient: {last_ingredient}")

# Reverse the order of elements in the list
chai_ingredients.reverse()

print("\nAfter reversing:")
print(chai_ingredients)

# Sort the list alphabetically
chai_ingredients.sort()

print("\nAfter sorting:")
print(chai_ingredients)


# =====================================
# Finding Maximum and Minimum Values
# =====================================

# Sugar level values
sugar_levels = [1, 2, 3, 4, 5]

# Find highest and lowest sugar levels
print(f"\nMaximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")


# =====================================
# Operator Overloading with Lists
# =====================================

# Base liquids for chai
base_liquid = ["water", "milk"]

# Additional flavor
extra_flavor = ["ginger"]

# Combine two lists using '+' operator
full_liquid_mix = base_liquid + extra_flavor

print("\nFull liquid mix:")
print(full_liquid_mix)

# Repeat list elements using '*' operator
strong_brew = ["black tea"] * 3

print("\nStrong brew:")
print(strong_brew)


# =====================================
# Bytearray Example
# =====================================

# Create a bytearray object
raw_spice_data = bytearray(b"cinamon")

print("\nOriginal bytearray:")
print(raw_spice_data)

# Replace part of the byte sequence
new_raw_spice_data = raw_spice_data.replace(b"cina", b"cardi")

print("\nUpdated bytearray:")
print(new_raw_spice_data)