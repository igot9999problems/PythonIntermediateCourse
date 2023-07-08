from multiprocessing import Pool

def cube(number):
    return number * number * number

if __name__ == "__main__":

    numbers = range(10)

    # A pool will basically take care of multiprocessing everything for you
    pool = Pool()

    # map, apply, join, close
    result = pool.map(cube, numbers)

    pool.close()
    pool.join()

    print(result)