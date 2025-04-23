#!/usr/bin/env python3
"""
Module pour créer une tâche asynchrone avec un délai aléatoire.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Crée et retourne une tâche asyncio pour exécuter wait_random.
    """
    resultat = asyncio.create_task(wait_random(max_delay))
    return resultat
