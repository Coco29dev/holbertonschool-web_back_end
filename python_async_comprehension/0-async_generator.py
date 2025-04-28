#!/usr/bin/env python3
"""
Module async_generator
Génère des nombres aléatoires de manière asynchrone.
"""


import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """
    Coroutine asynchrone générant 10 nombres
    flottants aléatoires entre 0 et 10,
    avec une pause d'une seconde entre chaque génération.
    """

    for _ in range(10):
        i = random.uniform(0, 10)
        yield i
        await asyncio.sleep(1)
