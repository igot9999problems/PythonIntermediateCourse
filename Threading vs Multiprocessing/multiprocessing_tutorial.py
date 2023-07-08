import multiprocessing
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # Create the processes
    for i in range(num_processes):
        p = multiprocessing.Process(target=square_numbers)
        processes.append(p)

    # Start the processes
    for i in processes:
        i.start()

    # Join the processes
    for i in processes:
        i.join()
    
    print("end main")