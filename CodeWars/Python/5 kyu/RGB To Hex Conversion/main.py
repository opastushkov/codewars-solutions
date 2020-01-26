def f(num):
    if num > 255: return 255
    elif num < 0: return 0
    else: return num

def rgb(r, g, b):
    return '{:02X}{:02X}{:02X}'.format(f(r), f(g), f(b))