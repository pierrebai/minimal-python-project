import unittest
from unittest.mock import Mock, patch

import example

class TestExample(unittest.TestCase):
    '''
    The goal of these tests is to show how to write unit tests.
    '''

    def test_example_1(self):
        '''
        The goal of the test is to show how to write a unit test.
        '''
        self.assertTrue(True)
        self.assertNotEqual(55, 37)
        self.assertEqual(example.foo(3), 4)


    def test_example_2(self):
        '''
        The goal of the test is to show how to write a unit test.
        '''
        self.assertFalse(False)
        self.assertDictEqual({ 'foo': 1, 'bar': 2 }, { 'bar': 2, 'foo': 1 })
        self.assertEqual(example.bar(2), 14)


if __name__ == '__main__':
    unittest.main()

