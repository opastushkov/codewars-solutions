def grille(message, code):
    return ''.join([message[x] for x in reversed(range(-1, -len(message) - 1, -1)) if bin(code)[2:].zfill(len(message))[x] == '1'])