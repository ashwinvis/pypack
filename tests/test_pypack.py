#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypack` package."""

import unittest
from warnings import warn

import pypack


class TestPypack(unittest.TestCase):
    """Tests for `pypack` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_something(self):
        """Test something."""
        pass

    def test_scm_version(self):
        """Test scm version."""
        if ".dev" in pypack.__version__:
            warn("At some distance from the last tagged release")
        if pypack.__version__[-8:].isdecimal():
            warn("Repository not clean, commit needed")
