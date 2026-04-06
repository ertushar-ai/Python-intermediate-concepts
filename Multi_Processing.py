# Designed to work separately =)

from multiprocessing import Process, Value, Array, Lock, Queue
import os
import time

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine. Usually a good choice for the number of processes

    # create processes and assign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main program until these processes are finished
    for process in processes:
        process.join()
        
# Designed to work separately =)

def add_100(number,lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

def add_100_array(numbers,lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


if __name__ == "__main__":
    
    lock = Lock()

    shared_number = Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    process1 = Process(target=add_100, args=(shared_number,lock))
    process2 = Process(target=add_100, args=(shared_number,lock))

    process3 = Process(target=add_100_array, args=(shared_array,lock))
    process4 = Process(target=add_100_array, args=(shared_array,lock))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')
    
# Designed to work separately =)

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i*-1)

if __name__ == "__main__":
    
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers,q))
    p2 = Process(target=make_negative, args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # order might not be sequential
    while not q.empty():
        print(q.get())
        
    print('end main')
    
# Designed to work separately =)

from multiprocessing import Pool 

def cube(number):
    return number * number * number

    
if __name__ == "__main__":
    numbers = range(10)
    
    p = Pool()

    # by default this allocates the maximum number of available 
    # processors for this task --> os.cpu_count()
    result = p.map(cube,  numbers)
    
    # or 
    # result = [p.apply(cube, args=(i,)) for i in numbers]
    
    p.close()
    p.join()
    
    print(result)