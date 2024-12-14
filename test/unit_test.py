#coding:utf-8

import unittest
import sys
sys.path.append("./")  #for run in root directory
sys.path.append("../") #for run in test/ directory 
from segment.segment import QueueMgr

class TestStringMethods(unittest.TestCase):
    """
    unit test class
    """
    def test_empty_queue(self):
        """
        test the empty output
        """
        queue_mgr = QueueMgr()
        self.assertEqual(queue_mgr.to_string(), '[]')
    
    def test_add(self):
        """
        test the add functions
        """
        queue_mgr = QueueMgr()
        queue_mgr.add(10, 30, 1)
        self.assertEqual(queue_mgr.to_string(), '[[10, 1], [30, 0]]')
        queue_mgr.add(20, 40, 1)
        self.assertEqual(queue_mgr.to_string(), '[[10, 1], [20, 2], [30, 1], [40, 0]]')

    def test_add2(self):
        """
        other add test
        """
        queue_mgr = QueueMgr()
        queue_mgr.add(10, 30, 1)
        self.assertEqual(queue_mgr.to_string(), '[[10, 1], [30, 0]]')
        queue_mgr.add(20, 40, 1)
        self.assertEqual(queue_mgr.to_string(), '[[10, 1], [20, 2], [30, 1], [40, 0]]')
        queue_mgr.add(10, 40, -1)
        self.assertEqual(queue_mgr.to_string(), '[[20, 1], [30, 0]]')
        queue_mgr.add(10, 40, -1)
        self.assertEqual(queue_mgr.to_string(), '[[10, -1], [20, 0], [30, -1], [40, 0]]')

    def test_add3(self):
        """
        test other screne
        """
        queue_mgr = QueueMgr()
        queue_mgr.add(-10, 20, 1)
        self.assertEqual(queue_mgr.to_string(), '[[-10, 1], [20, 0]]')
        queue_mgr.add(10, 40, 1)
        self.assertEqual(queue_mgr.to_string(), '[[-10, 1], [10, 2], [20, 1], [40, 0]]')
        queue_mgr.add(0, 20, -3)
        #index 0 is not exist, so the value is 1(the 0's prev -10's value) + -3 = -2
        self.assertEqual(queue_mgr.to_string(), '[[-10, 1], [0, -2], [10, -1], [20, 1], [40, 0]]')
        queue_mgr.add(-10, 20, -1)
        self.assertEqual(queue_mgr.to_string(), '[[0, -3], [10, -2], [20, 1], [40, 0]]')
        queue_mgr.add(20, 40, -1)
        self.assertEqual(queue_mgr.to_string(), '[[0, -3], [10, -2], [20, 0]]')
        queue_mgr.add(10, 20, 2)
        self.assertEqual(queue_mgr.to_string(), '[[0, -3], [10, 0]]')
        queue_mgr.add(0, 20, 3)
        self.assertEqual(queue_mgr.to_string(), '[[10, 3], [20, 0]]')
        queue_mgr.add(10, 20, -3)
        self.assertEqual(queue_mgr.to_string(), '[]')
        queue_mgr.add(-10, 40, 1)
        self.assertEqual(queue_mgr.to_string(), '[[-10, 1], [0, 1], [10, 1], [20, 1], [40, 0]]')


if __name__ == '__main__':
    unittest.main()
