import threading
import time

# Function to print numbers
def print_numbers():
    for i in range(1, 6):
        print("Thread 1 - Number:", i)
        time.sleep(1)

# Function to print alphabets
def print_alphabets():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print("Thread 2 - Alphabet:", ch)
        time.sleep(1)

# Function to display messages
def display_messages():
    messages = ["Hello", "Welcome", "Python", "Multithreading", "Complete"]
    for msg in messages:
        print("Thread 3 - Message:", msg)
        time.sleep(1)

# Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)
t3 = threading.Thread(target=display_messages)

# Starting threads
t1.start()
t2.start()
t3.start()

# Waiting for all threads to complete
t1.join()
t2.join()
t3.join()

print("\nAll threads have completed execution.")