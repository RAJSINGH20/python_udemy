chai_size = input("enter size of chai : ").lower()

if chai_size == "small":
    print("you have selected small size chai, price is 10")
elif chai_size == "medium":
    print("you have selected medium size chai, price is 15")
elif chai_size == "large":
    print("you have selected large size chai, price is 20")
else:
    print("Sorry, we do not have that size of chai. Please select from small, medium, or large.")