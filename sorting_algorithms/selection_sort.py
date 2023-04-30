# Selection sort in Python

def selection_sort(input_array):
    array = input_array.copy()
    for index in range(len(array)):
        min_idx = index

        for i in range(index + 1, len(array)):

            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[index], array[min_idx]) = (array[min_idx], array[index])
    return array


if __name__ == '__main__':
    print(selection_sort([2, 7, 1, 3, 56]))
