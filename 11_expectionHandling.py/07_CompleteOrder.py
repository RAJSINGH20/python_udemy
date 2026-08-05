# Custom exception for invalid chai
class InvalidChaiError(Exception):
    pass


# Function to calculate the bill
def bill(flavour, cups):
    menu = {
        "masala": 20,
        "ginger": 40,
    }

    try:
        # Check if the chai exists in the menu
        if flavour not in menu:
            raise InvalidChaiError("That chai is not in the menu.")

        # Check if cups is an integer
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer.")

        # Check if cups is positive
        if cups <= 0:
            raise ValueError("Number of cups must be greater than 0.")

        # Calculate total bill
        total = menu[flavour] * cups

        # Display the bill
        print("----- Chai Bill -----")
        print(f"Flavour : {flavour.title()}")
        print(f"Cups    : {cups}")
        print(f"Price   : ₹{menu[flavour]} per cup")
        print(f"Total   : ₹{total}")

    except InvalidChaiError as e:
        print("Error:", e)

    except TypeError as e:
        print("Error:", e)

    except ValueError as e:
        print("Error:", e)

    finally:
        print("Thank you for visiting!\n")


# Test cases
bill("masala", 2)
bill("ginger", 3)
bill("lemon", 2)
bill("masala", "two")
bill("masala", -1)