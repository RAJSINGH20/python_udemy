# =====================================
# Working with Arrow Library
# =====================================

# Import Arrow library
import arrow as ar

# Get current UTC time
my_time = ar.utcnow()

print("Current UTC Time:")
print(my_time)

# Convert UTC time to Rome timezone
rome_time = my_time.to("Europe/Rome")

print("\nTime in Rome:")
print(rome_time)

