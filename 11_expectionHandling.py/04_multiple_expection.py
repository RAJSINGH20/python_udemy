# Function to process a chai order
def process_order(item, quantity):
    try:
        # Dictionary containing chai prices
        price = {"masala": 20,"ginger":20}[item]

        # Calculate total cost
        cost = price * quantity

        # Display the total cost
        print(f"The total cost is {cost}")

    # Handle invalid chai names
    except KeyError:
        print("Sorry, the chai is not in the menu.")

    # Handle invalid quantity types
    except TypeError:
        print("Quantity must be a number.")

    # Execute if no exception occurs
    else:
        print("Order processed successfully.")

    # Always execute
    finally:
        print("Thank you for visiting!\n")


# Test cases
process_order("ginger", 2)
process_order("masala", "two")
process_order("masala", 2)