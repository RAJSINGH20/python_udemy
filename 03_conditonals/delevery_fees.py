order_amount = int(input("enter your order amount: "))
print("your order amount is: ",order_amount)
delivery_fees = 0 if order_amount > 99 else 20
print("your delivery fees is: ",delivery_fees)