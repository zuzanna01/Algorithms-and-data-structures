def bubble_sort(input_array):
    array = input_array.copy()
    sorted = 0
    for _ in range(len(array)):
        i = len(array) - 1
        for _ in range(len(array) - sorted - 1):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
            i -= 1
        sorted += 1
    return array
