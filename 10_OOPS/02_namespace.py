class Chai:
    origin = "India"
Chai.is_hot = True

# print(Chai.origin)
# print(Chai.is_hot)


# Creating object from class chai

masala = Chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print(masala.origin)
print(masala.is_hot)