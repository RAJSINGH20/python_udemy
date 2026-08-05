class OutOfIndregientError:
    pass

def milk_chai(milk , sugar):
    if(milk == 0 or sugar == 0):
        raise OutOfIndregientError("missing milk or sugar")
    else:
        print("chai ready")


milk_chai(1,1)
milk_chai(0,0)