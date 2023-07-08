from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # Create the threads
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    # Start the threads
    for i in threads:
        i.start()

    # Join the threads
    for i in threads:
        i.join()

    print("end main")