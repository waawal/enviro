#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_enviro
----------------------------------

Tests for `enviro` module.
"""
import sys

sys.path.append('../') # Yeah... well... The price you have to pay.

import os
import shutil
import unittest
import __main__

import enviro

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
SETTINGS1 = os.path.join(TEST_DIR, 'fixtures', 'mysettings.conf')
SETTINGS2 = os.path.join(TEST_DIR, 'fixtures', 'myothersettings.conf')
print SETTINGS1, SETTINGS2


class TestCWD(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(SETTINGS1, os.path.join(os.getcwd(), 'mysettings.conf'))

    def test_something(self):
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ['foodir'], 'frob/whatever')


    def tearDown(self):
        os.remove(os.path.join(os.getcwd(), 'mysettings.conf'))
        os.environ = {}


class TestHome(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(SETTINGS1, os.path.join(os.path.expanduser('~'),
                                              'mysettings.conf'))

    def test_something(self):
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ['foodir'], 'frob/whatever')


    def tearDown(self):
        os.remove(os.path.join(os.path.expanduser('~'), 'mysettings.conf'))
        os.environ = {}

class TestETC(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(SETTINGS1, os.path.join('/etc', 'mysettings.conf'))

    def test_something(self):
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ['foodir'], 'frob/whatever')

    def tearDown(self):
        os.remove(os.path.join('/etc', 'mysettings.conf'))
        os.environ = {}


class TestScriptPath(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(SETTINGS1, os.path.join(
            os.path.dirname(os.path.realpath(__main__.__file__)),
            'mysettings.conf'))

    def test_something(self):
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ['foodir'], 'frob/whatever')

    def tearDown(self):
        os.remove(os.path.join(
            os.path.dirname(os.path.realpath(__main__.__file__)),
            'mysettings.conf'))
        os.environ = {}


class TestOverrides(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(SETTINGS1, os.path.join('/etc', 'mysettings.conf'))
        shutil.copyfile(SETTINGS2, os.path.join(os.getcwd(), 'mysettings.conf'))

    def test_something(self):
        print "now!"
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ['foodir'], 'yolo/whatever')

    def tearDown(self):
        os.remove(os.path.join('/etc', 'mysettings.conf'))
        os.remove(os.path.join(os.getcwd(), 'mysettings.conf'))
        os.environ = {}


if __name__ == '__main__':
    unittest.main()