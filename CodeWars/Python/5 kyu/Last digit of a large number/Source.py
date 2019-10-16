def last_digit(n1, n2):
    if not n2: return 1
    digits = ((0,),
              (1,), 
              (2, 4, 8, 6), 
              (3, 9, 7, 1), 
              (4, 6), 
              (5,), 
              (6,),
              (7, 9, 3, 1), 
              (8, 4, 2, 6), 
              (9, 1)
              )
    last_n1 = int(str(n1)[-1])
    reminder = n2%len(digits[last_n1])-1
    return digits[int(str(n1)[-1])][reminder]