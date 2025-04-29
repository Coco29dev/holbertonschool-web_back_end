#!/usr/bin/env python3
"""
Module de pagination simple.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retourne un tuple (start, end) pour paginer une séquence.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
