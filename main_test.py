import unittest
from logic import get_number_from_index, get_empty_list, get_index_from_number



class Test_2048(unittest.TestCase):
    def test_get_number_from_index(self):
        self.assertEqual(get_number_from_index(3, 3), 16)
        self.assertEqual(get_number_from_index(0, 0), 1)
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_get_empty_list(self):
        a = [1, 2, 3, 5, 7, 8, 10, 11, 12, 13, 14, 16]
        mas = [
            [0, 0, 0, 2],
            [0, 2, 0, 0],
            [2, 0, 0, 0],
            [0, 0, 2, 0]
        ]
        self.assertEqual(get_empty_list(mas), a)
        a = []
        mas = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]
        self.assertEqual(get_empty_list(mas), a)
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_get_index_from_number(self):
        self.assertEqual(get_index_from_number(1), (0, 0))
        self.assertEqual(get_index_from_number(16), (3, 3))
        self.assertEqual(get_index_from_number(5), (1, 0))

    # def test_is_zero_in_mas(self):
    #     mas = [
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0]
    #     ]
    #     self.assertEqual(is_zero_in_mas(mas), True)
    #     mas = [
    #         [2, 2, 2, 2],
    #         [2, 2, 2, 2],
    #         [2, 2, 2, 2],
    #         [2, 2, 2, 2]
    #     ]
    #     self.assertEqual(is_zero_in_mas(mas), False)
    #     mas = [
    #         [2, 0, 2, 0],
    #         [2, 2, 0, 2],
    #         [2, 0, 4, 0],
    #         [2, 0, 4, 0]
    #     ]
    #     self.assertEqual(is_zero_in_mas(mas), True)


if __name__ == 'main':
    unittest.main()
