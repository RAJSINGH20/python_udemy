import threading

# Create two locks
lock_a = threading.Lock()
lock_b = threading.Lock()


# Task 1 acquires Lock A first, then Lock B
def task1():
    with lock_a:
        print("Task 1 acquired Lock A")
        with lock_b:
            print("Task 1 acquired Lock B")


# Task 2 acquires Lock B first, then Lock A
def task2():
    with lock_b:
        print("Task 2 acquired Lock B")
        with lock_a:
            print("Task 2 acquired Lock A")


# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()