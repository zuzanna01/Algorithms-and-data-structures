# Quick sort in Python

# function to find the partition position
def partition(array, left_index, right_index):
    # set pivot as the rightmost element
    pivot = array[right_index]

    # pointer for greater element - greater than pivot and leftmost element
    i = left_index - 1

    for j in range(left_index, right_index):
        if array[j] <= pivot:
            i = i + 1

            # smaller element is moved to the front / swapped with i-pointer
            (array[i], array[j]) = (array[j], array[i])

    # pivot is swapped with i-pointer
    (array[i + 1], array[right_index]) = (array[right_index], array[i + 1])
    # returns pivot position for next split
    return i + 1


# function to perform quicksort recursive version
def quick_sort_recursive(array, left_index, right_index):
    if left_index < right_index:
        pi = partition(array, left_index, right_index)
        quick_sort_recursive(array, left_index, pi - 1)
        quick_sort_recursive(array, pi + 1, right_index)
        return array
    else:
        return ("ERROR: LEFT INDEX > RIGHT INDEX")


def quick_sort(array):
    if not array:
        return []

    if len(array) == 1:
        return array

    sorted_array = quick_sort_recursive(array[0:len(array)], 0, len(array) - 1)
    return sorted_array


if __name__ == '__main__':
    print(quick_sort([3,5,2,-1,2]))
