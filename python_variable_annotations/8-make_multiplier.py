#!/usr/bin/env python3
"""
Module pour générer des fonctions de multiplication dynamiques.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Retourne une fonction qui multiplie une
    valeur float par le multiplicateur donné.
    """

    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
