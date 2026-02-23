#!/usr/bin/env python3
"""
Module for filtering and obfuscating personally identifiable information
in log messages and providing a secure logger for user data.
"""
import re
import logging
import os
from typing import List, Tuple
import mysql.connector


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates the values of specified fields in a log message."""
    return re.sub(
        r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
        r'\1=' + redaction, message
    )


class RedactingFormatter(logging.Formatter):
    """Formatter that redacts sensitive PII fields in log records."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes the formatter with the list of fields to redact."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters PII field values in the log record before formatting."""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        record.args = None
        return super().format(record)


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a MySQL database connector using
    environment variable credentials."""
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def get_logger() -> logging.Logger:
    """Returns a logger named user_data configured to redact PII fields."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger
