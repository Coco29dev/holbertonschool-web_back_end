#!/usr/bin/env python3
"""
Module asynchrone pour attendre un délai aléatoire.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un délai aléatoire compris entre 0 et max_delay, puis le retourne.
    """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
