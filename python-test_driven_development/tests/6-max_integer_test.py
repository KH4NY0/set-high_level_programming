#!/usr/bin/python3
"""Unittest for max_integer([..])

Run with: python3 -m unittest tests.6-max_integer_test
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test a list of integers sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list of integers in no particular order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_reverse_ordered_list(self):
        """Test a list of integers sorted in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_beginning(self):
        """Test a list where the largest value comes first."""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Test a list where the largest value comes last."""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test that calling with no argument returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list holding a single integer."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list of only negative integers."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_signs(self):
        """Test a list mixing positive and negative integers."""
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_duplicates(self):
        """Test a list where the largest value appears more than once."""
        self.assertEqual(max_integer([4, 4, 2, 4]), 4)

    def test_all_identical(self):
        """Test a list where every element is the same."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 3.7, 2.2]), 3.7)

    def test_ints_and_floats(self):
        """Test a list mixing integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2, 0.5]), 2.5)

    def test_zeros(self):
        """Test a list of zeroes."""
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_large_numbers(self):
        """Test a list holding large integers."""
        self.assertEqual(max_integer([1000000, 999999, 1]), 1000000)

    def test_string_of_characters(self):
        """Test that a string returns its largest character."""
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        """Test a list of strings, compared lexicographically."""
        self.assertEqual(max_integer(["Holberton", "ALX", "School"]), "School")

    def test_empty_string(self):
        """Test that an empty string returns None."""
        self.assertIsNone(max_integer(""))

    def test_none_argument(self):
        """Test that None raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_uncomparable_types(self):
        """Test that mixing strings and integers raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])


if __name__ == '__main__':
    unittest.main()
