class chaiCup:
    size = 150
    
    def describe(self):
        return f"Cup size: {self.size} ml"

cup = chaiCup()
print(cup.describe())
print(chaiCup.describe(cup))  

cup_2 = chaiCup()
print(cup_2.describe())