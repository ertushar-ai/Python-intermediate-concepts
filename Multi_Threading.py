from threading import Thread, Lock, current_thread
from queue import Queue
import time

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()
        
        
# Designed to work separately =)
        
        
# all threads can access this global variable
database_value = 0

def increase(lock):
    global database_value # needed to modify the global value
    
    with lock:
        # get a local copy (simulate data retrieving)
        local_copy = database_value
            
        # simulate some modifying operation
        local_copy += 1
        time.sleep(0.1)
            
        # write the calculated new value into the global variable
        database_value = local_copy


if __name__ == "__main__":
    
    lock = Lock()

    print('Start value: ', database_value)

    t1 = Thread(target=increase,args=(lock,))
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')
    
    
# Designed to work separately =)


def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()
    
    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')