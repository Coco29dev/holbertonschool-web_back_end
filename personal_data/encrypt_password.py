#!/usr/bin/env python3
"""
Password hashing module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt (salted + hashed).
    Returns the hashed password as bytes.
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that the provided password matches the hashed password.
    Returns True if match, otherwise False.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
