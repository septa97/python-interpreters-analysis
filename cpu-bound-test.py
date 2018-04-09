import time

from threading import Thread

def foo(COUNT):
    """
    From David Beazley's CPU bound test code
    http://www.dabeaz.com/GIL/gilvis/measure2.py
    """
    def countdown(n):
            while n > 0:
                    n -= 1

    t1 = Thread(target=countdown,args=(COUNT/2,))
    t2 = Thread(target=countdown,args=(COUNT/2,))
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.time()
    print COUNT, end-start

def main():
    counts = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
    for count in counts:
        foo(count)

main()
