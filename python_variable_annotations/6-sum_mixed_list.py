#!/usr/bin/python3
"""
Module pour effectuer la somme d'une liste avec des entiers et des flottants.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calcule et retourne la somme d'une liste de nombres entiers et flottants.
    """
    return sum(mxd_lst)
