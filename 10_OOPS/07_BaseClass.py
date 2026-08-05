class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength
        
# class Ginger_Chai(Chai):
#     def __init__(self, type_ , strength , Spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = Spice_level


# class ginger_chai(Chai):
#     def __init__(self, type_, strength , spice_level):
#         Chai.__init__(self, type_, strength)   //explict Call to base class constructor
#         self.spice_level = spice_level


class ginger_chai(Chai):
    def __init__(self, type_, strength , spice_level):
        super().__init__(type_, strength)    # Call to base class constructor
        self.spice_level = spice_level