from __future__ import print_function
import multiprocessing
def countdown(count):
    while count > 0:
        print("Count value", count)
        count -= 1
    return

if __name__ == "__main__":
     p1 = multiprocessing.Process(target=countdown, args=(10,))
     p1.start()
     p2 = multiprocessing.Process(target=countdown, args=(20,))
     p2.start()
     p1.join()
     p2.join()
