# Import required modules
import sys
from fractions import Fraction
from decimal import Decimal


# Floating-point numbers
ideal_temp = 95.5
current_temp = 95.49999999999999

# Display values
print(f"Ideal Temperature   : {ideal_temp}")
print(f"Current Temperature : {current_temp}")

# Difference between values
difference = ideal_temp - current_temp

print(f"Temperature Difference : {difference}")


# Display float information
print("\nSystem Float Information:")
print(sys.float_info)