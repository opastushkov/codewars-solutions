alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    return ' '.join([str(alphabet.index(x.lower()) + 1) for x in text if x.isalpha()])