def chai_customer():
    print("Customer: I want a cup of chai")
    order = yield
    while True:
        print(f"Customer: I want a cup of {order}")
        order = yield

stall = chai_customer()
next(stall)  # Start the generator
stall.send("Masala Chai")
stall.send("Ginger Chai")