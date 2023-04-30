import time
import sys

from heap import Heap
from list_generator import generate_list
import matplotlib.pyplot as plt

if __name__ == '__main__':

    values = generate_list(1000000, 3000000)

    time_results_insert_2 = []
    time_results_insert_5 = []
    time_results_insert_7 = []
    time_results_remove_2 = []
    time_results_remove_5 = []
    time_results_remove_7 = []
    #test_elements = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    test_elements = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 95000, 100000,
                     120000, 150000, 170000, 200000, 400000, 600000, 800000, 1000000]

    # INSERT
    for n in test_elements:
        test_values = values[0:n]
        start = time.process_time()
        test_heap = Heap(test_values, 2)
        stop = time.process_time()
        time_results_insert_2.append(stop - start)
        
        start = time.process_time()
        test_heap = Heap(test_values, 5)
        stop = time.process_time()
        time_results_insert_5.append(stop - start)

        start = time.process_time()
        test_heap = Heap(test_values, 7)
        stop = time.process_time()
        time_results_insert_7.append(stop - start)

    plt.figure(1)
    plt.plot(test_elements, time_results_insert_2, 'red', label='insert 2')
    plt.plot(test_elements, time_results_insert_5, 'green', label='insert 5')
    plt.plot(test_elements, time_results_insert_7, 'blue', label='insert 7')
    plt.xlabel('n')
    plt.ylabel('time [s]')
    plt.legend()
    plt.title('Time Complexity - insert n elements')
    plt.savefig('time_insert.png')

    #REMOVE ROOT
    
    for n in test_elements:
        test_heap = Heap(values, 2)
        start = time.process_time()
        for m in range(n+1):
            test_heap.remove_root()
        stop = time.process_time()
        time_results_remove_2.append(stop - start)
        print('remove 2')
        print(n)

    for n in test_elements:
        test_heap = Heap(values, 5)
        start = time.process_time()
        for m in range(n+1):
            test_heap.remove_root()
        stop = time.process_time()
        time_results_remove_5.append(stop - start)
        print('remove 5')
        print(n)

    for n in test_elements:
        test_heap = Heap(values, 7)
        start = time.process_time()
        for m in range(n+1):
            test_heap.remove_root()
        stop = time.process_time()
        time_results_remove_7.append(stop - start)
        print('remove 7')
        print(n)

    plt.figure(2)
    plt.plot(test_elements, time_results_remove_2, 'red', label='remove 2')
    plt.plot(test_elements, time_results_remove_5, 'green', label='remove 5')
    plt.plot(test_elements, time_results_remove_7, 'blue', label='remove 7')
    plt.xlabel('n')
    plt.ylabel('time [s]')
    plt.legend()
    plt.title('Time Complexity - remove heap root n times')
    plt.savefig('time_remove.png')