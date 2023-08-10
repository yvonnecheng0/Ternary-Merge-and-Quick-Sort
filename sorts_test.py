""""
Module will test functionality of sorts.py
Yvonne Cheng 
csci 112
Winter, 2023
"""

import unittest
from sorts import *

class TestSorts(unittest.TestCase):

    def test_mergeSortBinary(self):
        #Test small list
        alist = [5, 4, 2, 7, 1]
        mergeSortBinary(alist)
        self.assertEqual(alist, [1, 2, 4, 5, 7])

        #Test empty list
        alist = []
        mergeSortBinary(alist)
        self.assertEqual(alist, [])

        #Test one item
        alist = [4]
        mergeSortBinary(alist)
        self.assertEqual(alist, [4])

    def test_mergeSortTernary(self):
        #Test small list
        alist = [5, 4, 2, 7, 1]
        mergeSortTernary(alist)
        self.assertEqual(alist, [1, 2, 4, 5, 7])

        #Test empty list
        alist = []
        mergeSortTernary(alist)
        self.assertEqual(alist, [])

        #Test one item
        alist = [50]
        mergeSortTernary(alist)
        self.assertEqual(alist, [50])
        
    def test_quickSortBinary(self):
        #Test small list
        alist = [5, 4, 2, 7, 1]
        quickSortBinary(alist)
        self.assertEqual(alist, [1, 2, 4, 5, 7])

        #Test empty list
        alist = []
        quickSortBinary(alist)
        self.assertEqual(alist, [])

        #Test one item
        alist = [4]
        quickSortBinary(alist)
        self.assertEqual(alist, [4])

    def test_quickSortTernary(self):
        #Test small list
        alist = [5, 4, 2, 7, 1]
        quickSortTernary(alist)
        self.assertEqual(alist, [1, 2, 4, 5, 7])

        #Test empty list
        alist = []
        quickSortTernary(alist)
        self.assertEqual(alist, [])

        #Test one item
        alist = [50]
        quickSortTernary(alist)
        self.assertEqual(alist, [50])

if __name__ == "__main__":
    unittest.main(verbosity = 2)