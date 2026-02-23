#!/usr/bin/env python3
"""
Module that contains the function filter_datum
"""
import re


def filter_datum(fields, redaction, message, separator):
    """Returns the log message obfuscated"""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
        r'\1=' + redaction, message
    )
