#!/usr/bin/python3
"""Unit tests for the City class in the models module."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.city import City

class TestCityInstantiation(unittest.TestCase):
    """Test cases for City class instantiation."""

    def test_default_instance(self):
        city = City()
        self.assertIsInstance(city, City)

    def test_stored_in_objects(self):
        city = City()
        self.assertIn(city, City.all().values())

    def test_id_is_str(self):
        city = City()
        self.assertIsInstance(city.id, str)

    def test_created_at_is_datetime(self):
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_updated_at_is_datetime(self):
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_name_is_class_attribute(self):
        self.assertTrue(hasattr(City, "name"))
        self.assertFalse(hasattr(City(), "name"))

    def test_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_created_at_order(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_updated_at_order(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = dt
        city_str = str(city)
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'created_at': {!r}".format(dt), city_str)
        self.assertIn("'updated_at': {!r}".format(dt), city_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, dt)
        self.assertEqual(city.updated_at, dt)

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

class TestCitySave(unittest.TestCase):
    """Test cases for the save method of the City class."""

    def test_save_updates_updated_at(self):
        city = City()
        original_updated_at = city.updated_at
        city.save()
        self.assertGreater(city.updated_at, original_updated_at)

    def test_save_with_arg_raises_type_error(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

class TestCityToDict(unittest.TestCase):
    """Test cases for the to_dict method of the City class."""

    def test_to_dict_type(self):
        city = City()
        self.assertIsInstance(city.to_dict(), dict)

    def test_to_dict_contains_keys(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)

    def test_to_dict_datetime_attributes_as_str(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict["id"], str)
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()

