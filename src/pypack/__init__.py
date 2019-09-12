# -*- coding: utf-8 -*-

"""Top-level package for PyPack."""



__author__ = """Ashwin Vishnu Mohanan"""
__email__ = "ashwinvis@example.com"

try:
    from ._version import __version__
except ImportError:
    from pkg_resources import get_distribution
    __version__ = get_distribution(__package__).version
    del get_distribution
