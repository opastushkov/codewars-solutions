def solution(s):
    ls = [s[x:x+2] for x in range(0, len(s)) if x % 2 == 0 and x != len(s)]
    if len(s) % 2 == 1: ls[-1] += "_"
    return ls