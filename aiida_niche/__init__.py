# -*- coding: utf-8 -*-

"""
A plugin for the AiiDA framework to put interstitial impurities, using the ``niche`` code.
"""

__version__ = "0.0.1"

from ._generate_structures import GenerateStructures

__all__ = [
    "GenerateStructures",
]
