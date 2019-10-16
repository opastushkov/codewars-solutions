def binary_to_string(b):
    return ''.join([chr(int(b[x:x+8], 2)) for x in range(0, len(b), 8)])
    