# -*- coding: utf-8 -*-
"""
    test_sphinx
    ~~~~~~~~~~~
    General Sphinx test and check output.
"""

from sphinx_testing.util import path, with_app
import sphinxcontrib.lpblocks

srcdir = path(__file__).dirname().joinpath('sphinx').abspath()


def teardown_module():
    (srcdir / '_build').rmtree(True)


@with_app(srcdir=srcdir)
def test_sphinx(app, status, warning):
    app.builder.build_all()
    warnings = warning.getvalue()
    assert u'pylit' in warnings
