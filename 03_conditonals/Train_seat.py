train_seat = input ("enter your train seat type : ").lower()

match train_seat:
    case "sleeper":
        print("you have selected sleeper class, price is 1000")
    case "seater":
        print("you have selected seater class, price is 500")
    case "ac":
        print("you have selected AC class, price is 1500")
    case "luxury":
        print("you have selected luxury class, price is 2000")
    case _:
        print("invalid seat type") 