# Tuple containing different spices
masala_spices = ("cumin", "turmeric", "coriander")


# Tuple unpacking
spice1, spice2, spice3 = masala_spices

print(f"Spice 1 : {spice1}")
print(f"Spice 2 : {spice2}")
print(f"Spice 3 : {spice3}")


# Assigning values
ginger_ratio = 2
cardamom_ratio = 1

print(f"\nBefore Swapping:")
print(f"Ginger Ratio   : {ginger_ratio}")
print(f"Cardamom Ratio : {cardamom_ratio}")


# Swapping values
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"\nAfter Swapping:")
print(f"Ginger Ratio   : {ginger_ratio}")
print(f"Cardamom Ratio : {cardamom_ratio}")


# Membership check
print(f"\nIs 'cumin' present in masala_spices? {'cumin' in masala_spices}")