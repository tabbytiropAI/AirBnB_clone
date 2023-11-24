#!/usr/bin/python3
"""Unit tests for the State class in the models module."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.state import State

class TestStateInstantiation(unittest.TestCase):
    """Test cases for State class instantiation."""

    def test_default_instance(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_stored_in_objects(self):
        state = State()
        self.assertIn(state, State.all().values())

    def test_id_is_str(self):
        state = State()
        self.assertIsInstance(state.id, str)

    def test_created_at_is_datetime(self):
        state = State()
        self.assertIsInstance(state.created_at, datetime)

    def test_updated_at_is_datetime(self):
        state = State()
        self.assertIsInstance(state.updated_at, datetime)

    def test_name_is_class_attribute(self):
        self.assertTrue(hasattr(State, "name"))
        self.assertFalse(hasattr(State(), "name"))

    def test_unique_ids(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_created_at_order(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_updated_at_order(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = dt
        state_str = str(state)
        self.assertIn("[State] (123456)", state_str)
        self.assertIn("'id': '123456'", state_str)
        self.assertIn("'created_at': {!r}".format(dt), state_str)
        self.assertIn("'updated_at': {!r}".format(dt), state_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, dt)
        self.assertEqual(state.updated_at, dt)

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

class TestStateSave(unittest.TestCase):
    """Test cases for the save method of the State class."""

    def test_save_updates_updated_at(self):
        state = State()
        original_updated_at = state.updated_at
        state.save()
        self.assertGreater(state.updated_at, original_updated_at)

    def test_save_with_arg_raises_type_error(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

class TestStateToDict(unittest.TestCase):
    """Test cases for the to_dict method of the State class."""

    def test_to_dict_type(self):
        state = State()
        self.assertIsInstance(state.to_dict(), dict)

    def test_to_dict_contains_keys(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)

    def test_to_dict_datetime_attributes_as_str(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict["id"], str)
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()

