from concurrent.futures import thread
from multiprocessing.dummy import freeze_support
from pathlib import Path
from shutil import move
from time import localtime, sleep, perf_counter

# if(Path('D:\\').exists()):
#     for file in Path('D:\\').glob('**/*.jpg'):
#         move(file, Path('C:\\Users\\maste\\OneDrive\\Desktop\\Pictures\\{:%Y-%m-%d}'.format(localtime())))

from threading import Thread
from multiprocessing import Process

def square(x):
    for i in range(x):
        print(i ** 2)

def test_speed():
    for _ in range(10):

        s = perf_counter()
        threads = []
        for i in range(10):
            t=Thread(target=square, args=(i,))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        f = perf_counter()

        # s = perf_counter()
        # for i in range(10):
        #     square(i)
        # f = perf_counter()

        # s = perf_counter()
        # processes = []
        # for i in range(10):
        #     p = Process(target=square, args=(i,))
        #     p.start()
        #     processes.append(p)
        # for p in processes:
        #     p.join()
        # f = perf_counter()

        print('Timer: {}'.format(f - s))
    print('Done')

if __name__ == '__main__':
    freeze_support()
    test_speed()