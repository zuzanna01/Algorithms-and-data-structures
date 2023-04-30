from merge_sort import merge_sort


def test_random_array():
    assert merge_sort([5, 10, 2, 8, 9, 1]) == [1, 2, 5, 8, 9, 10]


def test_array_odd_amount_of_numbers():
    assert merge_sort([
        5, 10, 9, 2, 1, 15, 4, -5, -4
        ]) == [
            -5, -4, 1, 2, 4, 5, 9, 10, 15
            ]


def test_array_same_numbers():
    assert merge_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]


def test_empty_array():
    assert merge_sort([]) == []
