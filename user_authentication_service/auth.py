#!/usr/bin/env python3
"""Auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt using a generated salt

    Args:
        password: the plain-text password to hash

    Returns:
        The salted hash of the password as bytes
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
