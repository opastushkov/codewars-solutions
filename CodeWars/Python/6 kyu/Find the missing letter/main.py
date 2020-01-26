def find_missing_letter(chars):
    return ''.join([chr(ord(chars[x]) + 1) for x in range(len(chars) - 1) if ord(chars[x + 1]) - ord(chars[x])  > 1])

