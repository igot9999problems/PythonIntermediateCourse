from multiprocessing import Process, Value, Array, Lock
import time
import os

def square_numbers():
    for i in range(100):
        i * i

def add_100(x, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        x.value += 1
        lock.release()

def add_100_arr(x_more, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            for j in range(len(x_more)):
                x_more[j] += 1

if __name__ == "__main__":
    lock = Lock()

    # How to share values between processes, since they don't share the same memory space
    shared_number = Value('i', 0)
    print("Number at beginning is:", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Number at end is:", shared_number.value)
    print()


    shared_array = Array('d', [0.0, 100.0, 200.0])
    print("Array at the beginning is", shared_array[:])

    p1 = Process(target=add_100_arr, args=(shared_array,lock))
    p2 = Process(target=add_100_arr, args=(shared_array,lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Array at the end is", shared_array[:])
    print()