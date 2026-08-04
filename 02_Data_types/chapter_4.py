# Boolean value
is_boiling = True

# Integer value
stir_count = 5

# Boolean behaves like 1 (True) or 0 (False)
total = stir_count + is_boiling

print(f"Total Value               : {total}")
print(f"Initial value of is_boiling : {is_boiling}")
print(f"Initial value of stir_count : {stir_count}")


# Checking truthy value
milk_liters = 11

print(f"\nIs milk_liters True? : {bool(milk_liters)}")


# Tea preparation example - Case 1
water_hot = True
tea_added = False

can_serve_tea = water_hot and tea_added

print(f"\nCan we serve tea? : {can_serve_tea}")


# Tea preparation example - Case 2
water_hot = True
tea_added = True

can_serve_tea = water_hot and tea_added

print(f"Can we serve tea? : {can_serve_tea}")