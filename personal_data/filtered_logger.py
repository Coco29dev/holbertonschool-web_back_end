#!/usr/bin/env python3
"""
Module that contains the function filter_datum
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Returns the log message obfuscated"""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
        r'\1=' + redaction, message
    )
