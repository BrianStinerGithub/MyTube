from pathlib import Path
from shutil import move
from time import localtime

if(Path('D:\\').exists()):
    for file in Path('D:\\').glob('**/*.jpg'):
        move(file, Path('C:\\Users\\maste\\OneDrive\\Desktop\\Pictures\\{:%Y-%m-%d}'.format(localtime())))

from threading import Thread
from multiprocessing import Process

def square(x):
    yield x * x