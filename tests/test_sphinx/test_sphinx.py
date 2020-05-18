# -*- coding: utf-8 -*-
"""
    test_sphinx
    ~~~~~~~~~~~
    General Sphinx test and check output.
"""
import unittest
from sphinx_testing import TestApp


class TestSphinx(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = TestApp(buildername='singlehtml',
                          srcdir='tests/sphinx/basic')
        cls.app.build()

    def test(self):
        pass
