#!/usr/bin/python3
"""Unit tests for the Place class in the models module."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlaceInstantiation(unittest.TestCase):
    """Test cases for Place class instantiation."""

    def test_default_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_stored_in_objects(self):
        place = Place()
        self.assertIn(place, Place.all().values())

    def test_id_is_str(self):
        place = Place()
        self.assertIsInstance(place.id, str)

    def test_created_at_is_datetime(self):
        place = Place()
        self.assertIsInstance(place.created_at, datetime)

    def test_updated_at_is_datetime(self):
        place = Place()
        self.assertIsInstance(place.updated_at, datetime)

    def test_city_id_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertFalse(hasattr(Place(), "city_id"))

    def test_user_id_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertFalse(hasattr(Place(), "user_id"))

    def test_name_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "name"))
        self.assertFalse(hasattr(Place(), "name"))

    def test_description_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "description"))
        self.assertFalse(hasattr(Place(), "description"))

    def test_number_rooms_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertFalse(hasattr(Place(), "number_rooms"))

    def test_number_bathrooms_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertFalse(hasattr(Place(), "number_bathrooms"))

    def test_max_guest_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertFalse(hasattr(Place(), "max_guest"))

    def test_price_by_night_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertFalse(hasattr(Place(), "price_by_night"))

    def test_latitude_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertFalse(hasattr(Place(), "latitude"))

    def test_longitude_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertFalse(hasattr(Place(), "longitude"))

    def test_amenities_is_class_attribute(self):
        self.assertTrue(hasattr(Place, "amenities"))
        self.assertFalse(hasattr(Place(), "amenities"))

    def test_unique_ids(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_created_at_order(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_updated_at_order(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = dt
        place_str = str(place)
        self.assertIn("[Place] (123456)", place_str)
        self.assertIn("'id': '123456'", place_str)
        self.assertIn("'created_at': {!r}".format(dt), place_str)
        self.assertIn("'updated_at': {!r}".format(dt), place_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        place = Place(id="345", created_at=dt_iso, updated_at=dt_iso, city_id="c123", user_id="u123", name="My Place", description="A cozy place", number_rooms=2, number_bathrooms=1, max_guest=4, price_by_night=100, latitude=12.34, longitude=56.78, amenities=["WiFi", "TV"])
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, dt)
        self.assertEqual(place.updated_at, dt)
        self.assertEqual(place.city_id, "c123")
        self.assertEqual(place.user_id, "u123")
        self.assertEqual(place.name, "My Place")
        self.assertEqual(place.description, "A cozy place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 12.34)
        self.assertEqual(place.longitude, 56.78)
        self.assertEqual(place.amenities, ["WiFi", "TV"])

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None, city_id=None, user_id=None, name=None, description=None, number_rooms=None, number_bathrooms=None, max_guest=None, price_by_night=None, latitude=None, longitude=None, amenities=None)

class TestPlaceSave(unittest.TestCase):
    """Test cases for the save method of the Place class."""

    def test_save_updates_updated_at(self):
        place = Place()
        original_updated_at = place.updated_at
        place.save()
        self.assertGreater(place.updated_at, original_updated_at)

    def test_save_with_arg_raises_type_error(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

class TestPlaceToDict(unittest.TestCase):
    """Test cases for the to_dict method of the Place class."""

    def test_to_dict_type(self):
        place = Place()
        self.assertIsInstance(place.to_dict(), dict)

    def test_to_dict_contains_keys(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)
        self.assertIn("city_id", place_dict)
        self.assertIn("user_id", place_dict)
        self.assertIn("name", place_dict)
        self.assertIn("description", place_dict)
        self.assertIn("number_rooms", place_dict)
        self.assertIn("number_bathrooms", place_dict)
        self.assertIn("max_guest", place_dict)
        self.assertIn("price_by_night", place_dict)
        self.assertIn("latitude", place_dict)
        self.assertIn("longitude", place_dict)
        self.assertIn("amenities", place_dict)

    def test_to_dict_datetime_attributes_as_str(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict["id"], str)
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()

