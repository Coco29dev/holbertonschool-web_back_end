#!/usr/bin/env python3

"""
Module de mesure de la durée d'exécution d'une coroutine.

Ce module utilise asyncio pour exécuter des coroutines en parallèle
et mesure le temps total nécessaire à leur exécution.
"""


import asyncio
import time
from typing import Awaitable


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure et retourne le temps d'exécution pour lancer
    async_comprehension en parallèle.

    Retourne :
        float : Durée totale d'exécution en secondes.
    """
    depart = time.time()
    await asyncio.gather(async_comprehension())
    fin = time.time()
    total = fin - depart
    return total
