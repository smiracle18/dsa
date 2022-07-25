"""
Test module for binary_search.py
"""
import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    """
    Test class for binary_search.py module
    """

    def test_binary_search(self):
        """
        Test binary_search() function
        """
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)

    def test_binary_search_with_duplicates(self):
        """
        Test binary_search() function
        """
        arr, target = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10], 5
        self.assertIn(binary_search(arr, target), [7, 8, 9])


if __name__ == '__main__':
    unittest.main()