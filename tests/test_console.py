import unittest
import sys
import io
from contextlib import contextmanager
from models import *
from datetime import datetime
from console import HBNBCommand


@contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Test_Console(unittest.TestCase):
    """
    Test the console
    """
    def setUp(self):
        self.cli = HBNBCommand()
        test_args = {'updated_at': datetime(2017, 2, 11, 23, 48, 34, 339879),
                     'created_at': datetime(2017, 2, 11, 23, 48, 34, 339743),
                     'name': '\"Ace\"'}
        self.model = State(**test_args)
        self.model.save()

    def tearDown(self):
        self.model.delete()

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.cli.do_quit(self.cli)

    def test_show_correct(self):
        with captured_output() as (out, err):
            self.cli.do_show("State {}".format(self.model.id))
        output = out.getvalue().strip()
        self.assertFalse("2017, 2, 11, 23, 48, 34, 339879" in output)

    def test_show_error_no_args(self):
        with captured_output() as (out, err):
            self.cli.do_show('')
        output = out.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_error_missing_arg(self):
        with captured_output() as (out, err):
            self.cli.do_show("State")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_show("Human 1234-5678-9101")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_error_class_missing(self):
        with captured_output() as (out, err):
            self.cli.do_show("d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_create(self):
        with captured_output() as (out, err):
            self.cli.do_create('')
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

        with captured_output() as (out, err):
            self.cli.do_create("State name=\"steve\"")
        output = out.getvalue().strip()
        self.cli.do_destroy("State {}".format(output))

        with captured_output() as (out, err):
            self.cli.do_show("State {}".format(output))
        output2 = out.getvalue().strip()

    def test_destroy_correct(self):
        test_args = {'name': "\"steve\"",
                     'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900)}
        testmodel = State(**test_args)
        testmodel.save()
        self.cli.do_destroy("State {}".format(testmodel.id))
        with captured_output() as (out, err):
            self.cli.do_show("State {}".format(testmodel.id))
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_error_missing_id(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("State")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_error_class_missing(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("Human d3da85f2-499c-43cb-b33d-3d7935bc808c")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_error_invalid_id(self):
        with captured_output() as (out, err):
            self.cli.do_destroy("BaseModel " +
                                "f519fb40-1f5c-458b-945c-2e8eaaf4900")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_all_correct(self):
        test_args = {'name': '"steve"',
                     'updated_at': datetime(2017, 2, 12, 00, 31, 53, 331997),
                     'created_at': datetime(2017, 2, 12, 00, 31, 53, 331900),
                     }
        testmodel = State(**test_args)
        testmodel.save()
        with captured_output() as (out, err):
            self.cli.do_all("")
        output = out.getvalue().strip()
        self.assertTrue(testmodel.id in output)
        self.assertTrue(self.model.id in output)
        testmodel.delete()

    def test_all_correct_with_class(self):
        with captured_output() as (out, err):
            self.cli.do_all("State")
        output = out.getvalue().strip()
        self.assertTrue(len(output) > 0)
        self.assertTrue(self.model.id in output)

    def test_all_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_all("Human")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_correct(self):
        with captured_output() as (out, err):
            self.cli.do_update("State " +
                               "{} name Bay".format(
                                   self.model.id))
        output = out.getvalue().strip()

        with captured_output() as (out, err):
            self.cli.do_show("State {}".format(self.model.id))
        output = out.getvalue().strip()
        self.assertTrue("Bay" in output)
        self.assertFalse("Ace" in output)

    def test_update_error_invalid_id(self):
        with captured_output() as (out, err):
            self.cli.do_update("BaseModel 123-456-abc name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** no instance found **" or None)

    def test_update_error_no_id(self):
        with captured_output() as (out, err):
            self.cli.do_update("BaseModel name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** value missing **")

    def test_update_error_invalid_class(self):
        with captured_output() as (out, err):
            self.cli.do_update("Human " +
                               "d3da85f2-499c-43cb-b33d-3d7935bc808c name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_error_no_class(self):
        with captured_output() as (out, err):
            self.cli.do_update("d3da85f2-499c-43cb-b33d-3d7935bc808c name Cat")
        output = out.getvalue().strip()
        self.assertEqual(output, "** value missing **")

    def test_update_error_missing_value(self):
        with captured_output() as (out, err):
            self.cli.do_update("BaseModel " +
                               "d3da85f2-499c-43cb-b33d-3d7935bc808c name")
        output = out.getvalue().strip()
        self.assertEqual(output, "** value missing **")

if __name__ == "__main__":
    unittest.main()
