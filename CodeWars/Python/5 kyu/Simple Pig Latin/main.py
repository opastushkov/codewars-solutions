def pig_it(text):
    return ' '.join([ x[1:] + x[0] + 'ay' if all([i.isalpha() for i in x]) else x for x in text.split()])