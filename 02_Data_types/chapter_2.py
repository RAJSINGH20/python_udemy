# Create an empty set
spice_mix = set()

# Display initial set and its memory ID
print(f"Initial spice_mix : {spice_mix}")
print(f"ID of spice_mix   : {id(spice_mix)}")


# Add spices to the set
spice_mix.add("cumin")
spice_mix.add("ginger")
spice_mix.add("turmeric")


# Display updated set and its memory ID
print(f"\nUpdated spice_mix : {spice_mix}")
print(f"ID of spice_mix   : {id(spice_mix)}")