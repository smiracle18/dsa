"""
Test module for binary_search.py
"""
import unittest
from binary_search import BinarySearch


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
        self.assertEqual(BinarySearch.binary_search(arr, target), 4)

    def test_binary_search_with_duplicates(self):
        """
        Test binary_search() function
        """
        arr, target = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10], 5
        self.assertIn(BinarySearch.binary_search(arr, target), [7, 8, 9])

    def test_binary_search_without_target(self):
        """
        Test binary_search() function
        """
        arr, target = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10], 12
        self.assertIn(BinarySearch.binary_search(arr, target), [-1])


        

    '''Left test cases'''

    def test_binary_search_left(self):
        """
        Test binary_search_left() function
        """
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        self.assertEqual(BinarySearch.binary_search_left(arr, target), 4)

    def test_binary_search_left_with_duplicates(self):
        """
        Test binary_search_left() function
        """
        arr, target = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10], 5
        self.assertIn(BinarySearch.binary_search_left(arr, target), [7])

    def test_binary_search_left_without_target(self):
        """
        Test binary_search_left() function
        """
        arr, target = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10], 12
        self.assertIn(BinarySearch.binary_search_left(arr, target), [-1])

    

if __name__ == '__main__':
    unittest.main()