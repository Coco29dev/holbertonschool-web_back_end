#!/usr/bin/env python3
"""
Module pour récupérer des nombres flottants de manière asynchrone.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Récupère 10 nombres flottants générés de façon asynchrone.

    Retourne:
        Liste de 10 flottants.
    """
    result = [value async for value in async_generator() if value < 11]
    return result
