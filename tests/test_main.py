# tests/test_main.py

import unittest
from dudu.main import find_common_elements

class TestDudu(unittest.TestCase):
    def test_find_common_elements(self):
        result = find_common_elements(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])
        expected = [('banana', 3), ('apple', 2), ('orange', 1)]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
