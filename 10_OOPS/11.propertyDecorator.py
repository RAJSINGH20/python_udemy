class TeaLeaf:
    def __init__(self , age):
        self._age = age;
    
    @property
    
    def age(self):
        return self._age + 2
    
    @age.setter
    
    def age(self , age):
        if 1 <= age >=5:
            self._age = age
        else:
            raise ValueError("tae leaf is not verified the condition")


leaf = TeaLeaf(2)
print(TeaLeaf.age)
TeaLeaf.age = 4
print(TeaLeaf.age)