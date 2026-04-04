from multiprocessing import Process
from threading import Thread
import os
import time

def square_num():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == '__main__':

    processes = []
    num_processes = os.cpu_count()

    # Creating processes:
    for i in range(num_processes):
        p = Process(target=square_num)
        processes.append(p)

    # Starting processes:

    for p in processes:
        p.start()

    # Joining the processes:

    for p in processes:
        p.join()

    print("Processing Complete")


# Designed to be executed separately =)


def square_num():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == '__main__':
    threads = []
    num_threads = 10

    # Creating threads:

    for i in range(num_threads):
        t = Thread(target=square_num)
        threads.append(t)

    # Starting a thread:

    for t in threads:
        t.start()

    # Joining threads:

    for t in threads:
        t.join()

    print("Threading complete")
    