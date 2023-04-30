import time
import sys

from heap import Heap
from list_generator import generate_list
import matplotlib.pyplot as plt

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    values = generate_list(20, 30)
    our_heap = Heap(values, 3)
    our_heap.print()
    print('--------------------------')
    print('INSERT 100')
    our_heap.insert(100)
    our_heap.print()
    print('--------------------------')
    print('INSERT 55')
    our_heap.insert(55)
    our_heap.print()
    print('--------------------------')
    print('REMOVE ROOT')
    our_heap.remove_root()
    our_heap.print()
    print('--------------------------')
    print('REMOVE ROOT')
    our_heap.remove_root()
    our_heap.print()