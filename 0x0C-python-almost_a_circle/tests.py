#!/usr/bin/python3
"""Unittest for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """testcase is created by subclassing unittest.TestCase"""
    def setUp(self):
        """Prepare the test fixture - Assign private class attribute """
        Base._Base__nb_objects = 0

    def test_create_an_instance_id_int(self):
        """Testing id property with int type"""
        test_base = Base(145)
        self.assertEqual(test_base.id, 145)

    def test_create_a_neg_id_int(self):
        """Testing id property with negative int type"""
        test_base = Base(-12)
        self.assertEqual(test_base.id, -12)

    def test_create_a_float_id(self):
        """Testing id property with float type"""
        test_base = Base(1.5)
        self.assertEqual(test_base.id, 1.5)

    def test_create_an_empty_instance_id(self):
        """Testing id property without attribute"""
        test_base = Base()
        self.assertEqual(test_base.id, 1)

    def test_create_instance_with_more_id_args(self):
        """Testing id property with more arguments"""
        with self.assertRaises(TypeError):
            test_base = Base(2, 4)


if __name__ == '__main__':
    unittest.main()
