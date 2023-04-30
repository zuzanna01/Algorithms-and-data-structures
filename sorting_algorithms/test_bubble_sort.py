from bubble_sort import bubble_sort

def test_random_array():
    assert bubble_sort([5, 1, 10, 500, 2, 8, 74]) == [1, 2, 5, 8, 10, 74, 500]


def test_duplicates_in_array():
    assert bubble_sort([5, 2, 3, 8, 9, 5, 2]) == [2, 2, 3, 5, 5, 8, 9]


def test_whole_array_same_number():
    assert bubble_sort([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]


def test_one_number():
    assert bubble_sort([1]) == [1]


def test_negative_numbers():
    assert bubble_sort([5, 2, 9, -5, 1, -1]) == [-5, -1, 1, 2, 5, 9]


def test_empty_array():
    assert bubble_sort([]) == []
