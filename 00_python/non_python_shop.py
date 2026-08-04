class chai:
    def __init__(self , sweetness , milklevel):
        self.sweetness = sweetness
        self.milklevel = milklevel
        
    def sip(self):
        print("sipping chai ")
        
    def add_sugar(self):
        print("add Sugar")
        
myChai=chai(sweetness=3, milklevel=4)

myChai.add_sugar(3)
