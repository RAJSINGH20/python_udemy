# =====================================
# Coupon Discount Calculation
# =====================================

# List of users and their orders
users = [
    {"id": 1, "name": "Alice", "total": 100, "coupon": "DISCOUNT10"},
    {"id": 2, "name": "Bob", "total": 200, "coupon": "DISCOUNT20"},
    {"id": 3, "name": "Charlie", "total": 300, "coupon": "DISCOUNT30"}
]

# Coupon rules
# (percentage_discount, fixed_discount)
discounts = {
    "DISCOUNT10": (0.20, 0),   # 20%
    "DISCOUNT20": (0.50, 0),   # 50%
    "DISCOUNT30": (0.30, 10)   # 30% + ₹10
}

# Process each user
for user in users:

    # Get discount details
    percent, fixed = discounts.get(user["coupon"], (0, 0))

    # Calculate discount amount
    discount_amount = user["total"] * percent + fixed

    # Calculate final price
    final_total = user["total"] - discount_amount

    # Display result
    print(
        f"{user['name']} has a discount of ₹{discount_amount:.2f} "
        f"and total after discount is ₹{final_total:.2f}"
    )