import sys
import time
import json

import matplotlib.pyplot as plt

from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort
from load_file import create_list_from_text_file as load

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    words_to_sort = load('pan-tadeusz.txt')

    time_results_quick = []
    time_results_selection = []
    time_results_merge = []
    time_results_bubble = []

    y_axis = [1000, 2000, 3000, 4000, 5000, 6000, 7000,
              8000, 9000, 10000, 20000, 30000, 40000, 50000]

    for n in y_axis:

        # QUICK
        array_to_sort = words_to_sort[0:n]
        start = time.process_time()
        sorted_list = quick_sort(array_to_sort)
        stop = time.process_time()
        print('Quick n=', n, '- Czas wykonania w sekundach:', stop - start)
        time_results_quick.append(stop - start)

        # SELECTION
        start = time.process_time()
        sorted_list = selection_sort(array_to_sort)
        stop = time.process_time()
        print('Selection n=', n, '- Czas wykonania w sekundach:', stop - start)
        time_results_selection.append(stop - start)

        # MERGE
        start = time.process_time()
        sorted_list = merge_sort(array_to_sort)
        stop = time.process_time()
        print('Merge n=', n, '- Czas wykonania w sekundach:', stop - start)
        time_results_merge.append(stop - start)

        # BUBBLE
        start = time.process_time()
        sorted_list = bubble_sort(array_to_sort)
        stop = time.process_time()
        time_results_bubble.append(stop - start)
        print('Bubble n=', n, '- Czas wykonania w sekundach:', stop - start)

    data = []
    for i in range(len(y_axis)):
        record_data = {
            "amount": y_axis[i],
            "quick result": time_results_quick[i],
            "selection result": time_results_selection[i],
            "merge result": time_results_merge[i],
            "bubble result": time_results_bubble[i]
        }
        data.append(record_data)
    with open('result.json', 'w') as file_handle:
        json.dump(data, file_handle, indent=5)

    plt.plot(y_axis, time_results_quick, 'red', label='quick sort')
    plt.plot(y_axis, time_results_selection, 'green', label='selection sort')
    plt.plot(y_axis, time_results_merge, 'blue', label='merge sort')
    plt.plot(y_axis, time_results_bubble, 'yellow', label='bubble sort')
    plt.xlabel('n')
    plt.ylabel('time [s]')
    plt.legend()
    plt.title('Time Complexity')
    plt.savefig('time_complexity.png')
