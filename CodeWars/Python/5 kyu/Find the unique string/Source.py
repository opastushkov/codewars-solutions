def find_uniq(arr):
    first = set(arr[0].lower()) if set(arr[0].lower()) == set(arr[1].lower()) else set(arr[2].lower())
    for x in arr:
        if not set(x.lower()) == first:
            return x