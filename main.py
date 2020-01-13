import os
import multiprocessing as mp

def hello():
    print('hello', os.getpid())

    mp.current_process().daemon = False

    process = 3
    pool = mp.Pool(process)
    pool.starmap(bye, [[] for _ in range(process)])

def bye():
    print('bye', os.getpid())

if __name__ == '__main__':
    print('main', os.getpid())

    process = 2
    pool = mp.Pool(process)
    pool.starmap(hello, [[] for _ in range(process)])
