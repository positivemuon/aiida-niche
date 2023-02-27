# -*- coding: utf-8 -*-

# Author: Pietro Bonfa'
"""
Tests that the entrypoints are loadable through their respective factory.
"""


def test_entrypoints(check_entrypoints):
    """
    Check that the entrypoints are valid.
    """
    check_entrypoints('aiida_niche')
