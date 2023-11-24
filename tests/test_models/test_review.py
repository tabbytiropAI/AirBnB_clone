#!/usr/bin/python3
"""Unit tests for the Review class in the models module."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

class TestReviewInstantiation(unittest.TestCase):
    """Test cases for Review class instantiation."""

    def test_default_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_stored_in_objects(self):
        review = Review()
        self.assertIn(review, Review.all().values())

    def test_id_is_str(self):
        review = Review()
        self.assertIsInstance(review.id, str)

    def test_created_at_is_datetime(self):
        review = Review()
        self.assertIsInstance(review.created_at, datetime)

    def test_updated_at_is_datetime(self):
        review = Review()
        self.assertIsInstance(review.updated_at, datetime)

    def test_place_id_is_class_attribute(self):
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertFalse(hasattr(Review(), "place_id"))

    def test_user_id_is_class_attribute(self):
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertFalse(hasattr(Review(), "user_id"))

    def test_text_is_class_attribute(self):
        self.assertTrue(hasattr(Review, "text"))
        self.assertFalse(hasattr(Review(), "text"))

    def test_unique_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_created_at_order(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.created_at, review2.created_at)

    def test_updated_at_order(self):
        review1 = Review()
        sleep(0.05)
        review2 = Review()
        self.assertLess(review1.updated_at, review2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        review = Review()
        review.id = "123456"
        review.created_at = review.updated_at = dt
        review_str = str(review)
        self.assertIn("[Review] (123456)", review_str)
        self.assertIn("'id': '123456'", review_str)
        self.assertIn("'created_at': {!r}".format(dt), review_str)
        self.assertIn("'updated_at': {!r}".format(dt), review_str)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        review = Review(id="345", created_at=dt_iso, updated_at=dt_iso, place_id="p123", user_id="u123", text="This is a review.")
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, dt)
        self.assertEqual(review.updated_at, dt)
        self.assertEqual(review.place_id, "p123")
        self.assertEqual(review.user_id, "u123")
        self.assertEqual(review.text, "This is a review.")

    def test_instantiation_with_none_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None, place_id=None, user_id=None, text=None)

class TestReviewSave(unittest.TestCase):
    """Test cases for the save method of the Review class."""

    def test_save_updates_updated_at(self):
        review = Review()
        original_updated_at = review.updated_at
        review.save()
        self.assertGreater(review.updated_at, original_updated_at)

    def test_save_with_arg_raises_type_error(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

class TestReviewToDict(unittest.TestCase):
    """Test cases for the to_dict method of the Review class."""

    def test_to_dict_type(self):
        review = Review()
        self.assertIsInstance(review.to_dict(), dict)

    def test_to_dict_contains_keys(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("place_id", review_dict)
        self.assertIn("user_id", review_dict)
        self.assertIn("text", review_dict)

    def test_to_dict_datetime_attributes_as_str(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict["id"], str)
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()

