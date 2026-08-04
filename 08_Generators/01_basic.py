def server_Chai():
    yield "Chai cup 1 masala chai"
    yield "Chai cup 2 Ginger chai"
    yield "Chai cup 3 Elaichi chai"
    
stall = server_Chai()

# for chai in stall:
#     print(chai)
    
    
def server_Chai():
    yield "Chai cup 1 "
    yield "Chai cup 2 "
    yield "Chai cup 3 "
    
stall = server_Chai()
print(next(stall))
print(next(stall))
print(next(stall))
# print(next(stall))  # Give Error because all the yield values are exhausted.
