def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "MAtcha Chai"
    yield "Oolong Chai"

def fullMenu():
    yield from local_chai()
    yield from imported_chai()

for chai in fullMenu():
    print(chai)

def Chai_Stall():
    try:
        while True:
            order = yield
            print(f"Preparing {order}")
    except:
        print("Shop Closed")


stall = Chai_Stall()
print(next(stall))  # Start the generator
stall.close()  # Close the generator
