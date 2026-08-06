import threading
import time


# Function to take orders
def take_order():
    for i in range(1, 4):
        print(f"Taking order #{i}")
        time.sleep(1)


# Function to brew chai
def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai #{i}")
        time.sleep(2)

# Function to brew chai
def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai #{i}")
        time.sleep(2)

print("Taking a order............")
# Create threads
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

# Start both threads
order_thread.start()
brew_thread.start()

# Wait for both threads to finish
order_thread.join()
brew_thread.join()

# Final message
print("All orders have been brewed.")