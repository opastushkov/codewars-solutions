def binary_to_string(binary):
    return "".join(chr(int(x, 2)) for x in binary.split('0b')[1:])