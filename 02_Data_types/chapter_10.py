# =====================================
# Python Dictionary Operations Example
# =====================================

# Create a dictionary using dict()
chai_order = dict(type="masala chai", size="large", sugar=2)

print("Chai Order:")
print(chai_order)


# -------------------------------------
# Creating an Empty Dictionary
# -------------------------------------
chai_recipe = {}

# Add key-value pairs
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk tea"

# Access dictionary values
print("\nBase:", chai_recipe["base"])
print("Liquid:", chai_recipe["liquid"])


# -------------------------------------
# Delete a Key
# -------------------------------------
del chai_recipe["liquid"]

# print(chai_recipe["liquid"])  # Would raise KeyError


# -------------------------------------
# Membership Test
# -------------------------------------
print("\nIs 'sugar' in order?", "sugar" in chai_order)


# -------------------------------------
# Create Another Dictionary
# -------------------------------------
chai_order = dict(type="ginger chai", size="large", sugar=2)

# Display keys, values, and items
print("\nOrder Keys:")
print(chai_order.keys())

print("\nOrder Values:")
print(chai_order.values())

print("\nOrder Items:")
print(chai_order.items())


# -------------------------------------
# Remove Last Inserted Item
# -------------------------------------
last_item = chai_order.popitem()

print("\nRemoved Last Item:")
print(last_item)


# -------------------------------------
# Update Dictionary
# -------------------------------------
extra_spices = {
    "spice1": "cardamom",
    "spice2": "ginger",
    "spice3": "turmeric"
}

chai_recipe.update(extra_spices)

print("\nUpdated Recipe:")
print(chai_recipe)


# -------------------------------------
# Access Dictionary Value
# -------------------------------------
size = chai_order["size"]

print("\nCup Size:")
print(size)


# -------------------------------------
# Using get() Method
# -------------------------------------
customer_note = chai_order.get("note", "no note")

print("\nCustomer Note:")
print(customer_note)