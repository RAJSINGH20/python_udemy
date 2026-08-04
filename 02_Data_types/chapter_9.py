# =====================================
# Python Set Operations Example
# =====================================

# Essential spices used in chai
essential_spices = {"cardamom", "ginger", "turmeric"}

# Optional spices that can also be added
optional_spices = {"cloves", "ginger", "black pepper"}


# -------------------------------------
# Union (|) - Combines all unique items
# -------------------------------------
all_spices = essential_spices | optional_spices

print("All spices:")
print(all_spices)


# -------------------------------------
# Intersection (&)
# Finds common items in both sets
# -------------------------------------
common_spices = essential_spices & optional_spices

print("\nCommon spices:")
print(common_spices)


# -------------------------------------
# Difference (-)
# Items present only in essential_spices
# -------------------------------------
only_in_essential = essential_spices - optional_spices

print("\nOnly in essential spices:")
print(only_in_essential)

 
# -------------------------------------
# Membership Test (in)
# Checks whether an item exists in a set
# -------------------------------------
print("\nIs 'cloves' in essential spices?","cloves" in essential_spices)