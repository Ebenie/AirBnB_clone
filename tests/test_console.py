#!/usr/bin/python3
"""the console module unit test code"""
import os
import io
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_command(self, mock_stdout):
        with patch('builtins.input', return_value="quit"):
            self.console.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_EOF_command(self, mock_stdout):
        with patch('builtins.input', return_value="EOF"):
            self.console.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_emptyline_command(self, mock_stdout):
        with patch('builtins.input', return_value=""):
            self.console.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_command(self, mock_stdout):
        with patch('builtins.input', return_value="create BaseModel"):
            self.console.cmdloop()
            self.assertIn("created", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_command(self, mock_stdout):
        with patch('builtins.input', return_value="show BaseModel"):
            self.console.cmdloop()
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_destroy_command(self, mock_stdout):
        with patch('builtins.input', return_value="destroy BaseModel"):
            self.console.cmdloop()
            self.assertIn("** instance id missing **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_all_command(self, mock_stdout):
        with patch('builtins.input', return_value="all BaseModel"):
            self.console.cmdloop()
            self.assertIn("** class doesn't exist **", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_command(self, mock_stdout):
        with patch('builtins.input', return_value="update BaseModel"):
            self.console.cmdloop()
            self.assertIn("** instance id missing **", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()



