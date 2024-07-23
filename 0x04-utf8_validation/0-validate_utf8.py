#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for byte in data:
        if num_bytes > 0:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1
        else:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
            num_bytes -= 1
    return num_bytes == 0
