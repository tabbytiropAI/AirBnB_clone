#!/usr/bin/python3
"""Unit tests for the BaseModel class in the models module."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModelInstantiation(unittest.TestCase):
    """Test cases for BaseModel class instantiation."""

    def test_default_instance(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_id_is_str(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_created_at_is_datetime(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_unique_ids(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_created_at_order(self):
        base_model1 = BaseModel()
        sleep(0.05)
        base_model2 = BaseModel()
        self.assertLess(base_model1.created_at, base_model2.created_at)

    def test_updated_at_order(self):
        base_model1 = BaseModel()
        sleep(0.05)
        base_model2 = BaseModel()
        self.assertLess(base_model1.updated_at, base_model2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = dt
        base_model_str = str(base_model)
        self.assertIn("[BaseModel] (123456)", base_model_str)
        self.assertIn("'id': '123456'", base_model_str)
        self.assertIn("'created_at': {!r}".format(dt), base_model_str)
        self.assertIn("'updated_at': {!r}".format(dt), base_model_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        base_model = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, dt)
        self.assertEqual(base_model.updated_at, dt)

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

class TestBaseModelSave(unittest.TestCase):
    """Test cases for the save method of the BaseModel class."""

    def test_save_updates_updated_at(self):
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertGreater(base_model.updated_at, original_updated_at)

    def test_save_with_arg_raises_type_error(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save(None)

class TestBaseModelToDict(unittest.TestCase):
    """Test cases for the to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.to_dict(), dict)

    def test_to_dict_contains_keys(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIn("id", base_model_dict)
        self.assertIn("created_at", base_model_dict)
        self.assertIn("updated_at", base_model_dict)
        self.assertIn("__class__", base_model_dict)

    def test_to_dict_datetime_attributes_as_str(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict["id"], str)
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()

