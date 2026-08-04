# Chai order details
chai_type = "ginger chai"
customer_name = "Alice"

# Basic formatted output
print(f"Order for {customer_name}: {chai_type} please")


# Chai description
chai_description = "Aromatic blend of black tea, ginger, and spices"

# String slicing examples
print(f"\n{customer_name} ordered a {chai_description[0:7]} chai")
print(f"{customer_name} ordered a {chai_description[0:8]} chai")
print(f"{customer_name} ordered a {chai_description[0:8:2]} chai")
print(f"{customer_name} ordered a {chai_description[5:]} chai")
print(f"{customer_name} ordered a {chai_description[::-1]} chai")


# Encoding and decoding example
label_text = "Chai Latte"

# Convert string into bytes
encoded_text = label_text.encode("utf-8")

print("\nNon-encoded:", label_text)
print("Encoded:", encoded_text)

# Convert bytes back into string
decoded_text = encoded_text.decode("utf-8")

print("Decoded:", decoded_text)