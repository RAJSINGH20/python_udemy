def brewChai(flavour):
    Shop_flavour = ["masala","ginger","eleachi"]
    if flavour not in Shop_flavour:
        raise ValueError("unsuppoted chai Flavour")
    else:
        print(f"Brewing {flavour} chai")

brewChai("mint")