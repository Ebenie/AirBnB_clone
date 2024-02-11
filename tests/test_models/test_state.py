#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):

    state = State()
    self.assertTrue(hasattr(self.state, 'name'))
    self.assertEqual(self.state.name, "")

if __name__ == '__main__':
    unittest.main()

