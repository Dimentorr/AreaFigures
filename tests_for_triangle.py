import unittest
from area_figures import Triangle


class MyTestCase(unittest.TestCase):
    # ----------------------------Triangle----------------------------
    def test_triangle_normal(self):
        test_obj = Triangle(3, 4, 6)
        self.assertEqual(test_obj.get_area_by_three_sides(), 5.33)

    def test_triangle_incorrect_ratio(self):
        test_obj = Triangle(26, 4, 6)
        with self.assertRaises(Exception) as context:
            test_obj.get_area_by_three_sides()
        self.assertTrue('Incorrect triangle aspect ratio.' in str(context.exception))

    def test_triangle_zero(self):
        test_obj = Triangle(0, 4, 6)
        with self.assertRaises(Exception) as context:
            test_obj.get_area_by_three_sides()
        self.assertTrue('Incorrect data. Impossible value.' in str(context.exception))

    def test_triangle_negative(self):
        test_obj = Triangle(-3, 4, 6)
        with self.assertRaises(Exception) as context:
            test_obj.get_area_by_three_sides()
        self.assertTrue('Incorrect data. Impossible value.' in str(context.exception))

    def test_triangle_string(self):
        test_obj = Triangle('-3', 4, 6)
        with self.assertRaises(Exception) as context:
            test_obj.get_area_by_three_sides()
        self.assertTrue('Incorrect data. Was input string.' in str(context.exception))

    # ----------------------------React Triangle----------------------------
    def test_react_triangle_normal_true(self):
        test_obj = Triangle(3, 4, 5)
        self.assertEqual(test_obj.react_triangle(), True)

    def test_react_triangle_normal_false(self):
        test_obj = Triangle(3, 4, 7)
        self.assertEqual(test_obj.react_triangle(), False)


if __name__ == '__main__':
    unittest.main()
