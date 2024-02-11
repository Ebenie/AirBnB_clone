#!/usr/bin/python3
import unittest
from models.city import City

class TestCity(unittest.TestCase):

    city = City()
    self.assertTrue(hasattr(city, 'state_id'))
    self.assertTrue(hasattr(city, 'name'))
    self.assertEqual(city.state_id, "")
    self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()

