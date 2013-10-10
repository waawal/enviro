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
FIXTURE = os.path.join(TEST_DIR, 'fixtures', 'mysettings.conf')


class TestCWD(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(FIXTURE, os.path.join(os.getcwd(), 'mysettings.conf'))

    def test_something(self):
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ.get('foodir'), 'frob/whatever')


    def tearDown(self):
        os.remove(os.path.join(os.getcwd(), 'mysettings.conf'))


class TestHome(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(FIXTURE, os.path.join(os.path.expanduser('~'), 'mysettings.conf'))

    def test_something(self):
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ.get('foodir'), 'frob/whatever')


    def tearDown(self):
        os.remove(os.path.join(os.path.expanduser('~'), 'mysettings.conf'))

class TestETC(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(FIXTURE, os.path.join('/etc', 'mysettings.conf'))

    def test_something(self):
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ.get('foodir'), 'frob/whatever')


    def tearDown(self):
        os.remove(os.path.join('/etc', 'mysettings.conf'))


class TestScriptPath(unittest.TestCase):

    def setUp(self):
        shutil.copyfile(FIXTURE, os.path.join(os.path.dirname(os.path.realpath(__main__.__file__)),
                                                              'mysettings.conf'))

    def test_something(self):
        enviro.setdefault('mysettings.conf')
        self.failUnlessEqual(os.environ.get('foodir'), 'frob/whatever')


    def tearDown(self):
        os.remove(os.path.join(os.path.dirname(os.path.realpath(__main__.__file__)),
                                                              'mysettings.conf'))


if __name__ == '__main__':
    unittest.main()