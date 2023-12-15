import unittest
from logic import get_number_from_index, get_empty_list, get_index_from_number, move_left, move_right, move_up, \
    move_down, can_move


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

    def test_move_left(self):
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        rez = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rez, 12, True))
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rez = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0]
        ]
        self.assertEqual(move_left(mas), (rez, 32, True))

    def test_move_right(self):
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        rez = [
            [0, 0, 0, 4],
            [0, 0, 0, 8],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_right(mas), (rez, 12, True))
        mas = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        rez = [
            [0, 2, 8, 2],
            [0, 0, 4, 2],
            [0, 0, 0, 0],
            [0, 0, 16, 8]
        ]
        self.assertEqual(move_right(mas), (rez, 32, True))

    def test_move_up(self):
        mas = [
            [2, 2, 0, 0],
            [2, 0, 4, 2],
            [4, 4, 0, 2],
            [4, 0, 4, 0]
        ]
        rez = [
            [4, 2, 8, 4],
            [8, 4, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(mas), (rez, 24, True))

    def test_move_down(self):
        mas = [
            [2, 2, 0, 0],
            [2, 0, 4, 2],
            [4, 4, 0, 2],
            [4, 0, 4, 0]
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 2, 0, 0],
            [8, 4, 8, 4]
        ]
        self.assertEqual(move_down(mas), (rez, 24, True))

    def test_can_move(self):
        mas = [
            [2, 2, 0, 0],
            [2, 0, 4, 2],
            [4, 4, 0, 2],
            [4, 0, 4, 0]
        ]
        self.assertEqual(can_move(mas), True)
        mas = [
            [4, 2, 1, 3],
            [2, 1, 3, 4],
            [1, 3, 4, 2],
            [3, 4, 2, 1]
        ]
        self.assertEqual(can_move(mas), False)

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
