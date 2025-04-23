#!/usr/bin/env python3
"""
Module de transformation de données typées en tuple.
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Retourne un tuple contenant une chaîne et
    le carré d'un entier ou d'un flottant.
    """
    return (k, v * v)
