#!/usr/bin/python3
"""Unit tests for the Amenity class in the models module."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenityInstantiation(unittest.TestCase):
    """Test cases for Amenity class instantiation."""

    def test_default_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_stored_in_objects(self):
        amenity = Amenity()
        self.assertIn(amenity, Amenity.all().values())

    def test_id_is_str(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_created_at_is_datetime(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at_is_datetime(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_name_is_class_attribute(self):
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertFalse(hasattr(Amenity(), "name"))

    def test_unique_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_created_at_order(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_updated_at_order(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = dt
        amenity_str = str(amenity)
        self.assertIn("[Amenity] (123456)", amenity_str)
        self.assertIn("'id': '123456'", amenity_str)
        self.assertIn("'created_at': {!r}".format(dt), amenity_str)
        self.assertIn("'updated_at': {!r}".format(dt), amenity_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        amenity = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, dt)
        self.assertEqual(amenity.updated_at, dt)

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

class TestAmenitySave(unittest.TestCase):
    """Test cases for the save method of the Amenity class."""

    def test_save_updates_updated_at(self):
        amenity = Amenity()
        original_updated_at = amenity.updated_at
        amenity.save()
        self.assertGreater(amenity.updated_at, original_updated_at)

    def test_save_with_arg_raises_type_error(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

class TestAmenityToDict(unittest.TestCase):
    """Test cases for the to_dict method of the Amenity class."""

    def test_to_dict_type(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.to_dict(), dict)

    def test_to_dict_contains_keys(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)

    def test_to_dict_datetime_attributes_as_str(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict["id"], str)
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()

