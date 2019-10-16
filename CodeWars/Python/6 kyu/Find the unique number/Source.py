def find_uniq(arr):
    return max(arr) if arr.count(max(arr)) == 1 else min(arr)