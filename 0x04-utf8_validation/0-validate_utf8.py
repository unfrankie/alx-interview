#!/usr/bin/python3
def validUTF8(data):
    def is_valid_byte(byte):
        return 0 <= byte <= 255

    n_bytes = 0

    for byte in data:
        if not is_valid_byte(byte):
            return False

        if n_bytes == 0:
            if byte >> 5 == 0b110:
                n_bytes = 1
            elif byte >> 4 == 0b1110:
                n_bytes = 2
            elif byte >> 3 == 0b11110:
                n_bytes = 3
            elif byte >> 7:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
