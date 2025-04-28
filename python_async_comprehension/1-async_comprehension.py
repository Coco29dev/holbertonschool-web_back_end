#!/usr/bin/env python3

import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    result = [value async for value in async_generator() if value < 11]
    return result