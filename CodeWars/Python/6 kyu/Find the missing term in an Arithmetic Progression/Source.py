def find_missing(s):
    step = min(s[1] - s[0], s[2] - s[1])
    for x in range(1, len(s)):
        if s[x] != s[0] + x * step:
            return s[0] + x * step
