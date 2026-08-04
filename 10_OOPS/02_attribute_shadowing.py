class chai:
    temp = "hot"
    strength = "strong"

cutting = chai()
print(cutting.temp)

cutting.temp = "cold"
print(cutting.temp)
print(chai.temp)

del cutting.temp
print(cutting.temp)