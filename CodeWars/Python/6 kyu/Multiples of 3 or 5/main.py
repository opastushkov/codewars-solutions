def solution(n):
    return sum([x for x in range(3, n) if x % 3 == 0 or x % 5 == 0])  