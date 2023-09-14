import unittest
from area_figures import Circle


class MyTestCase(unittest.TestCase):
    # ----------------------------Circle----------------------------
    def test_circle_normal(self):
        test_obj = Circle(3)
        self.assertEqual(test_obj.get_area(), 18.84)

    def test_circle_zero(self):
        test_obj = Circle(0)
        self.assertEqual(test_obj.get_area(), 'Incorrect data')

    def test_circle_negative(self):
        test_obj = Circle(-5)
        self.assertEqual(test_obj.get_area(), 'Incorrect data')

    def test_circle_strung(self):
        test_obj = Circle('-5')
        self.assertEqual(test_obj.get_area(), 'Incorrect data')

    def test_circle_tuple(self):
        test_obj = Circle((1, 4, 5))
        self.assertEqual(test_obj.get_area(), 'Incorrect data')

    def test_circle_list(self):
        test_obj = Circle([1, 4, 5])
        self.assertEqual(test_obj.get_area(), 'Incorrect data')


if __name__ == '__main__':
    unittest.main()
