#!/usr/bin/python3

"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

# ... (rest of your code remains unchanged)


# ... (unchanged code above)

class TestAmenity_instantiation(unittest.TestCase):
    # ... (unchanged code above)

    def test_name_is_public_class_attribute(self):
        am = Amenity()
        self.assertEqual(str, type(am.name))  # Fix: Replace Amenity.name with am.name
        self.assertIn("name", dir(am))
        self.assertNotIn("name", am.__dict__)

    # ... (unchanged code below)

class TestAmenity_to_dict(unittest.TestCase):
    # ... (unchanged code above)

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)  # Use assertDictEqual

    # ... (unchanged code below)

