# -*- coding: utf-8 -*-

import unittest
from sphinx_testing import TestApp


class TestPackage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = TestApp(buildername='singlehtml',
                          srcdir='tests/sphinx/package')
        cls.app.build()

    def test(self):
        pass
