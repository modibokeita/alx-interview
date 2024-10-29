#!/usr/bin/python3
"""
UTF-8 Validation module
"""

def validUTF8(data):
    """Checks if the given data set is a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the significant bits in each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get only the least significant 8 bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes based on the leading bits
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # For 1-byte characters, reset num_bytes to 0 and continue
            if num_bytes == 0:
                continue

            # Invalid scenarios for UTF-8:
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0

