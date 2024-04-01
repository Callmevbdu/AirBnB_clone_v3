#!/usr/bin/python3
"""
Contains the TestAmenityDocs classes
"""

from datetime import datetime
import inspect
import models
from models import amenity
import pep8
import unittest
import os
import json
import unittest

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_amenity_creation(self):
        """Test creating an Amenity object"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_name_default_value(self):
        """Test default value of name attribute"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_name_set_value(self):
        """Test setting a value for the name attribute"""
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")

if __name__ == '__main__':
    unittest.main()

