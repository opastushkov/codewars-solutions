def wave(str):
    return [str[:it] + str[it].upper() + str[it + 1:] for it, x in enumerate(str) if x is not ' ']