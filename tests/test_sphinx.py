# -*- coding: utf-8 -*-
"""
    test_sphinx
    ~~~~~~~~~~~

    Basic test of Sphinx for testing
"""

from sphinx_testing.util import with_app

@with_app(buildername='html', srcdir='tests/fixtures/test_sphinx')
def test_sphinx(app, status, warning):
    app.builder.build_all()


