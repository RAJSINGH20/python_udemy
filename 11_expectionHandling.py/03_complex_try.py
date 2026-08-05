def serveChai(flavour):
    try:
        print(f"preparing {flavour} chai")
        if(flavour == "unknown"):
            raise ValueError("we dont know about this flavour")
    except ValueError as e:
        print("Error :",e)
    else:
        print(f"{flavour} is served ")
    finally:
        print("next Customer please ")


serveChai("Masala Chai")
serveChai("unknown")