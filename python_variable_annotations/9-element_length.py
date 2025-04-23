#!/usr/bin/python3
"""
Module pour calculer la longueur des éléments dans une séquence itérable.
"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Retourne une liste de tuples contenant chaque élément de la séquence
    et sa longueur.
    """
    return [(i, len(i)) for i in lst]
