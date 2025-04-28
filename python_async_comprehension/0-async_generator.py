#!/usr/bin/env python3
"""
Module async_generator
Génère des nombres aléatoires de manière asynchrone.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine asynchrone générant 10 nombres
    flottants aléatoires entre 0 et 10,
    avec une pause d'une seconde entre chaque génération.
    """

    for _ in range(10):
        i = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield i
