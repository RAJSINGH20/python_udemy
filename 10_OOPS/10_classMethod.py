class ChaiOrder:
    def __init__(self, tea_type , Sweetness , size):
        self.tea_type = tea_type
        self.Sweetness = Sweetness
        self.size = size
        
    
    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["swetness"],
            order_data["size"]
        )
        
    @classmethod
    def from_string(cls , order_string):
        tea_type , swetness , size = order_string.split("-")
        return cls(tea_type , swetness, size)


class chaiUtils:
    
    @staticmethod
    def is_valid(size):
        return size in ["small","Medium","Large"]




order1 = ChaiOrder.from_dict({"tea_type":"ginger","swetness":"medium","size":"Large"})
order2 = ChaiOrder.from_string("ginger-low-small")
order3 = ChaiOrder("large","low","Large")
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)