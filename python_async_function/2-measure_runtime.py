#!/usr/bin/env python3
"""
Module pour mesurer le temps moyen d'exécution d'une coroutine asynchrone.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay) -> float:
    """
    Mesure le temps moyen d'attente pour exécuter wait_n n fois.
    """
    départ = time.time()
    asyncio.run(wait_n(n, max_delay))
    fin = time.time()
    total = fin - départ
    return total / n
