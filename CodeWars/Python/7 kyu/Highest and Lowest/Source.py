def high_and_low(numbers):
    return str(max([int(x) for x in numbers.split()])) + ' ' + str(min([int(x) for x in numbers.split()]))