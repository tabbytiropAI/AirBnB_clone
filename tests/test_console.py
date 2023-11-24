#!/usr/bin/python3
"""Unittests for HBNB command interpreter."""

import unittest
from unittest.mock import patch
from io import StringIO
import console
from console import HBNBCommand, BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Unittests for HBNB command interpreter."""
    def setUp(self):
        self.hbnb_command = HBNBCommand()

    def test_empty_line_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("")
            out = mock_stdout.getvalue().strip()
            self.assertEqual(out, "")

    def test_default_unknown_syntax_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("unknown_syntax")
            out = mock_stdout.getvalue().strip()
            self.assertEqual(out, "*** Unknown syntax: unknown_syntax")

    def test_do_quit_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            res = self.hbnb_command.onecmd("quit")
            out = mock_stdout.getvalue().strip()
            self.assertTrue(res)
            self.assertEqual(out, "")

    def test_do_EOF_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            res = self.hbnb_command.onecmd("EOF")
            out = mock_stdout.getvalue().strip()
            self.assertTrue(res)
            self.assertEqual(out, "")

    def test_do_create_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            out = mock_stdout.getvalue().strip()
            self.assertTrue(out)

    def test_do_show_missing_class_name_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("show")
            out = mock_stdout.getvalue().strip()
            self.assertEqual(out, "** class name missing **")

    def test_do_destroy_invalid_class_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("destroy InvalidClass")
            out = mock_stdout.getvalue().strip()
            self.assertEqual(out, "** class doesn't exist **")

    def test_do_all_no_class_instances_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("all BaseModel")
            out = mock_stdout.getvalue().strip()
            self.assertEqual(out, "[]")

    def test_do_count_(self):
        """Test do count """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("count BaseModel")
            out = mock_stdout.getvalue().strip()
            self.assertTrue(out.isdigit())

    def test_do_update_invalid_instance_id_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd("update BaseModel invalid_id")
            out = mock_stdout.getvalue().strip()
            self.assertEqual(out, "** no instance found **")

    def test_do_update_missing_value_(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd
            ("update BaseModel valid_id attribute_name")
            out = mock_stdout.getvalue().strip()
            self.assertEqual(out, "** value missing **")

        """create instance"""
    def create_instance_(self, class_name):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.hbnb_command.onecmd(f"create {class_name}")
            out = mock_stdout.getvalue().strip()
            return out


if __name__ == '__main__':
    unittest.main()
