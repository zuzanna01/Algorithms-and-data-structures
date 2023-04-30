import unittest
from quick_sort import quick_sort_recursive, quick_sort


class TestQuickSort(unittest.TestCase):
    def test_quick_sort_recursive(self):
        array = [5, 7, 2, 1]
        result = quick_sort_recursive(array, 0, len(array) - 1)
        self.assertEqual(result, [1, 2, 5, 7])

    def test_quick_sort(self):
        array_1 = [5, 7, 2, 1]
        result = quick_sort(array_1)
        self.assertEqual(result, [1, 2, 5, 7])
        array_2 = ['adam', 'mickiewicz', 'pan', 'tadeusz',
                   'czyli', 'ostatni', 'zajazd', 'na', 'litwie']
        result = quick_sort(array_2)
        self.assertEqual(result, ['adam', 'czyli', 'litwie', 'mickiewicz',
                                  'na', 'ostatni', 'pan', 'tadeusz', 'zajazd'])
        array_3 = [5, -7, 2, 1]
        result = quick_sort(array_3)
        self.assertEqual(result, [-7, 1, 2, 5])
        array_4 = [1]
        result = quick_sort(array_4)
        self.assertEqual(result, [1])
        array_5 = []
        result = quick_sort(array_5)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
