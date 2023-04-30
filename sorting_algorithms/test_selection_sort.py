import unittest
from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort(self):
        array_1 = [5, 7, 2, 1]
        result = selection_sort(array_1)
        self.assertEqual(result, [1, 2, 5, 7])
        array_2 = ['adam', 'mickiewicz', 'pan', 'tadeusz', 'czyli',
                   'ostatni', 'zajazd', 'na', 'litwie']
        result = selection_sort(array_2)
        self.assertEqual(result, ['adam', 'czyli', 'litwie', 'mickiewicz',
                                  'na', 'ostatni', 'pan', 'tadeusz', 'zajazd'])
        array_3 = [5, -7, 2, 1]
        result = selection_sort(array_3)
        self.assertEqual(result, [-7, 1, 2, 5])
        array_4 = [1]
        result = selection_sort(array_4)
        self.assertEqual(result, [1])
        array_5 = []
        result = selection_sort(array_5)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
