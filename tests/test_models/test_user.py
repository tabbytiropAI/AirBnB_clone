#!/usr/bin/python3
"""Unit tests for the User class in the models module."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.user import User

class TestUserInstantiation(unittest.TestCase):
    """Test cases for User class instantiation."""

    def test_default_instance(self):
        user = User()
        self.assertIsInstance(user, User)

    def test_stored_in_objects(self):
        user = User()
        self.assertIn(user, User.all().values())

    def test_id_is_str(self):
        user = User()
        self.assertIsInstance(user.id, str)

    def test_created_at_is_datetime(self):
        user = User()
        self.assertIsInstance(user.created_at, datetime)

    def test_updated_at_is_datetime(self):
        user = User()
        self.assertIsInstance(user.updated_at, datetime)

    def test_email_is_class_attribute(self):
        self.assertTrue(hasattr(User, "email"))
        self.assertFalse(hasattr(User(), "email"))

    def test_password_is_class_attribute(self):
        self.assertTrue(hasattr(User, "password"))
        self.assertFalse(hasattr(User(), "password"))

    def test_first_name_is_class_attribute(self):
        self.assertTrue(hasattr(User, "first_name"))
        self.assertFalse(hasattr(User(), "first_name"))

    def test_last_name_is_class_attribute(self):
        self.assertTrue(hasattr(User, "last_name"))
        self.assertFalse(hasattr(User(), "last_name"))

    def test_unique_ids(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at_order(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_updated_at_order(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = dt
        user_str = str(user)
        self.assertIn("[User] (123456)", user_str)
        self.assertIn("'id': '123456'", user_str)
        self.assertIn("'created_at': {!r}".format(dt), user_str)
        self.assertIn("'updated_at': {!r}".format(dt), user_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso, email="test@test.com", password="test123", first_name="John", last_name="Doe")
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, dt)
        self.assertEqual(user.updated_at, dt)
        self.assertEqual(user.email, "test@test.com")
        self.assertEqual(user.password, "test123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None, email=None, password=None, first_name=None, last_name=None)

class TestUserSave(unittest.TestCase):
    """Test cases for the save method of the User class."""

    def test_save_updates_updated_at(self):
        user = User()
        original_updated_at = user.updated_at
        user.save()
        self.assertGreater(user.updated_at, original_updated_at)

    def test_save_with_arg_raises_type_error(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

class TestUserToDict(unittest.TestCase):
    """Test cases for the to_dict method of the User class."""

    def test_to_dict_type(self):
        user = User()
        self.assertIsInstance(user.to_dict(), dict)

    def test_to_dict_contains_keys(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)

    def test_to_dict_datetime_attributes_as_str(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict["id"], str)
        self.assertIsInstance(user_dict["created_at"], str)
        self.assertIsInstance(user_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()

