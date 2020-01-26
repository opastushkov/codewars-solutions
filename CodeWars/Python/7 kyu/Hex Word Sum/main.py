def hex_word_sum(s):
    sum = 0
    for x in s.replace('O', '0').replace('S', '5').split():
        try: sum += int(x, 16)
        except: pass
    return sum