#!/usr/bin/env python3
"""
Module asynchrone pour exécuter plusieurs délais aléatoires en parallèle.
"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance n fois la coroutine wait_random avec max_delay et retourne
    les délais dans l'ordre d'exécution.
    """
    ma_list = []
    coroutine = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(coroutine):
        resultat = await task
        ma_list.append(resultat)
    return ma_list
